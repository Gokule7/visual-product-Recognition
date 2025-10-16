# Visual Product Matcher

A full-stack web application that helps users find visually similar products using AI-powered image recognition. Built with React and Flask, this tool leverages deep learning to extract visual features from product images and match them using cosine similarity.

## Overview

Visual Product Matcher uses a pre-trained MobileNetV2 convolutional neural network to analyze product images and find visually similar items from a database. Users can either upload an image from their device or provide a URL, and the system returns the top 10 most similar products ranked by similarity percentage. The application features an intuitive interface with real-time filtering capabilities.

**Key Features:**
- Upload images or use URLs for product matching
- AI-powered visual similarity using MobileNetV2
- Real-time similarity scoring with percentage display
- Interactive filtering by similarity threshold
- Responsive Material UI design
- Fast feature caching for improved performance

## Architecture

The application follows a clean client-server architecture:

```
React Frontend (Port 3000)
    ↓ (Axios HTTP)
Flask Backend (Port 5000)
    ↓ (TensorFlow)
MobileNetV2 Model
    ↓
Product Database (1000+ images)
```

**Frontend:** Built with React and Vite, the UI uses Material UI components for a modern, responsive design. Axios handles API communication with loading states and error handling.

**Backend:** Flask server processes image uploads and URLs, extracts features using TensorFlow/Keras, and computes cosine similarity scores against pre-computed product features stored in NumPy arrays.

**Model:** MobileNetV2 (ImageNet weights) extracts 1280-dimensional feature vectors from images, which are compared using cosine similarity for matching.

## Technologies Used

### Frontend
- React 18
- Vite (build tool)
- Material UI (components & styling)
- Axios (HTTP client)

### Backend
- Flask 3.0
- TensorFlow 2.15
- NumPy & Pandas
- Pillow (image processing)

### Machine Learning
- MobileNetV2 (pre-trained on ImageNet)
- Cosine similarity for feature matching

## Project Structure

```
visual-product-Recognition/
├── backend/
│   ├── app.py                  # Flask server & API routes
│   ├── feature_extractor.py    # CNN feature extraction
│   ├── build_features.py       # Pre-processing script
│   ├── requirements.txt        # Python dependencies
│   └── temp_uploads/           # Temporary upload storage
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ImageUpload.jsx
│   │   │   ├── ProductList.jsx
│   │   │   └── FilterBar.jsx
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
└── development_test_data/
    ├── gallery.csv             # Product database
    ├── gallery/                # Product images
    └── queries/                # Sample query images
```

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Node.js 16 or higher
- npm or yarn

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On Mac/Linux
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Build the feature cache (this takes a few minutes but only needs to be done once):
```bash
python build_features.py
```

5. Start the Flask server:
```bash
python app.py
```

The backend will run on http://localhost:5000

### Frontend Setup

1. Open a new terminal and navigate to the frontend directory:
```bash
cd frontend
```

2. Install npm dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend will run on http://localhost:3000

## Usage

1. Open your browser and go to http://localhost:3000
2. Choose between uploading an image or entering a URL
3. Select/enter your product image
4. Click "Find Similar Products"
5. View results sorted by similarity percentage
6. Use the slider to filter results by minimum similarity

## API Endpoints

### GET /
Health check endpoint
- **Response:** "Visual Product Matcher Backend Running"

### POST /api/search
Search for similar products
- **Content-Type:** multipart/form-data OR application/json
- **Body (file upload):** `file`: Image file
- **Body (URL):** `{"url": "image_url"}`
- **Response:**
```json
{
  "success": true,
  "results": [
    {
      "product_id": 5019,
      "image_path": "gallery/image.jpg",
      "similarity": 95.42,
      "seller_img_id": 0
    }
  ],
  "total_matches": 10
}
```

### GET /api/stats
Get database statistics
- **Response:**
```json
{
  "total_products": 1069,
  "features_loaded": true
}
```

## Deployment

### Backend Deployment (e.g., Heroku, Railway)

1. Create a `Procfile`:
```
web: python app.py
```

2. Set environment variables:
```
FLASK_ENV=production
```

3. Ensure `product_features.npy` is built before deployment or add to your deployment script

### Frontend Deployment (e.g., Vercel, Netlify)

1. Update API endpoint in ImageUpload.jsx to your production backend URL

2. Build the frontend:
```bash
npm run build
```

3. Deploy the `dist` folder

### Docker Deployment (Optional)

Create a `docker-compose.yml` for easy deployment of both services:

```yaml
version: '3'
services:
  backend:
    build: ./backend
    ports:
      - "5000:5000"
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend
```

## Performance Notes

- First-time feature extraction takes ~5-10 minutes for 1000+ images
- Features are cached in `product_features.npy` (reused on subsequent runs)
- Image matching is near-instant once features are cached
- Consider using a GPU for faster feature extraction in production

## Future Enhancements

- Add product metadata (name, category, price) from external data source
- Implement pagination for large result sets
- Add user authentication and search history
- Support for batch image processing
- Mobile app version
- Advanced filtering (by category, price range, etc.)

## 🚀 Online Deployment

This application is ready to be deployed online! We've configured it for:

### Backend: Render
- Automatic builds from GitHub
- Pre-configured with `render.yaml`
- Includes feature cache building
- Free tier available

### Frontend: Netlify
- One-click deployment
- Environment variable support
- Pre-configured with `netlify.toml`
- Automatic builds from GitHub

**📖 Complete Deployment Guide:** See [DEPLOYMENT_ONLINE.md](DEPLOYMENT_ONLINE.md) for step-by-step instructions.

**Quick Start:**
1. Push code to GitHub ✅ (Already done!)
2. Deploy backend to Render (5-10 minutes)
3. Deploy frontend to Netlify (2-3 minutes)
4. Update environment variables
5. Your app is live! 🎉

## Dataset

This project uses the Visual Product Recognition Challenge 2023 dataset from AI Crowd. The gallery contains 1000+ product images with unique identifiers.

## License

MIT License - feel free to use this project for learning or commercial purposes.

## Author

Built as a demonstration of full-stack AI integration for visual search applications.

---

**Note:** Make sure both frontend and backend servers are running simultaneously for the application to work properly.
