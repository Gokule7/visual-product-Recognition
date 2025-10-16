import numpy as np
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing import image
from PIL import Image
import io
import requests

class FeatureExtractor:
    """
    Handles image feature extraction using MobileNetV2.
    We're using a pretrained model to convert images into feature vectors
    for similarity comparison.
    """
    
    def __init__(self):
        # Load MobileNetV2 without the top classification layer
        # pooling='avg' gives us a nice compact feature vector
        self.model = MobileNetV2(
            weights='imagenet',
            include_top=False,
            pooling='avg'
        )
        print("Feature extractor loaded successfully")
    
    def extract_from_path(self, img_path):
        """Extract features from a local image file"""
        try:
            img = image.load_img(img_path, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = preprocess_input(img_array)
            
            # Get the feature vector
            features = self.model.predict(img_array, verbose=0)
            return features.flatten()
        except Exception as e:
            print(f"Error extracting features from {img_path}: {str(e)}")
            return None
    
    def extract_from_upload(self, file_storage):
        """Extract features from an uploaded file object"""
        try:
            img = Image.open(file_storage).convert('RGB')
            img = img.resize((224, 224))
            
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = preprocess_input(img_array)
            
            features = self.model.predict(img_array, verbose=0)
            return features.flatten()
        except Exception as e:
            print(f"Error processing uploaded image: {str(e)}")
            return None
    
    def extract_from_url(self, img_url):
        """Download and extract features from an image URL"""
        try:
            response = requests.get(img_url, timeout=10)
            response.raise_for_status()
            
            img = Image.open(io.BytesIO(response.content)).convert('RGB')
            img = img.resize((224, 224))
            
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = preprocess_input(img_array)
            
            features = self.model.predict(img_array, verbose=0)
            return features.flatten()
        except Exception as e:
            print(f"Error downloading/processing image from URL: {str(e)}")
            return None

def cosine_similarity(vec1, vec2):
    """Calculate cosine similarity between two vectors"""
    dot_product = np.dot(vec1, vec2)
    norm_a = np.linalg.norm(vec1)
    norm_b = np.linalg.norm(vec2)
    
    if norm_a == 0 or norm_b == 0:
        return 0.0
    
    return dot_product / (norm_a * norm_b)
