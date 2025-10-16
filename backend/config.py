"""
Configuration file for backend settings
Modify these values based on your deployment environment
"""

import os

class Config:
    # Flask settings
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # File upload settings
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    UPLOAD_FOLDER = 'temp_uploads'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
    
    # Model settings
    MODEL_NAME = 'MobileNetV2'
    INPUT_SIZE = (224, 224)
    FEATURE_DIM = 1280
    
    # Database paths
    GALLERY_CSV = os.path.join('..', 'development_test_data', 'gallery.csv')
    FEATURES_CACHE = 'product_features.npy'
    
    # API settings
    RESULTS_LIMIT = 10  # Number of top matches to return
    
    # CORS settings
    CORS_ORIGINS = ['http://localhost:3000', 'http://127.0.0.1:3000']

class ProductionConfig(Config):
    DEBUG = False
    # Add production-specific settings here

class DevelopmentConfig(Config):
    DEBUG = True
    # Add development-specific settings here

# Choose config based on environment
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
