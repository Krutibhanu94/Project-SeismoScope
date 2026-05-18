# Project-SeismoScope
A full-stack data application for exploring earthquake and tsunami patterns using real seismic data.

## Overview
Project SeismoScope analyzes a dataset of 782 earthquakes to surface patterns between seismic activity and tsunami events. Built as a portfolio project to demonstrate Python data processing, REST API design, machine learning, and interactive data visualization.

## Tech Stack

**Backend**
- Python 3.13
- FastAPI
- Pandas
- scikit-learn (Logistic Regression)
- joblib

**Frontend**
- React + TypeScript
- Vite
- Tailwind CSS
- CSS Modules
- Leaflet.js + react-leaflet

## Running Locally

**Backend**
```bash
# From project root
./start.sh
```

**Frontend**
```bash
cd client
npm run dev
```

## API Endpoints

- `GET /api/health` — server health check
- `GET /api/statistics` — total earthquakes, tsunami count, tsunami rate, average magnitude
- `GET /api/earthquakes` — all earthquake records with location data
- `POST /api/tsunami-predict` — predicts tsunami likelihood from earthquake features

## ML Model

Logistic Regression trained on 782 earthquake records with the following features: magnitude, depth, CDI, MMI, significance score, gap, dmin, nst.

- **Accuracy:** 82.80%
- **Recall:** 93.94%
- **Class weight:** balanced (optimized for catching real tsunamis)

## Dataset
[Global Earthquake-Tsunami Risk Assessment Dataset](https://www.kaggle.com/datasets/ahmeduzaki/global-earthquake-tsunami-risk-assessment-dataset) by Ahmed Uzaki, sourced from Kaggle. Contains 782 earthquake records with the following features: magnitude, depth, CDI, MMI, significance score, latitude, longitude, and tsunami outcome.

## Author
Kruti Bhanu
