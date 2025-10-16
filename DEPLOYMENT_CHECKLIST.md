# 🚀 Deployment Checklist

Use this checklist to ensure a smooth deployment of your Visual Product Matcher application.

## ✅ Pre-Deployment Checklist

### Code & Repository
- [x] Code pushed to GitHub
- [x] CORS configured for production
- [x] Environment variables set up
- [x] API endpoints use environment variables
- [x] .gitignore includes sensitive files
- [x] Deployment configuration files added (render.yaml, netlify.toml)

### Accounts Setup
- [ ] Render account created ([render.com](https://render.com))
- [ ] Netlify account created ([netlify.com](https://netlify.com))
- [ ] GitHub connected to both platforms

---

## 🔧 Backend Deployment (Render)

### Step 1: Create Web Service
- [ ] Navigate to Render Dashboard
- [ ] Click "New +" → "Web Service"
- [ ] Connect GitHub repository
- [ ] Select `visual-product-Recognition` repo

### Step 2: Configure Service
- [ ] **Name**: `visual-product-matcher-backend`
- [ ] **Region**: Selected (closest to users)
- [ ] **Branch**: `master`
- [ ] **Root Directory**: `backend`
- [ ] **Runtime**: Python 3
- [ ] **Build Command**: `pip install -r requirements.txt && python build_features.py`
- [ ] **Start Command**: `gunicorn app:app`
- [ ] **Instance Type**: Free (or higher if needed)

### Step 3: Deploy & Verify
- [ ] Click "Create Web Service"
- [ ] Wait for build to complete (~10-15 minutes)
- [ ] Check deployment logs for errors
- [ ] Visit: `https://your-app-name.onrender.com/`
- [ ] Verify API health check returns JSON response
- [ ] Test endpoint: `/api/stats` should return database info
- [ ] Copy your Render URL for frontend configuration

**Your Backend URL**: `_______________________________________`

---

## 🎨 Frontend Deployment (Netlify)

### Step 1: Prepare Environment Variable
- [ ] Open `frontend/.env.production` (or create it)
- [ ] Add line: `VITE_API_URL=https://your-render-app.onrender.com`
- [ ] Replace with your actual Render URL from above
- [ ] Save file (optional - can set in Netlify dashboard)

### Step 2: Deploy via Netlify Dashboard
- [ ] Go to [app.netlify.com](https://app.netlify.com)
- [ ] Click "Add new site" → "Import an existing project"
- [ ] Choose GitHub
- [ ] Select `visual-product-Recognition` repository
- [ ] Configure build settings:
  - [ ] **Base directory**: `frontend`
  - [ ] **Build command**: `npm run build`
  - [ ] **Publish directory**: `frontend/dist`

### Step 3: Set Environment Variables
- [ ] Go to Site Settings → Environment Variables
- [ ] Click "Add a variable"
- [ ] **Key**: `VITE_API_URL`
- [ ] **Value**: Your Render backend URL
- [ ] Click "Save"

### Step 4: Deploy & Verify
- [ ] Click "Deploy site"
- [ ] Wait for build (~2-3 minutes)
- [ ] Visit your Netlify URL
- [ ] Test image upload functionality
- [ ] Test URL-based search
- [ ] Verify product recommendations appear
- [ ] Check browser console for errors

**Your Frontend URL**: `_______________________________________`

---

## 🔐 CORS Configuration (If Needed)

### If You Get CORS Errors:

#### Option 1: Update Render Environment Variables
- [ ] Go to Render Dashboard → Your Service
- [ ] Click "Environment"
- [ ] Add variable:
  - **Key**: `FRONTEND_URL`
  - **Value**: Your Netlify URL
- [ ] Service will auto-redeploy

#### Option 2: Update Code (Already done!)
The code is already configured to accept requests from:
- `http://localhost:3000` (development)
- `https://*.netlify.app` (production)
- `https://*.netlify.com` (production)

---

## ✨ Post-Deployment Testing

### Backend Tests
- [ ] Health check: `GET /`
- [ ] Stats endpoint: `GET /api/stats`
- [ ] Search endpoint: `POST /api/search` (with test image)
- [ ] Image serving: `GET /images/[any-product-image]`
- [ ] Response time is acceptable (<5 seconds for search)

### Frontend Tests
- [ ] Homepage loads without errors
- [ ] Upload button works
- [ ] File selection works
- [ ] URL input works
- [ ] Search button triggers API call
- [ ] Loading indicator appears
- [ ] Results display correctly
- [ ] Product images load
- [ ] Similarity scores show correctly
- [ ] Filtering slider works
- [ ] Responsive design on mobile

### Integration Tests
- [ ] Upload an image from local device
- [ ] Verify backend receives request
- [ ] Check products are returned
- [ ] Verify images load from backend
- [ ] Test with different image formats (JPG, PNG)
- [ ] Test with URL-based search
- [ ] Test with invalid inputs (error handling)

---

## 📊 Performance Check

- [ ] First request time: _______ seconds (Render free tier may sleep)
- [ ] Subsequent requests: _______ seconds
- [ ] Image upload limit: 16MB (configured)
- [ ] Number of results: 10 products
- [ ] Frontend bundle size: Check Netlify build logs

---

## 🐛 Troubleshooting

### Common Issues

#### Backend not responding
- [ ] Check Render logs for errors
- [ ] Verify build completed successfully
- [ ] Wait 30-60 seconds if service was sleeping (free tier)
- [ ] Check that feature cache was built

#### Frontend can't connect to backend
- [ ] Verify `VITE_API_URL` is set in Netlify
- [ ] Check browser network tab for actual URL being called
- [ ] Verify CORS headers in response
- [ ] Check backend is actually running

#### Images not loading
- [ ] Verify `/images/` endpoint works on backend
- [ ] Check ProductList.jsx uses `API_URL` variable
- [ ] Look for 404 errors in browser console

#### CORS errors
- [ ] Check browser console for specific error
- [ ] Verify Netlify URL is allowed in backend CORS config
- [ ] Check that both HTTP and HTTPS protocols are handled

---

## 📱 Share Your Deployment

Once everything is working:

- [ ] Update GitHub README with live links
- [ ] Add deployment badges (optional)
- [ ] Share on social media
- [ ] Add to portfolio
- [ ] Write a blog post about the project

**Live URLs:**
- Frontend: `https://______________________.netlify.app`
- Backend API: `https://______________________.onrender.com`

---

## 🎉 Success!

Congratulations! Your Visual Product Matcher is now live and accessible to anyone on the internet!

### Next Steps (Optional)
- [ ] Set up custom domain
- [ ] Add analytics (Google Analytics)
- [ ] Implement monitoring (Sentry for errors)
- [ ] Set up staging environment
- [ ] Configure CD for automatic deployments
- [ ] Add performance monitoring
- [ ] Consider upgrading to paid tiers for better performance

---

## 📝 Notes

Use this section to track any custom configurations or issues you encountered:

```
Date: _______________
Notes:
__________________________________________________________________
__________________________________________________________________
__________________________________________________________________
__________________________________________________________________
```

---

**Need Help?** Refer to [DEPLOYMENT_ONLINE.md](DEPLOYMENT_ONLINE.md) for detailed instructions.
