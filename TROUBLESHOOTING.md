# Troubleshooting Guide

## Common Issues & Solutions

### 🔴 Backend Issues

#### Issue: "Import 'tensorflow' could not be resolved"

**Cause:** TensorFlow not installed or virtual environment not activated

**Solution:**
```bash
cd backend
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

---

#### Issue: "Port 5000 is already in use"

**Cause:** Another application is using port 5000

**Solution 1 - Use different port:**
Edit `backend/app.py`, change the last line:
```python
app.run(debug=True, port=5001)  # Changed from 5000 to 5001
```

Then update frontend API calls in `frontend/src/components/ImageUpload.jsx`:
```javascript
axios.post('http://localhost:5001/api/search', ...)
```

**Solution 2 - Kill existing process:**
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Mac/Linux
lsof -ti:5000 | xargs kill -9
```

---

#### Issue: "ModuleNotFoundError: No module named 'tensorflow'"

**Cause:** Virtual environment not activated or packages not installed

**Solution:**
```bash
cd backend
# Activate venv first
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Mac/Linux

# Then install
pip install -r requirements.txt
```

---

#### Issue: TensorFlow installation takes forever or fails

**Cause:** TensorFlow is large (~500MB)

**Solution - Use CPU-only version:**
Edit `requirements.txt`, replace:
```
tensorflow==2.15.0
```
with:
```
tensorflow-cpu==2.15.0
```

Then run:
```bash
pip install -r requirements.txt
```

---

#### Issue: "FileNotFoundError: gallery.csv not found"

**Cause:** Paths are incorrect relative to backend location

**Solution:**
Make sure your directory structure is:
```
visual-product-Recognition/
  ├── backend/
  │   └── app.py
  └── development_test_data/
      └── gallery.csv
```

Run backend from the `backend/` directory:
```bash
cd backend
python app.py
```

---

#### Issue: "Memory Error" when running build_features.py

**Cause:** Not enough RAM to process all images at once

**Solution:**
Edit `build_features.py`, add batch processing:
```python
# Process in batches of 100
batch_size = 100
for i in range(0, len(gallery_df), batch_size):
    batch = gallery_df[i:i+batch_size]
    # process batch
```

---

### 🔵 Frontend Issues

#### Issue: "npm install" fails

**Cause:** npm cache issues or peer dependency conflicts

**Solution:**
```bash
cd frontend
npm cache clean --force
npm install --legacy-peer-deps
```

---

#### Issue: "Cannot connect to backend" or CORS error

**Cause:** Backend not running or CORS not configured

**Solution 1 - Check backend is running:**
Visit http://localhost:5000 in browser. Should see: "Visual Product Matcher Backend Running"

**Solution 2 - Fix CORS:**
In `backend/app.py`, verify CORS is enabled:
```python
from flask_cors import CORS
app = Flask(__name__)
CORS(app)  # This line must be present
```

**Solution 3 - Check frontend proxy:**
In `frontend/vite.config.js`, verify proxy is set:
```javascript
server: {
  port: 3000,
  proxy: {
    '/api': {
      target: 'http://localhost:5000',
      changeOrigin: true
    }
  }
}
```

---

#### Issue: Images not displaying in results

**Cause:** Incorrect image paths or images not accessible

**Solution:**
Check `ProductList.jsx` image URL:
```javascript
image={`http://localhost:5000/../development_test_data/${product.image_path}`}
```

Better approach - serve images statically. In `backend/app.py`:
```python
from flask import send_from_directory

@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory('../development_test_data', filename)
```

Then in `ProductList.jsx`:
```javascript
image={`http://localhost:5000/images/${product.image_path}`}
```

---

#### Issue: "npm run dev" shows blank page

**Cause:** Build error or missing dependencies

**Solution:**
```bash
# Check console for errors
# Open browser DevTools (F12)

