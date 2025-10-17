# Visual Product Recognition System - Project Delivery

## Live Application
**Frontend:** https://visual-product-recognition.netlify.app  
**Backend API:** https://visual-product-recognition.onrender.com

## Source Code
**GitHub Repository:** https://github.com/Gokule7/visual-product-Recognition

Full source code with deployment configurations, documentation, and test data included.

---

## Development Approach

I built this visual search system to help users find similar products just by uploading an image. The core idea was simple - extract visual features from images and match them efficiently.

**Technical Stack:**
- Used MobileNetV2 for feature extraction because it's lightweight yet accurate
- Flask backend handles the heavy lifting - loading 1067 products on startup
- React frontend keeps things clean and responsive

**Key Challenges:**
- Getting the model to load properly on Render's free tier was tricky. Had to implement background threading so the server wouldn't timeout during the 30-second database initialization.
- Path resolution between local dev and production took some debugging. Ended up searching multiple locations to find the data files.
- CORS configuration needed fine-tuning for cross-origin requests between Netlify and Render.

**What Works:**
Upload any product image, and the system returns the top 5 most similar items with confidence scores. The similarity matching uses cosine similarity on the extracted feature vectors - straightforward but effective.

The whole thing runs on free hosting tiers, which is pretty neat for a prototype. Database stays in memory for fast queries once loaded.

---

## Quick Start
1. Visit the live app
2. Upload a product image (or use sample images from the repo)
3. Get instant visual matches with similarity scores

