# 🚨 CRITICAL FIX: Data Folder Not Accessible on Render

## Problem Identified ✅

The `development_test_data` folder is in your git repo (3004 files tracked), but Render can't access it because:

- **Render Root Directory**: `backend/`
- **Data Location**: `../development_test_data/` (parent directory)
- **Result**: Render can't access parent directories from the root directory setting

## Solution: Update Render Configuration

### Option 1: Change Root Directory (RECOMMENDED)

1. Go to Render Dashboard: https://dashboard.render.com
2. Select your service: `visual-product-matcher-backend`
3. Go to **Settings**
4. Find **Root Directory**
5. **Change from** `backend` **to** ` ` (blank/empty)
6. Update **Build Command** to:
   ```
   cd backend && pip install -r requirements.txt
   ```
7. Keep **Start Command** as:
   ```
   cd backend && gunicorn app:app
   ```
8. Click **Save Changes**
9. **Manual Deploy** → Deploy latest commit

### Option 2: Copy Data During Build

Keep Root Directory as `backend`, but update:

**Build Command:**
```bash
cp -r ../development_test_data . && pip install -r requirements.txt
```

This copies the data folder into the backend directory during build.

### Option 3: Symlink (May Not Work on Render)

**Build Command:**
```bash
ln -s ../development_test_data development_test_data && pip install -r requirements.txt
```

## Recommended: Option 1

**Why?** 
- Cleaner setup
- No file copying overhead
- Works with existing code
- Easier to debug

## Steps to Fix Right Now:

1. **Go to**: https://dashboard.render.com/web/srv-ctbj8o08fa8c73e1t1cg (your service)
2. **Click**: Settings
3. **Root Directory**: Leave BLANK or set to `.`
4. **Build Command**: 
   ```
   cd backend && pip install -r requirements.txt
   ```
5. **Start Command**:
   ```
   cd backend && gunicorn app:app
   ```
6. **Save Changes**
7. **Deploy** → Manual Deploy → Deploy latest commit

## Expected Result:

```
Loading product database...
Searching for gallery.csv in 3 possible locations...
  1. Trying: /opt/render/project/src/development_test_data/gallery.csv
  ✅ Found gallery.csv
✅ Loaded 1067 products from CSV
✅ Product database loaded successfully!
```

## Timeline:

- Update settings: 2 minutes
- Redeploy: 3-5 minutes
- **Total**: ~7 minutes

---

**Do this now and your app will work!** 🚀
