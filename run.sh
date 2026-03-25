#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Start Flask API Server
export FLASK_APP=app.py
flask run