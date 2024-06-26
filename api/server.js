const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const markersRouter = require('./routes/Marker.route.js');
const zoneRouter = require('./routes/Zone.route.js')
const cors = require('cors');
require('dotenv').config();
console.log(process.env.MONGODB);


const app = express();
const PORT = 5000;
app.use(cors())

mongoose.connect(process.env.MONGODB).then(() => {
  console.log('Connected to MongoDB');
}).catch(err => {
  console.error('MongoDB connection error:', err);
});
app.use(bodyParser.json());

app.use('/api/markers', markersRouter);
app.use('/api/polygons', zoneRouter);

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
