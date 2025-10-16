import { useState } from 'react'
import { Container, Box, Typography, Paper, Chip } from '@mui/material'
import ImageUpload from './components/ImageUpload'
import ProductList from './components/ProductList'
import FilterBar from './components/FilterBar'
import './App.css'

function App() {
  const [searchResults, setSearchResults] = useState([])
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState(null)
  const [minSimilarity, setMinSimilarity] = useState(0)
  const [queryImage, setQueryImage] = useState(null) // Store uploaded/URL image

  // Handle the search results from ImageUpload component
  const handleSearchComplete = (results, uploadedImage) => {
    setSearchResults(results)
    setQueryImage(uploadedImage) // Save the query image
    setError(null)
  }

  const handleSearchError = (errorMsg) => {
    setError(errorMsg)
    setSearchResults([])
  }

  // Filter results based on similarity threshold
  const filteredResults = searchResults.filter(
    product => product.similarity >= minSimilarity
  )

  return (
    <Box sx={{ 
      minHeight: '100vh',
      background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
      py: 4
    }}>
      <Container maxWidth="lg">
        {/* Header */}
        <Paper 
          elevation={3} 
          sx={{ 
            p: 3, 
            mb: 4, 
            textAlign: 'center',
            background: 'rgba(255, 255, 255, 0.95)'
          }}
        >
          <Typography 
            variant="h3" 
            component="h1" 
            gutterBottom
            sx={{ 
              fontWeight: 700,
              background: 'linear-gradient(45deg, #667eea, #764ba2)',
              WebkitBackgroundClip: 'text',
              WebkitTextFillColor: 'transparent'
            }}
          >
            Visual Product Matcher
          </Typography>
          <Typography variant="subtitle1" color="text.secondary">
            Find visually similar products using AI-powered image recognition
          </Typography>
        </Paper>

        {/* Upload Section */}
        <ImageUpload 
          onSearchComplete={handleSearchComplete}
          onSearchError={handleSearchError}
          setIsLoading={setIsLoading}
        />

        {/* Error Display */}
        {error && (
          <Paper 
            elevation={2} 
            sx={{ 
              p: 2, 
              mb: 3, 
              bgcolor: '#ffebee',
              borderLeft: '4px solid #f44336'
            }}
          >
            <Typography color="error">{error}</Typography>
          </Paper>
        )}

        {/* Query Image Display */}
        {queryImage && searchResults.length > 0 && (
          <Paper elevation={3} sx={{ p: 3, mb: 3, background: 'linear-gradient(to right, #f8f9ff, #fff)' }}>
            <Typography variant="h5" gutterBottom sx={{ mb: 3, fontWeight: 600 }}>
              🔍 Your Query Image
            </Typography>
            <Box sx={{ 
              display: 'flex', 
              alignItems: 'flex-start', 
              gap: 4,
              flexWrap: 'wrap'
            }}>
              {/* Query Image */}
              <Box sx={{ 
                border: '3px solid #667eea',
                borderRadius: '12px',
                padding: '8px',
                background: 'white',
                boxShadow: '0 4px 12px rgba(102, 126, 234, 0.2)'
              }}>
                <img 
                  src={queryImage} 
                  alt="Your uploaded query image" 
                  style={{ 
                    width: '280px', 
                    height: '280px',
                    objectFit: 'contain',
                    borderRadius: '8px',
                    display: 'block'
                  }} 
                />
              </Box>

              {/* Image Details */}
              <Box sx={{ flex: 1, minWidth: '250px' }}>
                <Typography variant="h6" color="primary" gutterBottom sx={{ fontWeight: 600 }}>
                  ✨ Search Results
                </Typography>
                <Box sx={{ mb: 2 }}>
                  <Chip 
                    label={`${searchResults.length} Similar Products Found`} 
                    color="success" 
                    sx={{ fontSize: '1rem', py: 2.5, px: 1, fontWeight: 600 }}
                  />
                </Box>
                
                <Typography variant="body1" color="text.secondary" sx={{ mb: 1 }}>
                  📊 <strong>Analysis Complete:</strong> Used AI to find visually similar products
                </Typography>
                <Typography variant="body2" color="text.secondary" sx={{ mb: 1 }}>
                  🎯 <strong>Matching Method:</strong> MobileNetV2 feature extraction + cosine similarity
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  📈 <strong>Top Match:</strong> {searchResults[0]?.similarity.toFixed(2)}% similarity
                </Typography>
              </Box>
            </Box>
          </Paper>
        )}

        {/* Results Section */}
        {searchResults.length > 0 && (
          <>
            <FilterBar 
              minSimilarity={minSimilarity}
              setMinSimilarity={setMinSimilarity}
              totalResults={searchResults.length}
              filteredCount={filteredResults.length}
            />
            
            <ProductList 
              products={filteredResults} 
              isLoading={isLoading}
            />
          </>
        )}

        {/* No results message */}
        {searchResults.length > 0 && filteredResults.length === 0 && (
          <Paper sx={{ p: 4, textAlign: 'center' }}>
            <Typography variant="h6" color="text.secondary">
              No products match the current filter criteria
            </Typography>
            <Typography variant="body2" color="text.secondary" sx={{ mt: 1 }}>
              Try lowering the similarity threshold
            </Typography>
          </Paper>
        )}
      </Container>
    </Box>
  )
}

export default App
