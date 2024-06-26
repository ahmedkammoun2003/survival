const express = require('express');
const router = express.Router();
const Marker = require('../models/Marker.model.js');

router.get('/', async (req, res) => {
  try {
    const markers = await Marker.find();
    res.json(markers);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

router.post('/', async (req, res) => {
  const marker = new Marker({
    latlng: {
      type: 'Point',
      coordinates: [req.body.latlng.lat, req.body.latlng.lng],
    },
    comments: req.body.comments,
    iconUrl: req.body.iconUrl,
  });

  try {
    const newMarker = await marker.save();
    res.status(201).json(newMarker);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

module.exports = router;
