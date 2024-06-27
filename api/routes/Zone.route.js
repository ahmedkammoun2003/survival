const express = require("express");
const router = express.Router();
const Zone = require("../models/Zone.model.js");

router.get('/', async (req, res) => {
  try {
    const zones = await Zone.find();
    res.json(zones);
  } catch (error) {
    console.log(error);
  }
});
router.post('/', async (req, res) => {
  console.log('dythdhgfdhg');
  const { type, coordinates } = req.body;

  if (!type || !coordinates) {
    return res.status(400).json({ error: "Type and coordinates are required" });
  }

  const newZone = new Zone({ type, coordinates });

  try {
    const savedZone = await newZone.save();
    res.json(savedZone);
  } catch (error) {
    res.status(500).json({ error: "Failed to add zone" });
  }
});

module.exports = router;
