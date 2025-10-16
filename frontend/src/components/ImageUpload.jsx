import { useState, useRef } from 'react'
import { 
  Paper, 
  Button, 
  TextField, 
  Box, 
  Typography,
  CircularProgress,
  Tab,
  Tabs
} from '@mui/material'
import { CloudUpload, Link as LinkIcon } from '@mui/icons-material'
import axios from 'axios'

// Get API URL from environment variable or fallback to localhost
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000'

function ImageUpload({ onSearchComplete, onSearchError, setIsLoading }) {
  const [selectedFile, setSelectedFile] = useState(null)
  const [imageUrl, setImageUrl] = useState('')
  const [previewUrl, setPreviewUrl] = useState(null)
  const [loading, setLoading] = useState(false)
  const [activeTab, setActiveTab] = useState(0)
  const fileInputRef = useRef(null)

  const handleTabChange = (event, newValue) => {
    setActiveTab(newValue)
    // Clear the other input when switching tabs
    if (newValue === 0) {
      setImageUrl('')
    } else {
      setSelectedFile(null)
      setPreviewUrl(null)
    }
  }

  const handleFileSelect = (event) => {
    const file = event.target.files[0]
    if (file) {
      // Check if it's an image
      if (!file.type.startsWith('image/')) {
        onSearchError('Please select a valid image file')
        return
      }

      setSelectedFile(file)
      
      // Create preview
      const reader = new FileReader()
      reader.onloadend = () => {
        setPreviewUrl(reader.result)
      }
      reader.readAsDataURL(file)
    }
  }

  const handleSearch = async () => {
    if (activeTab === 0 && !selectedFile) {
      onSearchError('Please select an image first')
      return
    }
    
    if (activeTab === 1 && !imageUrl.trim()) {
      onSearchError('Please enter an image URL')
      return
    }

    setLoading(true)
    setIsLoading(true)

    try {
      let response

      if (activeTab === 0) {
        // Upload file
        const formData = new FormData()
        formData.append('file', selectedFile)
        
        response = await axios.post(`${API_URL}/api/search`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
      } else {
        // Use URL
        response = await axios.post(`${API_URL}/api/search`, {
          url: imageUrl
        }, {
          headers: {
            'Content-Type': 'application/json'
          }
        })
        
        // Set preview for URL
        setPreviewUrl(imageUrl)
      }

      if (response.data.success) {
        // Pass both results and the preview image URL to parent
        onSearchComplete(response.data.results, previewUrl)
      } else {
        onSearchError('Search failed. Please try again.')
      }

    } catch (err) {
      console.error('Search error:', err)
      
      if (err.response?.data?.error) {
        onSearchError(err.response.data.error)
      } else if (err.message.includes('Network Error')) {
        onSearchError('Cannot connect to server. Make sure the backend is running.')
      } else {
        onSearchError('An error occurred while searching. Please try again.')
      }
    } finally {
      setLoading(false)
      setIsLoading(false)
    }
  }

  return (
    <Paper elevation={3} sx={{ p: 3, mb: 4 }}>
      <Typography variant="h5" gutterBottom sx={{ mb: 2 }}>
        Upload Image or Enter URL
      </Typography>

      <Tabs value={activeTab} onChange={handleTabChange} sx={{ mb: 3 }}>
        <Tab label="Upload Image" icon={<CloudUpload />} iconPosition="start" />
        <Tab label="Image URL" icon={<LinkIcon />} iconPosition="start" />
      </Tabs>

      {/* Tab 0: File Upload */}
      {activeTab === 0 && (
        <Box>
          <input
            type="file"
            ref={fileInputRef}
            onChange={handleFileSelect}
            accept="image/*"
            style={{ display: 'none' }}
          />
          
          <Button
            variant="outlined"
            startIcon={<CloudUpload />}
            onClick={() => fileInputRef.current.click()}
            sx={{ mb: 2 }}
            fullWidth
          >
            Choose Image
          </Button>

          {selectedFile && (
            <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
              Selected: {selectedFile.name}
            </Typography>
          )}
        </Box>
      )}

      {/* Tab 1: URL Input */}
      {activeTab === 1 && (
        <TextField
          fullWidth
          label="Image URL"
          variant="outlined"
          value={imageUrl}
          onChange={(e) => setImageUrl(e.target.value)}
          placeholder="https://example.com/image.jpg"
          sx={{ mb: 2 }}
        />
      )}

      {/* Preview */}
      {previewUrl && (
        <Box 
          sx={{ 
            mb: 2, 
            textAlign: 'center',
            border: '2px dashed #ddd',
            borderRadius: 2,
            p: 2
          }}
        >
          <Typography variant="subtitle2" gutterBottom>
            Preview:
          </Typography>
          <img 
            src={previewUrl} 
            alt="Preview" 
            style={{ 
              maxWidth: '100%', 
              maxHeight: '300px',
              borderRadius: '8px'
            }} 
          />
        </Box>
      )}

      {/* Search Button */}
      <Button
        variant="contained"
        onClick={handleSearch}
        disabled={loading || (activeTab === 0 ? !selectedFile : !imageUrl.trim())}
        fullWidth
        size="large"
        sx={{
          background: 'linear-gradient(45deg, #667eea, #764ba2)',
          '&:hover': {
            background: 'linear-gradient(45deg, #5568d3, #6a3f8f)'
          }
        }}
      >
        {loading ? (
          <>
            <CircularProgress size={24} sx={{ mr: 1, color: 'white' }} />
            Searching...
          </>
        ) : (
          'Find Similar Products'
        )}
      </Button>
    </Paper>
  )
}

export default ImageUpload
