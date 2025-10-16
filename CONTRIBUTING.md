# Contributing to Visual Product Matcher

Thank you for your interest in contributing to Visual Product Matcher! This guide will help you get started.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- **Clear title** describing the problem
- **Steps to reproduce** the bug
- **Expected behavior** vs actual behavior
- **Screenshots** if applicable
- **Environment details** (OS, Python version, Node version)

Example:
```
Title: Search fails with large images

Steps:
1. Upload a 20MB image
2. Click "Find Similar Products"

Expected: Should process or show size warning
Actual: Server crashes with memory error

Environment: Windows 11, Python 3.9, 8GB RAM
```

### Suggesting Enhancements

We welcome feature suggestions! Please:
- Check if the feature is already requested
- Explain the use case
- Provide examples if possible

### Pull Requests

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Test thoroughly**
5. **Commit with clear messages**
   ```bash
   git commit -m "Add: feature description"
   ```
6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Create a Pull Request**

## Development Setup

### Prerequisites
- Python 3.8+
- Node.js 16+
- Git

### Setup Steps

1. **Clone your fork:**
   ```bash
   git clone https://github.com/your-username/visual-product-Recognition.git
   cd visual-product-Recognition
   ```

2. **Set up backend:**
   ```bash
   cd backend
   python -m venv venv
   venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   python build_features.py
   ```

3. **Set up frontend:**
   ```bash
   cd frontend
   npm install
   ```

4. **Run tests:**
   ```bash
   # Backend
   cd backend
   python test_api.py

   # Frontend
   cd frontend
   npm run dev
   ```

## Coding Guidelines

### Python (Backend)

**Style:**
- Follow PEP 8
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and small

**Example:**
```python
def extract_image_features(image_path):
    """
    Extract feature vector from an image file.
    
    Args:
        image_path (str): Path to the image file
        
    Returns:
        np.ndarray: 1280-dimensional feature vector
    """
    try:
        img = load_image(image_path)
        features = model.predict(img)
        return features.flatten()
    except Exception as e:
        logger.error(f"Failed to extract features: {e}")
        return None
```

**Import Order:**
1. Standard library
2. Third-party packages
3. Local modules

```python
import os
import sys

import numpy as np
from flask import Flask

from feature_extractor import FeatureExtractor
```

### JavaScript/React (Frontend)

**Style:**
- Use functional components with hooks
- Meaningful component and variable names
- Add comments for complex logic
- Keep components small and focused

**Example:**
```javascript
// Good: Clear purpose, single responsibility
function SimilaritySlider({ value, onChange }) {
  const handleChange = (event, newValue) => {
    onChange(newValue)
  }

  return (
    <Slider
      value={value}
      onChange={handleChange}
      min={0}
      max={100}
      aria-label="Similarity threshold"
    />
  )
}
```

**Component Structure:**
```javascript
// 1. Imports
import { useState } from 'react'
import { Button } from '@mui/material'

// 2. Component definition
function MyComponent({ prop1, prop2 }) {
  // 3. State
  const [value, setValue] = useState(0)
  
  // 4. Handlers
  const handleClick = () => {
    setValue(value + 1)
  }
  
  // 5. Render
  return (
    <Button onClick={handleClick}>
      Click me: {value}
    </Button>
  )
}

// 6. Export
export default MyComponent
```

## Project Structure

### Adding a New Backend Feature

Example: Add product category support

1. **Update data model** (if needed):
   ```python
   # In feature_extractor.py or new models.py
   class Product:
       def __init__(self, product_id, image_path, category):
           self.product_id = product_id
           self.image_path = image_path
           self.category = category
   ```

2. **Update API endpoint:**
   ```python
   # In app.py
   @app.route('/api/search', methods=['POST'])
   def search_products():
       # ... existing code ...
       
       results.append({
           'product_id': int(product_row['product_id']),
           'image_path': product_row['img_path'],
           'category': product_row.get('category', 'Unknown'),  # New field
           'similarity': float(similarity * 100)
       })
   ```

3. **Update tests:**
   ```python
   # In test_api.py
   def test_category_in_results():
       response = requests.post(f'{BASE_URL}/api/search', ...)
       assert 'category' in response.json()['results'][0]
   ```

### Adding a New Frontend Component

Example: Add a category filter

