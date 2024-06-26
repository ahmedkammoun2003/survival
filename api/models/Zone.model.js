const mongoose = require('mongoose');
const zoneSchema = new mongoose.Schema({
    type: { type: String, required: true }, 
    coordinates: { type: [[Number]], required: true }, 
  });
  
const Zone = mongoose.model("Zone", zoneSchema);
module.exports = Zone;