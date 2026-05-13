from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from server.routers import statistics, earthquakes

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

@app.get("/api/health")
def health_check():
    return {"status": "healthy"}

app.include_router(statistics.router)
app.include_router(earthquakes.router)