# Deployment Guide

## Deploying to Production

### Option 1: Deploy to Railway (Recommended for Backend)

Railway is a modern platform that makes deployment simple.

#### Backend on Railway

1. Install Railway CLI:
```bash
npm install -g @railway/cli
```

2. Login to Railway:
```bash
railway login
```

3. Initialize project:
```bash
cd backend
railway init
```

4. Add environment variables in Railway dashboard:
   - `FLASK_ENV=production`
   - `SECRET_KEY=your-secret-key-here`

5. Deploy:
```bash
railway up
```

6. Note your backend URL (e.g., `https://your-app.railway.app`)

#### Frontend on Vercel

1. Update API endpoint in `frontend/src/components/ImageUpload.jsx`:
```javascript
// Replace http://localhost:5000 with your Railway backend URL
const API_URL = 'https://your-app.railway.app'
```

2. Install Vercel CLI:
```bash
npm install -g vercel
```

3. Deploy:
```bash
cd frontend
vercel
```

4. Follow the prompts and your app will be live!

### Option 2: Deploy to Heroku

#### Backend

1. Create `Procfile` in backend folder:
```
web: gunicorn app:app
```

2. Add gunicorn to requirements.txt:
```bash
echo "gunicorn==21.2.0" >> requirements.txt
```

3. Deploy:
```bash
heroku create your-app-name
git subtree push --prefix backend heroku main
```

#### Frontend

Deploy to Vercel or Netlify as described above.

### Option 3: Docker Deployment

Create `backend/Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

Create `frontend/Dockerfile`:

```dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

RUN npm run build

EXPOSE 3000

CMD ["npm", "run", "preview"]
```

Create `docker-compose.yml` in root:

```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "5000:5000"
    volumes:
      - ./development_test_data:/app/development_test_data
    environment:
      - FLASK_ENV=production
  
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend
```

Run with:
```bash
docker-compose up
```

## Important Pre-Deployment Steps

### 1. Build Feature Cache

Before deploying, make sure to run:
```bash
cd backend
python build_features.py
```

This creates `product_features.npy` which should be included in your deployment.

### 2. Update CORS Settings

In `backend/app.py`, update CORS origins for production:

```python
CORS(app, origins=['https://your-frontend-domain.com'])
```

### 3. Environment Variables

Set these in your deployment platform:
- `FLASK_ENV=production`
- `SECRET_KEY=<random-secret-key>`

### 4. Update API Endpoint

In `frontend/src/components/ImageUpload.jsx`, replace all instances of `http://localhost:5000` with your production backend URL.

## Performance Optimization

### Backend
- Use `gunicorn` with multiple workers for better performance
- Consider using Redis for caching if scaling
- Use GPU instances for faster feature extraction

### Frontend
- Run `npm run build` to create optimized production build
- Enable CDN for static assets
- Use image lazy loading

## Monitoring

Add basic monitoring to track usage:

```python
# In app.py
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/api/search', methods=['POST'])
def search_products():
    logger.info(f"Search request from {request.remote_addr}")
    # ... rest of the code
```

## Troubleshooting Deployment

**Issue: TensorFlow too large**
- Solution: Use `tensorflow-cpu` instead of `tensorflow`
- Or use Docker with a smaller base image

**Issue: Feature extraction timeout**
- Solution: Build features locally and include .npy file
- Set longer timeout on your hosting platform

**Issue: CORS errors**
- Solution: Check CORS settings in app.py
- Ensure frontend URL is whitelisted

**Issue: Memory issues**
- Solution: Increase RAM allocation in hosting platform
- Consider using serverless functions for image processing

## Cost Optimization

- Railway: Free tier available, pay for usage
- Vercel: Free for personal projects
- Heroku: Free tier discontinued, paid plans start at $7/month
- Alternative: Use AWS/GCP free tier

## Security Checklist

- [ ] Change SECRET_KEY in production
- [ ] Limit file upload sizes
- [ ] Validate image files properly
- [ ] Use HTTPS for all connections
- [ ] Set proper CORS policies
- [ ] Add rate limiting for API endpoints
- [ ] Keep dependencies updated

## Backup Strategy

- Keep `product_features.npy` backed up
- Version control all code
- Regular database backups if adding user data later

---

For questions or issues, refer to the main README.md or create an issue on GitHub.