1. **Create component file:**
   ```javascript
   // src/components/CategoryFilter.jsx
   function CategoryFilter({ categories, selected, onChange }) {
     return (
       <Select value={selected} onChange={(e) => onChange(e.target.value)}>
         {categories.map(cat => (
           <MenuItem key={cat} value={cat}>{cat}</MenuItem>
         ))}
       </Select>
     )
   }
   
   export default CategoryFilter
   ```

2. **Integrate in App:**
   ```javascript
   // src/App.jsx
   import CategoryFilter from './components/CategoryFilter'
   
   function App() {
     const [selectedCategory, setSelectedCategory] = useState('all')
     
     return (
       <CategoryFilter
         categories={['all', 'electronics', 'fashion']}
         selected={selectedCategory}
         onChange={setSelectedCategory}
       />
     )
   }
   ```

3. **Add styling if needed:**
   ```css
   /* src/components/CategoryFilter.css */
   .category-filter {
     margin: 1rem 0;
   }
   ```

## Testing

### Backend Tests

Add tests to `backend/test_api.py`:

```python
def test_new_feature():
    """Test description"""
    print("\nTesting new feature...")
    try:
        response = requests.get(f'{BASE_URL}/api/new-endpoint')
        assert response.status_code == 200
        print("✓ New feature works!")
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False
```

### Frontend Testing

Manual testing checklist:
- [ ] Component renders without errors
- [ ] User interactions work (clicks, typing)
- [ ] API calls succeed
- [ ] Error states display correctly
- [ ] Loading states show appropriately
- [ ] Responsive on mobile/tablet/desktop

### Integration Testing

Test the full flow:
1. Start backend
2. Start frontend
3. Upload an image
4. Verify results display
5. Test filtering
6. Test error cases

## Documentation

When adding features, update:

1. **README.md** - If it affects setup or usage
2. **API.md** - For new endpoints or changed responses
3. **DEVELOPMENT.md** - For technical decisions
4. **Code comments** - For complex logic

### Writing Good Documentation

**Good:**
```python
def calculate_similarity(vec1, vec2):
    """
    Calculate cosine similarity between two feature vectors.
    
    Cosine similarity measures the angle between vectors, making it
    ideal for comparing image features regardless of magnitude.
    
    Args:
        vec1 (np.ndarray): First feature vector
        vec2 (np.ndarray): Second feature vector
    
    Returns:
        float: Similarity score between -1 and 1 (higher = more similar)
    """
```

**Less helpful:**
```python
def calculate_similarity(vec1, vec2):
    # Calculate similarity
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
```

## Commit Messages

Use clear, descriptive commit messages:

**Format:**
```
Type: Brief description

Optional longer description explaining why this change was made.
```

**Types:**
- `Add:` New feature
- `Fix:` Bug fix
- `Update:` Improve existing feature
- `Remove:` Remove feature/code
- `Docs:` Documentation only
- `Style:` Code formatting (no logic change)
- `Refactor:` Code restructuring (no behavior change)
- `Test:` Add or update tests

**Examples:**

Good:
```
Add: Category filter to product results

Users can now filter results by product category to narrow down
matches. This is useful when looking for specific types of products.
```

Less helpful:
```
updated stuff
```

## Code Review Process

When reviewing PRs, check for:
- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] Documentation is updated
- [ ] No unnecessary dependencies added
- [ ] No security vulnerabilities
- [ ] Performance impact is acceptable
- [ ] Changes are well-explained in PR description

## Performance Considerations

When contributing, consider:

### Backend
- Avoid loading large files into memory
- Use caching where appropriate
- Consider async operations for I/O
- Profile code if adding compute-heavy features

### Frontend
- Avoid unnecessary re-renders (use React.memo, useMemo)
- Lazy load images
- Debounce user inputs
- Keep bundle size small

## Security Considerations

- Never commit API keys or secrets
- Validate all user inputs
- Sanitize file uploads
- Use HTTPS in production
- Follow OWASP guidelines

## Getting Help

If you're stuck:
1. Check TROUBLESHOOTING.md
2. Review similar code in the project
3. Ask in the issue tracker
4. Refer to DEVELOPMENT.md for context

## Recognition

All contributors will be recognized in the project. Significant contributions may be highlighted in release notes.

## Code of Conduct

- Be respectful and constructive
- Welcome newcomers
- Focus on the code, not the person
- Give credit where due
- Have fun building together!

---

Thank you for contributing to Visual Product Matcher! 🎉
