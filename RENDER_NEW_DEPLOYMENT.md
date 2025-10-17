# ⚡ RENDER DEPLOYMENT - QUICK START

**Follow these steps to deploy your backend on Render from scratch.**

---

## 🎯 STEP 1: Create Web Service

1. Go to: **https://dashboard.render.com**
2. Click: **"New +"** → **"Web Service"**
3. Connect to GitHub
4. Select: **`Gokule7/visual-product-Recognition`**

---

## 🎯 STEP 2: Configuration Settings

### ⚠️ CRITICAL: Use These EXACT Values

**Name:**
```
visual-product-matcher-backend
```

**Branch:**
```
master
```

**Root Directory:**
```
(LEAVE BLANK - DELETE ANY TEXT HERE!)
```

**Build Command:**
```
cd backend && pip install -r requirements.txt
```

**Start Command:**
```
cd backend && gunicorn app:app
```

**Plan:**
- Select: **Free**

---

## 🎯 STEP 3: Environment Variables

Click **"Advanced"** and add:

**Variable 1:**
```
Key: PYTHON_VERSION
Value: 3.11.0
```

**Variable 2:**
```
Key: PORT
Value: 10000
```

---

## 🎯 STEP 4: Create & Deploy

1. **Review** all settings
2. **Click**: "Create Web Service"
3. **Wait**: ~4-5 minutes

---

## ✅ Verify Deployment

### After deployment completes:

**Test 1 - Health Check (Immediate):**
```
https://your-app-name.onrender.com/
```
**Expected:** "Visual Product Matcher Backend Running"

**Test 2 - Database Status (Wait 1 minute):**
```
https://your-app-name.onrender.com/api/stats
```
**Expected:**
```json
{
  "total_products": 1067,
  "features_loaded": true
}
```

---

## 🎨 STEP 5: Update Frontend (Netlify)

1. Go to: **https://app.netlify.com**
2. Select your site: **visual-product-recognition**
3. Go to: **Site settings** → **Environment variables**
4. Update `VITE_API_URL`:
   ```
   https://YOUR-NEW-RENDER-URL.onrender.com
   ```
5. **Save** and **trigger new deploy**

---

## 🐛 Quick Troubleshooting

**Build Fails?**
- ✅ Check Root Directory is **BLANK**
- ✅ Build command starts with `cd backend &&`

**Deployment Times Out?**
- ✅ Wait 1 minute, database loads in background
- ✅ Check logs for "Product database loaded successfully!"

**"Database not loaded" error?**
- ✅ Wait 1-2 minutes after deployment
- ✅ Database loads in background thread
- ✅ Check Render logs for errors

---

## 📊 Expected Timeline

| Phase | Duration |
|-------|----------|
| Build | 3 minutes |
| Deploy | 1 minute |
| Database Load | 30-60 seconds |
| **Total** | **~5 minutes** |

---

## ⚠️ MOST IMPORTANT SETTINGS

1. **Root Directory = BLANK** (not `backend`)
2. **Build Command = `cd backend && pip install -r requirements.txt`**
3. **Start Command = `cd backend && gunicorn app:app`**

These three settings are CRITICAL for success! ✅

---

## 🎉 Success Checklist

- [ ] Render service created
- [ ] Build completed successfully
- [ ] Service is live (green status)
- [ ] Health check works (`/`)
- [ ] Stats show 1067 products (`/api/stats`)
- [ ] Frontend updated with new backend URL
- [ ] Frontend can upload images
- [ ] Product recommendations appear

---

**That's it! Your app should be fully functional in ~5 minutes!** 🚀

**Still having issues?** Check the Render logs or let me know!
