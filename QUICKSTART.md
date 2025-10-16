# Quick Start Guide

## Running the Application

### Step 1: Start the Backend

```powershell
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python build_features.py
python app.py
```

Wait for the message: "Server starting on http://localhost:5000"

### Step 2: Start the Frontend

Open a new terminal:

```powershell
cd frontend
npm install
npm run dev
```

Visit http://localhost:3000 in your browser.

### Step 3: Test the Application

1. Click "Choose Image" or switch to "Image URL" tab
2. Upload a product image or paste an image URL
3. Click "Find Similar Products"
4. Adjust the similarity slider to filter results

## Troubleshooting

**Backend Issues:**
- If TensorFlow installation fails, try: `pip install tensorflow-cpu` (smaller, CPU-only version)
- If port 5000 is busy, change the port in `app.py` and update frontend axios calls

**Frontend Issues:**
- If npm install fails, try: `npm install --legacy-peer-deps`
- Clear browser cache if you see old UI

**Image Loading Issues:**
- Make sure the `development_test_data` folder is in the project root
- Check that image paths in gallery.csv are correct

## Testing with Sample Images

You can use images from the `development_test_data/queries/` folder to test the application. These are real product query images from the dataset.

## Performance Tips

- First run will be slow (building features)
- Subsequent runs are fast (cached features)
- Consider using GPU for faster processing: Install `tensorflow-gpu` instead of `tensorflow`

## Need Help?

Check the main README.md for detailed documentation.
