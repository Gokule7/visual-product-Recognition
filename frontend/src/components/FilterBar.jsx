import { Paper, Box, Typography, Slider } from '@mui/material'

function FilterBar({ minSimilarity, setMinSimilarity, totalResults, filteredCount }) {
  
  const handleSliderChange = (event, newValue) => {
    setMinSimilarity(newValue)
  }

  return (
    <Paper elevation={2} sx={{ p: 3, mb: 3 }}>
      <Typography variant="h6" gutterBottom>
        Filter Results
      </Typography>
      
      <Box sx={{ px: 2 }}>
        <Typography variant="body2" color="text.secondary" gutterBottom>
          Minimum Similarity: {minSimilarity}%
        </Typography>
        
        <Slider
          value={minSimilarity}
          onChange={handleSliderChange}
          min={0}
          max={100}
          step={5}
          marks={[
            { value: 0, label: '0%' },
            { value: 50, label: '50%' },
            { value: 100, label: '100%' }
          ]}
          valueLabelDisplay="auto"
          sx={{
            color: '#667eea',
            '& .MuiSlider-thumb': {
              '&:hover, &.Mui-focusVisible': {
                boxShadow: '0px 0px 0px 8px rgba(102, 126, 234, 0.16)'
              }
            }
          }}
        />
      </Box>

      <Box sx={{ mt: 2, display: 'flex', justifyContent: 'space-between' }}>
        <Typography variant="body2" color="text.secondary">
          Showing {filteredCount} of {totalResults} results
        </Typography>
        
        {filteredCount < totalResults && (
          <Typography variant="body2" color="warning.main">
            {totalResults - filteredCount} hidden by filter
          </Typography>
        )}
      </Box>
    </Paper>
  )
}

export default FilterBar
