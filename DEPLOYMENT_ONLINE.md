# 🚀 Deployment Guide

This guide will walk you through deploying the Visual Product Matcher application online using **Render** (backend) and **Netlify** (frontend).

---

## 📋 Prerequisites

- GitHub account
- Render account (free tier available at [render.com](https://render.com))
- Netlify account (free tier available at [netlify.com](https://netlify.com))
- Your code pushed to GitHub repository

---

## 🔧 Part 1: Deploy Backend to Render

### Step 1: Create a New Web Service on Render

1. Go to [dashboard.render.com](https://dashboard.render.com)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub account if not already connected
4. Select your repository: `visual-product-Recognition`

### Step 2: Configure the Web Service

Fill in the following settings:

- **Name**: `visual-product-matcher-backend` (or your preferred name)
- **Region**: Choose closest to your users (e.g., Oregon, Frankfurt)
- **Branch**: `master`
- **Root Directory**: `backend`
- **Runtime**: `Python 3`
- **Build Command**:
  ```bash
  pip install -r requirements.txt && python build_features.py
  ```
- **Start Command**:
  ```bash
  gunicorn app:app
  ```

### Step 3: Environment Variables (Optional)

Add these if needed:
- `PYTHON_VERSION`: `3.11.0`

### Step 4: Deploy

1. Click **"Create Web Service"**
2. Wait 5-10 minutes for:
   - Dependencies installation
   - Feature cache building (this might take longer on first deploy)
   - Service startup
3. Once deployed, you'll get a URL like: `https://visual-product-matcher-backend.onrender.com`

### Step 5: Test Your Backend

Visit: `https://your-app-name.onrender.com/`

You should see:
```json
{
  "message": "Visual Product Recognition API",
  "version": "1.0.0",
  "endpoints": {
    "/api/search": "POST - Search for similar products",
    "/api/stats": "GET - Get database statistics"
  }
}
```

⚠️ **Important Notes:**
- Free tier sleeps after 15 min of inactivity (first request may be slow)
- Build might take 10-15 minutes due to feature extraction
- Monitor logs for any errors

---

## 🎨 Part 2: Deploy Frontend to Netlify

### Step 1: Prepare Frontend

First, create a production environment file locally:

1. In the `frontend` folder, create `.env.production`:
   ```env
   VITE_API_URL=https://your-app-name.onrender.com
   ```
   Replace `your-app-name` with your actual Render app name!

### Step 2: Deploy to Netlify

#### Option A: Using Netlify CLI (Recommended)

1. Install Netlify CLI:
   ```bash
   npm install -g netlify-cli
   ```

2. Navigate to frontend folder:
   ```bash
   cd frontend
   ```

3. Login to Netlify:
   ```bash
   netlify login
   ```

4. Deploy:
   ```bash
   netlify deploy --prod
   ```

5. Follow the prompts:
   - **Create & configure a new site**: Yes
   - **Team**: Choose your team
   - **Site name**: `visual-product-matcher` (or your preferred name)
   - **Publish directory**: `dist`

#### Option B: Using Netlify Dashboard

1. Go to [app.netlify.com](https://app.netlify.com)
2. Click **"Add new site"** → **"Import an existing project"**
3. Connect to GitHub and select your repository
4. Configure build settings:
   - **Base directory**: `frontend`
   - **Build command**: `npm run build`
   - **Publish directory**: `frontend/dist`

5. **Set Environment Variable**:
   - Go to **Site settings** → **Environment variables**
   - Click **"Add a variable"**
   - Key: `VITE_API_URL`
   - Value: `https://your-render-app.onrender.com`
   - Click **"Save"**

6. Click **"Deploy site"**

### Step 3: Test Your Frontend

1. Visit your Netlify URL: `https://your-site-name.netlify.app`
2. Try uploading an image or using an image URL
3. Verify that product recommendations appear

---

## 🔐 Part 3: Update CORS Configuration (if needed)

If you encounter CORS errors:

1. Go to your Render dashboard
2. Open your web service
3. Go to **"Environment"** tab
4. Add environment variable:
   - Key: `FRONTEND_URL`
   - Value: `https://your-site-name.netlify.app`

5. Update `backend/app.py` CORS configuration to use this variable:
   ```python
   import os
   
   frontend_url = os.getenv('FRONTEND_URL', 'http://localhost:3000')
   
   CORS(app, resources={
       r"/*": {
           "origins": [frontend_url, "http://localhost:3000"],
           "methods": ["GET", "POST", "OPTIONS"],
           "allow_headers": ["Content-Type"]
       }
   })
   ```

6. Commit and push changes - Render will auto-redeploy

---

## ✅ Verification Checklist

- [ ] Backend health check responds at `/`
- [ ] Backend API stats work at `/api/stats`
- [ ] Frontend loads without errors
- [ ] Can upload an image successfully
- [ ] Product recommendations appear
- [ ] Images load correctly in results
- [ ] No CORS errors in browser console

---

## 🐛 Troubleshooting

### Backend Issues

**Problem**: Build timeout or failure
- **Solution**: Feature extraction takes time. Check Render logs. You may need to upgrade to paid tier for longer build times.

**Problem**: 502 Bad Gateway
- **Solution**: Service is starting up. Wait 30-60 seconds and refresh.

**Problem**: Memory issues
- **Solution**: Free tier has 512MB RAM. Consider upgrading or optimizing the model.

### Frontend Issues

**Problem**: "Network Error" when searching
- **Solution**: Check VITE_API_URL is set correctly in Netlify environment variables

**Problem**: Images not loading
- **Solution**: Verify backend URL in ProductList.jsx uses `API_URL` variable

**Problem**: CORS errors
- **Solution**: Update CORS configuration in backend app.py to include your Netlify domain

---

## 📊 Performance Optimization

### Backend
- Consider using Redis for caching results
- Implement request rate limiting
- Use CDN for serving product images

### Frontend
- Enable Netlify's asset optimization
- Implement lazy loading for images
- Add service worker for offline support

---

## 💰 Cost Estimates

### Free Tier Limitations

**Render (Free)**:
- 750 hours/month
- 512MB RAM
- Sleeps after 15 min inactivity
- Shared CPU

**Netlify (Free)**:
- 100GB bandwidth/month
- 300 build minutes/month
- Unlimited sites

### Upgrade Recommendations

For production use:
- **Render Starter ($7/month)**: Always-on, 512MB RAM
- **Render Standard ($25/month)**: 2GB RAM, better performance
- **Netlify Pro ($19/month)**: More bandwidth, build minutes

---

## 🔄 Continuous Deployment

Both platforms support automatic deployment:

1. **Push to GitHub** → Automatically triggers deployment
2. **Render**: Redeploys backend when `backend/` folder changes
3. **Netlify**: Redeploys frontend when `frontend/` folder changes

Configure branch deploys for staging:
- `master` → Production
- `develop` → Staging

---

## 📞 Support

If you encounter issues:
1. Check Render logs: Dashboard → Your Service → Logs
2. Check Netlify logs: Dashboard → Your Site → Deploys → Deploy log
3. Check browser console for frontend errors
4. Verify all environment variables are set correctly

---

## 🎉 Success!

Once deployed, your Visual Product Matcher is live and accessible worldwide! 

**Share your URLs**:
- Frontend: `https://your-site-name.netlify.app`
- Backend API: `https://your-app-name.onrender.com`

Don't forget to update your GitHub README with these live links!
