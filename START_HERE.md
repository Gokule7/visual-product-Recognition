# 🎯 Getting Started with Visual Product Matcher

## What is this project?

Visual Product Matcher is a full-stack AI-powered web application that finds visually similar products from a database. Upload any product image or paste a URL, and it returns the top 10 most similar products using deep learning.

**Think of it like:** Google Image Search, but for products in your database.

## Quick Visual Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     USER INTERFACE                           │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  [Upload Image]  OR  [Enter URL]                     │   │
│  │                                                       │   │
│  │  ┌─────────────┐                                    │   │
│  │  │   Preview   │                                    │   │
│  │  │   Image     │                                    │   │
│  │  └─────────────┘                                    │   │
│  │                                                       │   │
│  │  [Find Similar Products Button]                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                          ↓                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Filter: Similarity ≥ [────○────] 50%              │   │
│  └─────────────────────────────────────────────────────┘   │
│                          ↓                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Results:                                            │   │
│  │  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐                  │   │
│  │  │ 95% │ │ 89% │ │ 85% │ │ 78% │   ...             │   │
│  │  │Img 1│ │Img 2│ │Img 3│ │Img 4│                  │   │
│  │  └─────┘ └─────┘ └─────┘ └─────┘                  │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
        React Frontend (localhost:3000)
                     ↕ (HTTP/JSON)
        Flask Backend (localhost:5000)
                     ↕
        MobileNetV2 AI Model
                     ↕
        Product Database (1069 images)
```

## 3-Step Setup

### Step 1: Install Dependencies

**Windows:**
```powershell
.\setup.bat
```

**Mac/Linux:**
```bash
chmod +x setup.sh
./setup.sh
```

### Step 2: Start Backend

```powershell
cd backend
venv\Scripts\activate      # Windows
# source venv/bin/activate  # Mac/Linux
python app.py
```

Wait for: `Server starting on http://localhost:5000`

### Step 3: Start Frontend (New Terminal)

```powershell
cd frontend
npm run dev
```

Visit: http://localhost:3000

## How It Works (Simple Explanation)

1. **You upload an image** of a product (e.g., a watch)

2. **The AI extracts features** from your image
   - Converts image into a 1280-number "fingerprint"
   - Like a barcode, but for visual similarity

3. **Compares with database**
   - Already has "fingerprints" for 1069 products
   - Calculates similarity scores (0-100%)

4. **Shows top matches**
   - Returns 10 most similar products
   - Sorted by similarity percentage

## File Structure (Simplified)

```
visual-product-Recognition/
│
├── 📂 backend/              ← Python + AI brain
│   ├── app.py              ← Web server
│   ├── feature_extractor.py ← AI model
│   └── requirements.txt     ← Python packages
│
├── 📂 frontend/             ← React + UI
│   ├── src/
│   │   ├── components/     ← UI pieces
│   │   └── App.jsx         ← Main app
│   └── package.json        ← Node packages
│
├── 📂 development_test_data/ ← Product images
│   ├── gallery.csv         ← Product list
│   └── gallery/            ← 1069 product images
│
└── 📄 README.md            ← You are here!
```

## What Each File Does

### Backend Files

| File | Purpose | You Need It? |
|------|---------|--------------|
| `app.py` | Main server (receives uploads, returns results) | ✅ Yes |
| `feature_extractor.py` | AI model that analyzes images | ✅ Yes |
| `build_features.py` | Pre-processes all products (run once) | ✅ Yes (run once) |
| `test_api.py` | Tests if backend works | 🔧 Testing only |
| `config.py` | Settings | 📝 Optional |
| `utils.py` | Helper functions | 📝 Optional |

### Frontend Files

| File | Purpose | You Need It? |
|------|---------|--------------|
| `App.jsx` | Main application | ✅ Yes |
| `ImageUpload.jsx` | Upload/URL input interface | ✅ Yes |
| `ProductList.jsx` | Shows search results | ✅ Yes |
| `FilterBar.jsx` | Similarity slider | ✅ Yes |
| `package.json` | Dependencies list | ✅ Yes |

### Documentation Files

| File | What's In It |
|------|--------------|
| `README.md` | Main guide (setup, usage) |
| `QUICKSTART.md` | Fast setup instructions |
| `API.md` | How to use the API |
| `DEPLOYMENT.md` | How to deploy online |
| `TROUBLESHOOTING.md` | Fix common problems |
| `DEVELOPMENT.md` | Technical deep dive |
| `CONTRIBUTING.md` | How to contribute |
| `PROJECT_SUMMARY.md` | Complete overview |
| `CHECKLIST.md` | What's implemented |

