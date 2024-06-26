#!/bin/bash

set -e  # exit on error

ROOT_DIR=$(pwd)
CLIENT_DIR=$ROOT_DIR/client
CHATBOT_DIR=$ROOT_DIR/chatbot
API_DIR=$ROOT_DIR/api

echo "Installing Node.js dependencies..."
npm install &

echo "Installing client dependencies..."
(cd $CLIENT_DIR && npm install) &

echo "Installing virtualenv..."
pip install virtualenv &

echo "Creating virtual environment and installing Python dependencies..."
(cd $CHATBOT_DIR && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt && python app.py) &

echo "Starting client development server..."
(cd $CLIENT_DIR && npm run dev) &

echo "Starting API server..."
(cd $API_DIR && node server.js) &