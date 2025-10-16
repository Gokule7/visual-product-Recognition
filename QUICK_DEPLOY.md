# 🚀 Quick Deployment Reference Card

**Print this or keep it handy during deployment!**

---

## ⚡ Quick Links

| Platform | URL | Purpose |
|----------|-----|---------|
| Render Dashboard | https://dashboard.render.com | Deploy backend |
| Netlify Dashboard | https://app.netlify.com | Deploy frontend |
| GitHub Repo | https://github.com/Gokule7/visual-product-Recognition | Your code |

---

## 📦 Backend Deployment (Render)

### Configuration
```
Name: visual-product-matcher-backend
Root Directory: backend
Build Command: pip install -r requirements.txt && python build_features.py
Start Command: gunicorn app:app
```

### Time Required
- First deploy: ~15 minutes (builds feature cache)
- Subsequent: ~5 minutes

### Verify Success
- Visit: `https://YOUR-APP.onrender.com/`
- Should return JSON with API info

---

## 🎨 Frontend Deployment (Netlify)

### Configuration
```
Base Directory: frontend
Build Command: npm run build
Publish Directory: frontend/dist
```

### Environment Variable (IMPORTANT!)
```
Key: VITE_API_URL
Value: https://YOUR-RENDER-APP.onrender.com
```

### Time Required
- Build: ~3 minutes

### Verify Success
- Upload image and check results appear

---

## 🔧 Deployment Order

```
1. Deploy Backend First (Render)
   ↓
2. Copy Backend URL
   ↓
3. Deploy Frontend (Netlify)
   ↓
4. Add VITE_API_URL to Netlify
   ↓
5. Test Application
```

---

## ✅ Success Checklist (Minimal)

Backend:
- [ ] Health check returns JSON
- [ ] `/api/stats` shows product count

Frontend:
- [ ] Page loads without errors
- [ ] Can upload image
- [ ] Results display
- [ ] Images load

---

## 🐛 Quick Fixes

**502 Error?**
→ Wait 30 seconds (service waking up)

**Network Error?**
→ Check VITE_API_URL in Netlify settings

**CORS Error?**
→ Already configured, check Netlify URL format

**Images Not Loading?**
→ Verify backend URL doesn't end with `/`

---

## 📱 Your Deployment URLs

Fill these in after deployment:

**Backend**:
```
https://_________________________________.onrender.com
```

**Frontend**:
```
https://_________________________________.netlify.app
```

---

## 📚 Documentation Files

- `DEPLOYMENT_SUMMARY.md` - Overview (start here)
- `DEPLOYMENT_ONLINE.md` - Complete guide
- `DEPLOYMENT_CHECKLIST.md` - Track progress
- This file - Quick reference

---

## 💡 Pro Tips

1. **Deploy backend first** - Frontend needs its URL
2. **Don't skip environment variables** - App won't work without them
3. **Check logs** - Both platforms have excellent logging
4. **First request is slow** - Free tier wakes up from sleep
5. **Both auto-deploy** - Push to GitHub triggers rebuilds

---

**Total Time: ~20 minutes** ⏱️

**Cost: $0** (using free tiers) 💰

**Difficulty: Easy** ⭐⭐☆☆☆

---

*Print this card or save as PDF for easy reference!*
