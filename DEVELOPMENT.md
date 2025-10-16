# Development Notes

## Project Timeline & Decisions

### Architecture Choices

**Why MobileNetV2?**
- Lightweight and fast compared to ResNet or VGG
- Pre-trained on ImageNet (good general features)
- 1280-dimensional features are compact yet effective
- Works well on CPU (no GPU required for inference)

**Why Flask over FastAPI?**
- Simpler for beginners to understand
- Well-documented for ML projects
- Easy CORS setup
- Good community support

**Why React with Vite?**
- Faster build times compared to Create React App
- Modern dev experience
- Smaller bundle sizes
- Better HMR (Hot Module Replacement)

**Why Material UI?**
- Professional-looking components out of the box
- Responsive by default
- Good documentation
- Consistent design system

### Technical Decisions

**Feature Caching:**
We pre-compute features for all gallery images and save them as a NumPy array. This trades disk space (~50MB) for speed:
- Without cache: ~5-10 minutes to start server
- With cache: ~2-3 seconds to start server

**Cosine Similarity vs Euclidean Distance:**
Cosine similarity works better for image features because:
- It measures angle, not magnitude
- More robust to brightness variations
- Standard practice in visual search

**Top-10 Results:**
We return the top 10 matches as a balance between:
- Showing enough variety
- Not overwhelming the user
- API response size

### Known Limitations

1. **No GPU Acceleration:** The app runs on CPU. For production, consider GPU instances.

2. **No Product Metadata:** The dataset only has image paths and IDs. In a real app, you'd have:
   - Product names
   - Categories
   - Prices
   - Descriptions

3. **Single Model:** We use only MobileNetV2. Could ensemble with:
   - ResNet50
   - EfficientNet
   - Custom-trained model

4. **No User Authentication:** All searches are anonymous. Could add:
   - User accounts
   - Search history
   - Favorites/bookmarks

5. **No Pagination:** All results load at once. Fine for 10 items, but would need pagination for more.

### Performance Benchmarks

On a typical laptop (i5 processor, 8GB RAM):
- Feature extraction per image: ~0.3 seconds
- Search query (with cached features): ~0.1 seconds
- Initial feature cache build: ~5-8 minutes for 1069 images

### File Size Breakdown

- `product_features.npy`: ~5.2 MB (1069 images × 1280 features × 4 bytes)
- Model weights (MobileNetV2): ~14 MB
- Frontend bundle (production): ~500 KB

## Development Workflow

### Adding New Features

**To add a new filter (e.g., by category):**
1. Modify `gallery.csv` to include category column
2. Update `backend/app.py` to pass category in results
3. Update `ProductList.jsx` to display category
4. Add category filter in `FilterBar.jsx`

**To improve accuracy:**
1. Try different models (ResNet50, EfficientNet)
2. Fine-tune on product-specific dataset
3. Use ensemble of multiple models
4. Add data augmentation during feature extraction

**To add batch upload:**
1. Update `ImageUpload.jsx` to accept multiple files
2. Modify backend to process array of images
3. Return results grouped by query image

### Code Quality

**Linting:**
```bash
# Backend
cd backend
flake8 *.py

# Frontend
cd frontend
npm run lint
```

**Testing:**
```bash
# Backend
cd backend
python test_api.py

# Frontend
cd frontend
npm test
```

### Git Workflow

```bash
# Create feature branch
git checkout -b feature/new-feature

# Make changes and commit
git add .
git commit -m "Add descriptive message"

# Push and create PR
git push origin feature/new-feature
```

## Debugging Tips

**Backend not starting:**
- Check if port 5000 is available: `netstat -ano | findstr :5000`
- Try a different port in app.py
- Check virtual environment is activated

**Frontend can't connect to backend:**
- Verify backend is running (visit http://localhost:5000)
- Check CORS settings in app.py
- Clear browser cache

**Low similarity scores:**
- Images might be very different
- Try different query images
- Check if features were extracted correctly

**Memory errors:**
- Reduce batch size in feature extraction
- Use smaller model (MobileNetV2 is already small)
- Increase system RAM or use swap file

## Future Roadmap

### Phase 1 (Current)
- [x] Basic image upload and URL input
- [x] Feature extraction with MobileNetV2
- [x] Similarity search
- [x] Basic filtering

### Phase 2 (Next Steps)
- [ ] Add product metadata (name, price, category)
- [ ] User authentication
- [ ] Search history
- [ ] Favorites/bookmarks

### Phase 3 (Advanced)
- [ ] Fine-tune model on product data
- [ ] Multi-modal search (text + image)
- [ ] Recommendation system
- [ ] Analytics dashboard

### Phase 4 (Scale)
- [ ] Vector database (Pinecone, Milvus)
- [ ] Kubernetes deployment
- [ ] CDN for images
- [ ] API rate limiting

## Resources & References

- **MobileNetV2 Paper:** https://arxiv.org/abs/1801.04381
- **Cosine Similarity:** https://en.wikipedia.org/wiki/Cosine_similarity
- **Flask Documentation:** https://flask.palletsprojects.com/
- **React Documentation:** https://react.dev/
- **Material UI:** https://mui.com/

## Contributing

If others want to contribute:
1. Fork the repository
2. Create a feature branch
3. Make changes with tests
4. Submit a pull request

## License

MIT License - free to use and modify.

---

**Last Updated:** October 2025
**Maintainer:** [Your Name]
**Version:** 1.0.0
