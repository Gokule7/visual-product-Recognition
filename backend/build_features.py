"""
Script to pre-extract features from all gallery images
Run this once to speed up the backend startup time
"""

import numpy as np
import pandas as pd
import os
from feature_extractor import FeatureExtractor

def build_feature_cache():
    print("Starting feature extraction process...")
    
    # Initialize the extractor
    extractor = FeatureExtractor()
    
    # Load gallery data
    gallery_path = os.path.join('..', 'development_test_data', 'gallery.csv')
    gallery_df = pd.read_csv(gallery_path)
    
    print(f"Found {len(gallery_df)} products in gallery")
    
    # Extract features
    features_list = []
    failed_count = 0
    
    for idx, row in gallery_df.iterrows():
        img_path = os.path.join('..', 'development_test_data', row['img_path'])
        
        if os.path.exists(img_path):
            features = extractor.extract_from_path(img_path)
            
            if features is not None:
                features_list.append(features)
            else:
                # Use zero vector for failed extractions
                features_list.append(np.zeros(1280))
                failed_count += 1
        else:
            print(f"Warning: Image not found - {img_path}")
            features_list.append(np.zeros(1280))
            failed_count += 1
        
        # Progress update
        if (idx + 1) % 50 == 0:
            print(f"Progress: {idx + 1}/{len(gallery_df)} images processed")
    
    # Convert to numpy array and save
    features_array = np.array(features_list)
    np.save('product_features.npy', features_array)
    
    print(f"\n✓ Feature extraction complete!")
    print(f"  Total products: {len(features_list)}")
    print(f"  Failed extractions: {failed_count}")
    print(f"  Features saved to: product_features.npy")
    print(f"  File size: {os.path.getsize('product_features.npy') / (1024*1024):.2f} MB")

if __name__ == '__main__':
    build_feature_cache()
