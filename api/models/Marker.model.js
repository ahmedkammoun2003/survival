const mongoose = require('mongoose');

const MarkerSchema = new mongoose.Schema({
  comments: {
    type: String,
    required: true
  },
  iconUrl: {
    type: String,
    default: 'http://localhost:5173/node_modules/leaflet/dist/images/marker-icon-2x.png' // Default icon URL if none is provided
  },
  latlng: {
    type: {
      type: String,
      enum: ['Point'],
      required: true
    },
    coordinates: {
      type: [Number], // Array of numbers, [longitude, latitude]
      required: true
    }
  }
});

// Create a 2dsphere index on the latlng field for geospatial queries
MarkerSchema.index({ latlng: '2dsphere' });

const Marker = mongoose.model('Marker', MarkerSchema);

module.exports = Marker;
