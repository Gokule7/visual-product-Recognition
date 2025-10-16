from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import numpy as np
import os
import pandas as pd
from werkzeug.utils import secure_filename
from feature_extractor import FeatureExtractor, cosine_similarity

app = Flask(__name__)

# Configure CORS to allow requests from Netlify frontend
CORS(app, resources={
    r"/*": {
        "origins": [
            "http://localhost:3000",
            "https://visual-product-recognition.netlify.app",
            "https://*.netlify.app",
            "https://*.netlify.com"
        ],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"],
        "supports_credentials": True
    }
})

# Config
UPLOAD_FOLDER = 'temp_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Make sure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Global variables to store our product data
product_data = None
product_features = None
extractor = None
data_base_dir = None  # Will be set when database loads

def allowed_file(filename):
    """Check if uploaded file has valid extension"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def load_product_database():
    """Load the gallery products and their features"""
    global product_data, product_features, extractor, data_base_dir
    
    print("Loading product database...")
    
    # Initialize feature extractor
    extractor = FeatureExtractor()
    
    # Load gallery CSV - handle both local and deployed environments
    backend_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Try different possible paths
    possible_base_dirs = [
        os.path.dirname(backend_dir),  # Parent of backend folder
        backend_dir,  # Current directory (for Render)
        os.getcwd()  # Working directory
    ]
    
    gallery_path = None
    for base_dir in possible_base_dirs:
        test_path = os.path.join(base_dir, 'development_test_data', 'gallery.csv')
        if os.path.exists(test_path):
            gallery_path = test_path
            print(f"Found gallery.csv at: {gallery_path}")
            break
    
    if gallery_path is None:
        raise FileNotFoundError("Could not find gallery.csv in any expected location")
    
    product_data = pd.read_csv(gallery_path)
    
    # Store the base directory for image paths
    data_base_dir = os.path.dirname(os.path.dirname(gallery_path))
    
    # Check if we have cached features
    backend_dir = os.path.dirname(os.path.abspath(__file__))
    features_cache = os.path.join(backend_dir, 'product_features.npy')
    
    if os.path.exists(features_cache):
        print("Loading cached product features...")
        product_features = np.load(features_cache)
        print(f"Loaded {len(product_features)} product features from cache")
    else:
        print("Extracting features from product images (this may take a while)...")
        features_list = []
        
        for idx, row in product_data.iterrows():
            img_path = os.path.join(data_base_dir, 'development_test_data', row['img_path'])
            
            if os.path.exists(img_path):
                features = extractor.extract_from_path(img_path)
                if features is not None:
                    features_list.append(features)
                else:
                    # Use zero vector if extraction fails
                    features_list.append(np.zeros(1280))
            else:
                features_list.append(np.zeros(1280))
            
            if (idx + 1) % 100 == 0:
                print(f"Processed {idx + 1}/{len(product_data)} images")
        
        product_features = np.array(features_list)
        np.save(features_cache, product_features)
        print(f"Saved {len(product_features)} features to cache")

@app.route('/', methods=['GET'])
def home():
    """Health check endpoint"""
    return "Visual Product Matcher Backend Running"

@app.route('/images/<path:filename>')
def serve_image(filename):
    """Serve product images from the dataset"""
    global data_base_dir
    
    if data_base_dir is None:
        # Fallback if database not loaded yet
        backend_dir = os.path.dirname(os.path.abspath(__file__))
        possible_bases = [
            os.path.dirname(backend_dir),
            backend_dir,
            os.getcwd()
        ]
        for base in possible_bases:
            test_dir = os.path.join(base, 'development_test_data')
            if os.path.exists(test_dir):
                image_dir = test_dir
                break
        else:
            return jsonify({'error': 'Image directory not found'}), 404
    else:
        image_dir = os.path.join(data_base_dir, 'development_test_data')
    
    return send_from_directory(image_dir, filename)

@app.route('/api/search', methods=['POST'])
def search_products():
    """
    Main search endpoint - accepts either uploaded image or URL
    Returns top 10 similar products
    """
    
    if product_data is None or product_features is None:
        return jsonify({'error': 'Product database not loaded'}), 500
    
    query_features = None
    
    # Check if it's a file upload
    if 'file' in request.files:
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if file and allowed_file(file.filename):
            # Extract features from uploaded file
            query_features = extractor.extract_from_upload(file)
            
            if query_features is None:
                return jsonify({'error': 'Failed to process image'}), 400
        else:
            return jsonify({'error': 'Invalid file type. Please upload an image'}), 400
    
    # Check if it's a URL
    elif request.is_json and 'url' in request.json:
        img_url = request.json['url']
        
        if not img_url:
            return jsonify({'error': 'URL cannot be empty'}), 400
        
        # Extract features from URL
        query_features = extractor.extract_from_url(img_url)
        
        if query_features is None:
            return jsonify({'error': 'Failed to download or process image from URL'}), 400
    
    else:
        return jsonify({'error': 'Please provide either an image file or URL'}), 400
    
    # Calculate similarity with all products
    similarities = []
    for idx, product_feature in enumerate(product_features):
        sim_score = cosine_similarity(query_features, product_feature)
        similarities.append((idx, sim_score))
    
    # Sort by similarity (highest first) and get top 10
    similarities.sort(key=lambda x: x[1], reverse=True)
    top_matches = similarities[:10]
    
    # Build response
    results = []
    for idx, similarity in top_matches:
        product_row = product_data.iloc[idx]
        
        results.append({
            'product_id': int(product_row['product_id']),
            'image_path': product_row['img_path'],
            'similarity': float(similarity * 100),  # Convert to percentage
            'seller_img_id': int(product_row['seller_img_id'])
        })
    
    return jsonify({
        'success': True,
        'results': results,
        'total_matches': len(results)
    })

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Return some basic stats about the product database"""
    if product_data is None:
        return jsonify({'error': 'Database not loaded'}), 500
    
    return jsonify({
        'total_products': len(product_data),
        'features_loaded': product_features is not None
    })

if __name__ == '__main__':
    # Load database when server starts
    load_product_database()
    
    # Run the server
    print("\n=== Visual Product Matcher Backend ===")
    print("Server starting on http://localhost:5000")
    app.run(debug=True, port=5000)
