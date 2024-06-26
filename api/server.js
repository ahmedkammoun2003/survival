const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const markersRouter = require('./routes/Marker.route.js');
const zoneRouter = require('./routes/Zone.route.js')
const cors = require('cors');
const path=require('path')
require('dotenv').config();
console.log(process.env.MONGODB);


const app = express();
const PORT = 5000;
app.use(cors())
const __dirname = path.resolve();

mongoose.connect(process.env.MONGODB).then(() => {
  console.log('Connected to MongoDB');
}).catch(err => {
  console.error('MongoDB connection error:', err);
});
app.use(bodyParser.json());

app.use('/api/markers', markersRouter);
app.use('/api/polygons', zoneRouter);
app.use(express.static(path.join(__dirname,'/client/dist')));
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname,'/client/dist/index.html'));
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
