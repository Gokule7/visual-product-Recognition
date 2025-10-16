"""
Test script to verify backend functionality
Run this after setting up the backend to make sure everything works
"""

import requests
import os

BASE_URL = 'http://localhost:5000'

def test_health_check():
    """Test the health check endpoint"""
    print("Testing health check endpoint...")
    try:
        response = requests.get(f'{BASE_URL}/')
        print(f"✓ Status: {response.status_code}")
        print(f"✓ Response: {response.text}")
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def test_stats_endpoint():
    """Test the stats endpoint"""
    print("\nTesting stats endpoint...")
    try:
        response = requests.get(f'{BASE_URL}/api/stats')
        data = response.json()
        print(f"✓ Total products: {data['total_products']}")
        print(f"✓ Features loaded: {data['features_loaded']}")
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def test_image_search():
    """Test image search with a sample image"""
    print("\nTesting image search...")
    
    # Try to find a sample query image
    sample_img_path = os.path.join('..', 'development_test_data', 'queries', 'magnetic-powerful-platypus-of-hail.jpeg')
    
    if not os.path.exists(sample_img_path):
        print("✗ Sample image not found, skipping search test")
        return False
    
    try:
        with open(sample_img_path, 'rb') as img_file:
            files = {'file': img_file}
            response = requests.post(f'{BASE_URL}/api/search', files=files)
            
        data = response.json()
        
        if data.get('success'):
            print(f"✓ Search successful!")
            print(f"✓ Found {data['total_matches']} matches")
            if data['results']:
                print(f"✓ Top match: Product #{data['results'][0]['product_id']} ({data['results'][0]['similarity']:.2f}% similarity)")
            return True
        else:
            print(f"✗ Search failed: {data}")
            return False
            
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def test_url_search():
    """Test URL-based search"""
    print("\nTesting URL search...")
    
    # Using a sample image URL (you can replace with any image URL)
    test_url = 'https://images.unsplash.com/photo-1523275335684-37898b6baf30'
    
    try:
        response = requests.post(
            f'{BASE_URL}/api/search',
            json={'url': test_url},
            headers={'Content-Type': 'application/json'}
        )
        
        data = response.json()
        
        if data.get('success'):
            print(f"✓ URL search successful!")
            print(f"✓ Found {data['total_matches']} matches")
            return True
        else:
            print(f"✗ URL search failed: {data}")
            return False
            
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

if __name__ == '__main__':
    print("=== Backend API Tests ===\n")
    print("Make sure the Flask server is running on http://localhost:5000\n")
    
    results = []
    results.append(("Health Check", test_health_check()))
    results.append(("Stats Endpoint", test_stats_endpoint()))
    results.append(("Image Search", test_image_search()))
    results.append(("URL Search", test_url_search()))
    
    print("\n=== Test Summary ===")
    for test_name, passed in results:
        status = "✓ PASSED" if passed else "✗ FAILED"
        print(f"{test_name}: {status}")
    
    total_passed = sum(1 for _, passed in results if passed)
    print(f"\nTotal: {total_passed}/{len(results)} tests passed")
