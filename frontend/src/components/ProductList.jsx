import { 
  Grid, 
  Card, 
  CardMedia, 
  CardContent, 
  Typography,
  Chip,
  Box
} from '@mui/material'
import { CheckCircle } from '@mui/icons-material'

function ProductList({ products, isLoading }) {
  if (isLoading) {
    return null
  }

  return (
    <Box sx={{ mt: 3 }}>
      <Typography variant="h5" gutterBottom sx={{ color: 'white', mb: 3 }}>
        Similar Products Found: {products.length}
      </Typography>

      <Grid container spacing={3}>
        {products.map((product, index) => (
          <Grid item xs={12} sm={6} md={4} lg={3} key={product.seller_img_id}>
            <Card 
              sx={{ 
                height: '100%',
                display: 'flex',
                flexDirection: 'column',
                transition: 'transform 0.2s, box-shadow 0.2s',
                '&:hover': {
                  transform: 'translateY(-4px)',
                  boxShadow: 6
                }
              }}
            >
              {/* Product Image */}
              <CardMedia
                component="img"
                height="200"
                image={`http://localhost:5000/images/${product.image_path}`}
                alt={`Product ${product.product_id}`}
                sx={{ 
                  objectFit: 'cover',
                  bgcolor: '#f5f5f5'
                }}
                onError={(e) => {
                  console.error('Failed to load image:', product.image_path)
                  e.target.src = 'https://via.placeholder.com/200x200?text=Image+Not+Found'
                }}
              />

              <CardContent sx={{ flexGrow: 1 }}>
                {/* Rank Badge */}
                {index === 0 && (
                  <Chip
                    icon={<CheckCircle />}
                    label="Best Match"
                    color="success"
                    size="small"
                    sx={{ mb: 1 }}
                  />
                )}

                {/* Product ID */}
                <Typography variant="h6" component="div" gutterBottom sx={{ fontWeight: 600 }}>
                  Product #{product.product_id}
                </Typography>

                {/* Similarity Score - Large Display */}
                <Box sx={{ mb: 2, textAlign: 'center', py: 1.5, bgcolor: product.similarity >= 80 ? '#e8f5e9' : '#e3f2fd', borderRadius: 2 }}>
                  <Typography variant="caption" color="text.secondary" display="block" sx={{ mb: 0.5 }}>
                    Match Confidence
                  </Typography>
                  <Typography variant="h4" color={product.similarity >= 80 ? 'success.main' : 'primary.main'} sx={{ fontWeight: 700 }}>
                    {product.similarity.toFixed(1)}%
                  </Typography>
                </Box>

                {/* Additional Details */}
                <Box sx={{ display: 'flex', flexDirection: 'column', gap: 0.5 }}>
                  <Typography variant="body2" color="text.secondary" sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
                    📦 Gallery ID: <strong>{product.seller_img_id}</strong>
                  </Typography>
                  <Typography variant="body2" color="text.secondary" sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
                    🏷️ Product ID: <strong>{product.product_id}</strong>
                  </Typography>
                  <Typography variant="caption" color="text.secondary" sx={{ mt: 1, fontStyle: 'italic' }}>
                    {product.image_path.split('/')[1]}
                  </Typography>
                </Box>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Box>
  )
}

export default ProductList
