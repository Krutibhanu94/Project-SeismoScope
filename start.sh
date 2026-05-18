#!/bin/bash

echo "Checking for model file..."
if [ ! -f "server/ml/tsunami_prediction_model.pkl" ]; then
    echo "Model file not found! Training model..."
    python server/ml/model.py
    if [ ! -f "server/ml/tsunami_prediction_model.pkl" ]; then
        echo "Failed to train model!"
        exit 1
    fi
else
    echo "Model file found. Skipping training."
fi

echo "Starting FastAPI server..."
uvicorn server.main:app --reload