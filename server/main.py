from fastapi import FastAPI
import pandas as pd
from server.routers import statistics

app = FastAPI()

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