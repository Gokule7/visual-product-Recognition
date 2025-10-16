"""
Utility functions for the backend
"""

import os
from PIL import Image
import numpy as np

def validate_image(file_path):
    """
    Validate if a file is a valid image
    Returns (is_valid, error_message)
    """
    try:
        img = Image.open(file_path)
        img.verify()
        return True, None
    except Exception as e:
        return False, str(e)

def ensure_directory(dir_path):
    """Create directory if it doesn't exist"""
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print(f"Created directory: {dir_path}")

def format_file_size(size_bytes):
    """Convert bytes to human-readable format"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"

def normalize_features(features):
    """Normalize feature vector to unit length"""
    norm = np.linalg.norm(features)
    if norm == 0:
        return features
    return features / norm