# Try clean install
rm -rf node_modules package-lock.json
npm install
npm run dev
```

---

### 🟡 Data & Model Issues

#### Issue: Very low similarity scores (all below 30%)

**Cause:** Query image is very different from gallery images

**Solution:**
- Test with images from `development_test_data/queries/` (these should match well)
- Check that features were extracted correctly
- Try re-building features: `python build_features.py`

---

#### Issue: Search returns same results for different images

**Cause:** Features not loaded or corrupted

**Solution:**
```bash
cd backend
# Delete cache
rm product_features.npy
# Rebuild
python build_features.py
# Restart server
python app.py
```

---

#### Issue: "build_features.py" fails with image errors

**Cause:** Some gallery images are corrupted or missing

**Solution:**
The script already handles this with zero vectors. Check console output:
```
Warning: Image not found - path/to/image.jpg
```

Verify that `development_test_data/gallery/` contains images.

---

### 🟢 Performance Issues

#### Issue: Search takes too long (>5 seconds)

**Cause:** Features not cached

**Solution:**
```bash
cd backend
python build_features.py  # This creates product_features.npy
```

After this, searches should be <1 second.

---

#### Issue: First search is very slow

**Cause:** Model loading into memory

**Expected behavior:** First search takes 2-3 seconds while TensorFlow loads model. Subsequent searches are fast.

**Solution to pre-warm:**
Add to `app.py` after `load_product_database()`:
```python
# Warm up the model
import numpy as np
dummy_features = extractor.extract_from_path(
    os.path.join('..', 'development_test_data', 'gallery', 'test.jpg')
)
print("Model warmed up and ready")
```

---

### 🟣 Deployment Issues

#### Issue: "gunicorn: command not found"

**Cause:** gunicorn not installed

**Solution:**
```bash
pip install gunicorn
# or
pip install -r requirements.txt
```

---

#### Issue: Heroku deployment fails

**Cause:** Multiple possible issues

**Solutions:**

1. **Check Procfile exists:**
```
web: gunicorn app:app
```

2. **Check Python version in runtime.txt:**
```
python-3.9.18
```

3. **Ensure requirements.txt is complete:**
```bash
pip freeze > requirements.txt
```

4. **Check logs:**
```bash
heroku logs --tail
```

---

#### Issue: Vercel deployment shows "Function too large"

**Cause:** TensorFlow model is too large for serverless

**Solution:**
Don't deploy backend to Vercel. Use:
- Railway (recommended)
- Heroku
- DigitalOcean
- AWS EC2

Vercel is only for the frontend.

---

### 🔧 Development Issues

#### Issue: Changes not reflecting in browser

**Cause:** Browser cache or HMR not working

**Solution:**
```bash
# Hard refresh
Ctrl + Shift + R (Windows/Linux)
Cmd + Shift + R (Mac)

# Or clear cache in DevTools
F12 → Network tab → Disable cache (checkbox)
```

---

#### Issue: ESLint errors in VS Code

**Cause:** Missing ESLint configuration

**Solution:**
Create `frontend/.eslintrc.json`:
```json
{
  "extends": ["react-app"],
  "rules": {
    "no-unused-vars": "warn"
  }
}
```

---

## Quick Diagnostics

### Backend Health Check

Run these commands to verify backend setup:

```bash
cd backend

# 1. Check Python version (should be 3.8+)
python --version

# 2. Check virtual environment
where python  # Windows
which python  # Mac/Linux
# Should point to venv/Scripts/python (Windows) or venv/bin/python (Mac/Linux)

# 3. Check if packages installed
pip list | grep tensorflow
pip list | grep flask

# 4. Check if feature cache exists
ls -l product_features.npy  # Mac/Linux
dir product_features.npy    # Windows

# 5. Test API
python test_api.py
```

### Frontend Health Check

```bash
cd frontend

# 1. Check Node version (should be 16+)
node --version

# 2. Check if dependencies installed
npm list react
npm list axios

# 3. Check for build errors
npm run build

# 4. Test dev server
npm run dev
```

---

## Still Having Issues?

1. **Check the logs:**
   - Backend: Look at terminal where `python app.py` is running
   - Frontend: Check browser console (F12)

2. **Verify setup:**
   - Follow QUICKSTART.md step by step
   - Don't skip any steps

3. **Test with minimal setup:**
   - Backend only: `curl http://localhost:5000/api/stats`
   - Frontend only: Comment out API calls, test UI

4. **Clean slate:**
   ```bash
   # Backend
   cd backend
   rm -rf venv
   rm product_features.npy
   # Start fresh with setup

   # Frontend
   cd frontend
   rm -rf node_modules
   npm install
   ```

---

## Getting Help

If none of these solutions work:

1. Check error messages carefully
2. Search the error on Google/StackOverflow
3. Review the code in the failing component
4. Try the test scripts (`test_api.py`)

---

**Remember:** Most issues are environment-related (paths, ports, dependencies). Double-check your setup matches the project structure.
