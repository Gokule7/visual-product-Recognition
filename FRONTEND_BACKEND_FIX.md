# 🔧 Frontend-Backend Connection Fix

## ❌ Problem
Frontend shows: **"Cannot connect to server. Make sure the backend is running."**

## ✅ Solution Applied

### Changes Made:

1. **✅ Updated CORS in backend** - Now explicitly allows your Netlify URL
2. **✅ Created production environment file** - Sets correct backend URL
3. **✅ Pushed changes to GitHub** - Both Render and Netlify will auto-redeploy

---

## 📋 What You Need to Do Now:

### Option 1: Verify Netlify Environment Variable (RECOMMENDED)

1. **Go to Netlify Dashboard**: https://app.netlify.com
2. **Select your site**: `visual-product-recognition`
3. **Go to**: Site settings → Environment variables
4. **Check if `VITE_API_URL` exists**:
   - **If YES**: Verify it's set to: `https://visual-product-recognition-1.onrender.com`
   - **If NO**: Add it now:
     ```
     Key: VITE_API_URL
     Value: https://visual-product-recognition-1.onrender.com
     ```
5. **Save and Redeploy**:
   - Go to: Deploys tab
   - Click: "Trigger deploy" → "Deploy site"

### Option 2: Wait for Auto-Deploy

Since you pushed to GitHub:
- **Render** will auto-redeploy (with new CORS) - ~3 minutes
- **Netlify** will auto-redeploy (with new env file) - ~2 minutes

**Total wait time: ~5 minutes**

---

## 🧪 How to Test After Redeployment:

### Step 1: Check Backend CORS
Open browser console and run:
```javascript
fetch('https://visual-product-recognition-1.onrender.com/')
  .then(r => r.text())
  .then(console.log)
```

Should show: "Visual Product Matcher Backend Running"

### Step 2: Check Frontend API URL
On your Netlify site, open browser console and run:
```javascript
console.log(import.meta.env.VITE_API_URL)
```

Should show: `https://visual-product-recognition-1.onrender.com`

### Step 3: Test Upload
- Go to: https://visual-product-recognition.netlify.app/
- Try uploading an image
- Should work! ✅

---

## 🐛 If Still Not Working:

### Check 1: Netlify Environment Variable
```bash
# SSH into your local repo and check
cat frontend/.env.production
```

Should contain:
```
VITE_API_URL=https://visual-product-recognition-1.onrender.com
```

### Check 2: Backend CORS Headers
```bash
curl -I https://visual-product-recognition-1.onrender.com/
```

Should show:
```
access-control-allow-origin: https://visual-product-recognition.netlify.app
```

### Check 3: Browser Network Tab
1. Open your Netlify site
2. Open DevTools → Network tab
3. Try uploading an image
4. Look for the API request
5. Check:
   - **URL**: Should be `https://visual-product-recognition-1.onrender.com/api/search`
   - **Status**: Should be `200 OK` (not `0` or `CORS error`)
   - **Response**: Should have JSON with results

---

## 🎯 Quick Fix Checklist:

- [✅] Backend CORS updated (done automatically via GitHub push)
- [✅] Production env file created (done automatically via GitHub push)
- [ ] **Netlify environment variable set** - YOU NEED TO DO THIS
- [ ] Wait for Render redeploy (~3 min)
- [ ] Wait for Netlify redeploy (~2 min)
- [ ] Test the connection

---

## 📱 Expected Timeline:

**Right now** (16:30):
- ✅ Code pushed to GitHub

**In ~3 minutes** (16:33):
- ✅ Render finishes redeploying with new CORS

**In ~2 minutes** (16:32):
- ✅ Netlify finishes redeploying with new env file

**After both complete** (16:35):
- 🎉 Everything should work!

---

## 💡 Why This Happened:

1. **Missing Environment Variable**: Netlify needs `VITE_API_URL` to know where your backend is
2. **CORS Not Configured**: Backend needs to explicitly allow your Netlify domain
3. **Wildcard Issue**: `https://*.netlify.app` might not work on all servers, explicit URL is better

---

## ✅ Final Check Command:

After 5 minutes, run this to verify everything:

```bash
# Check backend is up
curl https://visual-product-recognition-1.onrender.com/api/stats

# Should return JSON with product count
```

---

## 🆘 If Still Stuck:

1. Check Netlify build logs for errors
2. Check Render logs for CORS errors
3. Verify environment variable is set in Netlify dashboard
4. Try hard refresh (Ctrl+Shift+R) on your Netlify site

---

**Most likely fix: Just add the environment variable in Netlify dashboard and trigger a redeploy!**
