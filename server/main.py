from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd
from server.routers import statistics, earthquakes, tsunami_predict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# class seismoscope:
#     id: int
#     magnitude: float
#     cdi: float
#     mmi: float
#     sig: float
#     dmin: float
#     gap: float
#     depth: float
#     latitude: float
#     longitude: float
#     Year: int
#     Month: int
#     tsunami_boolean: bool
#     nst: float

df = pd.read_csv('data/earthquake_tsunami_cleaned.csv')
app.state.df = df

#load the trained model
model = joblib.load('server/ml/tsunami_prediction_model.pkl')
app.state.model = model

@app.get("/api/health")
def health_check():
    return {"status": "healthy"}

app.include_router(statistics.router)
app.include_router(earthquakes.router)
app.include_router(tsunami_predict.router)