## Common Questions

### Q: Do I need to know AI/ML to use this?
**A:** No! Everything is pre-built. Just run it.

### Q: Do I need a GPU?
**A:** No. It runs on CPU (slower but works fine).

### Q: How long does setup take?
**A:** 
- First time: ~10 minutes (downloads packages, builds features)
- After that: ~10 seconds to start

### Q: Can I use my own images?
**A:** Yes! 
- For searching: Upload any image
- For the database: Replace images in `development_test_data/gallery/`

### Q: How accurate is it?
**A:** Pretty good! Similar products typically score 80-95%. Unrelated products score <50%.

### Q: Is this free to use?
**A:** Yes! MIT License. Use it for anything.

## Technology Stack (What You'll Learn)

**Frontend:**
- React (JavaScript UI framework)
- Material UI (Beautiful components)
- Axios (API communication)
- Vite (Modern build tool)

**Backend:**
- Flask (Python web framework)
- TensorFlow (AI/Machine Learning)
- NumPy (Fast math operations)
- Pandas (Data handling)

**AI:**
- MobileNetV2 (Image recognition model)
- Transfer Learning (Using pre-trained model)
- Cosine Similarity (Comparing vectors)

## Usage Examples

### Example 1: Upload from Computer

1. Click "Choose Image"
2. Select a product photo
3. Click "Find Similar Products"
4. See top 10 matches!

### Example 2: Use Image URL

1. Switch to "Image URL" tab
2. Paste: `https://example.com/product.jpg`
3. Click "Find Similar Products"
4. See results!

### Example 3: Filter Results

1. After getting results
2. Move slider to "80%"
3. Only products with 80%+ similarity show

## Performance Tips

**First Run:**
- Building features: 5-10 minutes (one-time only)
- After that: instant startup

**Search Speed:**
- With cache: ~0.1 seconds
- Without cache: ~5 seconds per search

**Improve Speed:**
- Make sure `product_features.npy` exists
- Use smaller images (<5MB)
- Close other programs

## Next Steps After Setup

1. ✅ **Test with sample images**
   - Use images from `development_test_data/queries/`
   
2. ✅ **Try the filter**
   - Adjust similarity threshold
   
3. ✅ **Test error cases**
   - Upload invalid file
   - Enter broken URL
   
4. ✅ **Read API.md**
   - Learn how to integrate
   
5. ✅ **Customize**
   - Change colors
   - Add features

## Troubleshooting Quick Fixes

**Backend won't start:**
```bash
cd backend
pip install -r requirements.txt
python app.py
```

**Frontend won't start:**
```bash
cd frontend
npm install
npm run dev
```

**Can't connect to backend:**
- Check backend is running (http://localhost:5000)
- Check no firewall blocking

**Search returns no results:**
- Run `python build_features.py` first
- Check images exist in gallery folder

For detailed help: See `TROUBLESHOOTING.md`

## Project Stats

- **Backend:** ~800 lines of Python
- **Frontend:** ~600 lines of React
- **Documentation:** ~15,000 words
- **Total Files:** 25+ files
- **Product Database:** 1,069 images
- **AI Model:** MobileNetV2 (14MB)

## Where to Get Help

1. **Quick problems:** → `TROUBLESHOOTING.md`
2. **Setup issues:** → `QUICKSTART.md`
3. **API questions:** → `API.md`
4. **Development:** → `DEVELOPMENT.md`
5. **Deployment:** → `DEPLOYMENT.md`

## Contributing

Want to improve this project? See `CONTRIBUTING.md`

Ideas for enhancements:
- Add product names/prices
- Support multiple images at once
- Add user accounts
- Improve accuracy with fine-tuning
- Add mobile app

## License

MIT License - Free to use, modify, distribute!

---

## Ready to Start?

1. Run `setup.bat` (Windows) or `setup.sh` (Mac/Linux)
2. Follow the terminal instructions
3. Open http://localhost:3000
4. Upload an image and see the magic! ✨

**Need help?** Check `QUICKSTART.md` for step-by-step guide.

**Want to deploy?** Check `DEPLOYMENT.md` for hosting options.

**Happy matching! 🚀**
