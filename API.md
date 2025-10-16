# API Documentation

## Visual Product Matcher REST API

Base URL: `http://localhost:5000` (development)

---

## Endpoints

### 1. Health Check

Check if the server is running.

**Endpoint:** `GET /`

**Response:**
```
Visual Product Matcher Backend Running
```

**Example:**
```bash
curl http://localhost:5000/
```

---

### 2. Get Database Statistics

Retrieve information about the product database.

**Endpoint:** `GET /api/stats`

**Response:**
```json
{
  "total_products": 1069,
  "features_loaded": true
}
```

**Fields:**
- `total_products` (int): Number of products in the gallery
- `features_loaded` (bool): Whether features are loaded in memory

**Example:**
```bash
curl http://localhost:5000/api/stats
```

---

### 3. Search Similar Products

Find visually similar products based on an uploaded image or URL.

**Endpoint:** `POST /api/search`

**Content-Type:** `multipart/form-data` OR `application/json`

#### Option A: File Upload

**Request (multipart/form-data):**
```
file: <image file>
```

**Example:**
```bash
curl -X POST http://localhost:5000/api/search \
  -F "file=@/path/to/image.jpg"
```

#### Option B: Image URL

**Request (application/json):**
```json
{
  "url": "https://example.com/image.jpg"
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/api/search \
  -H "Content-Type: application/json" \
  -d '{"url":"https://example.com/image.jpg"}'
```

**Success Response (200 OK):**
```json
{
  "success": true,
  "results": [
    {
      "product_id": 5019,
      "image_path": "gallery/ambitious-tough-teal-from-asgard.jpg",
      "similarity": 95.42,
      "seller_img_id": 0
    },
    {
      "product_id": 3550,
      "image_path": "gallery/fine-shrewd-oarfish-of-genius.jpg",
      "similarity": 89.31,
      "seller_img_id": 1
    }
  ],
  "total_matches": 10
}
```

**Fields:**
- `success` (bool): Whether the search was successful
- `results` (array): Array of matching products
  - `product_id` (int): Unique product identifier
  - `image_path` (string): Relative path to product image
  - `similarity` (float): Similarity score (0-100%)
  - `seller_img_id` (int): Gallery image ID
- `total_matches` (int): Number of results returned

**Error Response (400 Bad Request):**
```json
{
  "error": "Please provide either an image file or URL"
}
```

**Error Response (500 Internal Server Error):**
```json
{
  "error": "Product database not loaded"
}
```

**Possible Errors:**
- `No file selected` - File upload was empty
- `Invalid file type. Please upload an image` - File is not an image
- `Failed to process image` - Image couldn't be processed
- `URL cannot be empty` - URL field is empty
- `Failed to download or process image from URL` - URL invalid or unreachable
- `Please provide either an image file or URL` - No input provided
- `Product database not loaded` - Server not initialized

---

## Data Models

### Product Result
```typescript
{
  product_id: number,        // Unique product identifier
  image_path: string,        // Path to product image
  similarity: number,        // Similarity score (0-100)
  seller_img_id: number     // Gallery image identifier
}
```

### Search Response
```typescript
{
  success: boolean,
  results: ProductResult[],
  total_matches: number
}
```

### Error Response
```typescript
{
  error: string              // Human-readable error message
}
```

---

## Rate Limiting

Currently no rate limiting is implemented. For production, consider:
- 100 requests per minute per IP
- 1000 requests per day per user

---

## Image Requirements

**Supported Formats:**
- JPEG (.jpg, .jpeg)
- PNG (.png)
- GIF (.gif)
- WebP (.webp)

**Size Limits:**
- Maximum file size: 16 MB
- Recommended: Under 5 MB for faster processing

**Image Requirements:**
- Minimum resolution: 224×224 pixels
- Recommended: High-quality product photos with clear visibility

---

## Performance

**Typical Response Times:**
- Health check: <10ms
- Stats endpoint: <10ms
- Search (file upload): 200-500ms
- Search (URL): 300-800ms (depends on download time)

**First Request:**
The first search request may take longer as the model loads into memory.

---

## CORS Configuration

The API allows requests from:
- `http://localhost:3000`
- `http://127.0.0.1:3000`

For production, update CORS settings in `app.py`.

---

## Example Integration

### JavaScript (Axios)

```javascript
import axios from 'axios';

// Upload file
const searchByFile = async (file) => {
  const formData = new FormData();
  formData.append('file', file);
  
  const response = await axios.post('http://localhost:5000/api/search', formData, {
    headers: { 'Content-Type': 'multipart/form-data' }
  });
  
  return response.data;
};

// Use URL
const searchByUrl = async (imageUrl) => {
  const response = await axios.post('http://localhost:5000/api/search', 
    { url: imageUrl },
    { headers: { 'Content-Type': 'application/json' } }
  );
  
  return response.data;
};
```

### Python (Requests)

```python
import requests

# Upload file
def search_by_file(image_path):
    with open(image_path, 'rb') as f:
        files = {'file': f}
        response = requests.post('http://localhost:5000/api/search', files=files)
    return response.json()

# Use URL
def search_by_url(image_url):
    data = {'url': image_url}
    response = requests.post('http://localhost:5000/api/search', json=data)
    return response.json()
```

---

## Versioning

Current API Version: **v1.0**

The API does not currently use versioned endpoints. Future versions may use:
- `/api/v2/search`
- Header-based versioning: `X-API-Version: 2`

---

## Authentication

Currently no authentication is required. For production, consider implementing:
- API key authentication
- JWT tokens
- OAuth 2.0

---

## Troubleshooting

**Problem:** 500 Internal Server Error
- **Solution:** Check if backend is fully initialized. Wait for "Server starting" message.

**Problem:** CORS errors in browser
- **Solution:** Verify frontend URL is in CORS whitelist.

**Problem:** Slow response times
- **Solution:** Ensure `product_features.npy` exists (run `build_features.py`).

**Problem:** Out of memory errors
- **Solution:** Increase server RAM or reduce model size.

---

## Support

For issues or questions:
- Check the main README.md
- Review DEVELOPMENT.md for technical details
- Test with `backend/test_api.py`

---

**Last Updated:** October 2025
**API Version:** 1.0
