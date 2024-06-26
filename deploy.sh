#!/bin/bash

set -e  # exit on error

ROOT_DIR=$(pwd)
CLIENT_DIR=$ROOT_DIR/client
CHATBOT_DIR=$ROOT_DIR/chatbot
API_DIR=$ROOT_DIR/api

echo "Installing Node.js dependencies..."
npm install

echo "Installing client dependencies..."
pushd $CLIENT_DIR
npm install
popd

echo "Installing virtualenv..."
pip install virtualenv

echo "Creating virtual environment and installing Python dependencies..."
pushd $CHATBOT_DIR
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
popd

echo "Starting client development server..."
pushd $CLIENT_DIR
npm run dev
popd

echo "Starting API server..."
pushd $API_DIR
node server.js
popd