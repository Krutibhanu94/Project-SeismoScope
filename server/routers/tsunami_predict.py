from fastapi import APIRouter, Request
import pandas as pd
from pydantic import BaseModel

router = APIRouter()

class TsunamiPredictionRequest(BaseModel):
    magnitude: float
    depth: float
    cdi: float
    sig: float
    mmi: float
    gap: float
    nst: float
    dmin: float

class TsunamiPredictionResponse(BaseModel):
    predictedTsunami: bool
    probability: float

@router.post("/api/tsunami-predict", response_model=TsunamiPredictionResponse)
def predict_tsunami(request: Request, data: TsunamiPredictionRequest):
    """
    Predicts the likelihood of a tsunami based on earthquake data using a pre-trained machine learning model.
     Args:
        data (TsunamiPredictionRequest): A Pydantic model containing earthquake features such as magnitude, depth, cdi, sig, mmi, gap, nst, and dmin.
     Returns:
        A dictionary containing the prediction and predicted probability of a tsunami occurring.
    """
    model = request.app.state.model
    
    features = pd.DataFrame([[
        data.magnitude,
        data.depth,
        data.cdi,
        data.sig,
        data.mmi,
        data.gap,
        data.nst,
        data.dmin
    ]], columns = ['magnitude', 'depth', 'cdi', 'sig', 'mmi', 'gap', 'nst', 'dmin'])

    prediction = model.predict(features)[0]  # Get the predicted class (0 or 1)
    probability = model.predict_proba(features)[0][1]  # Get the probability of the positive class (tsunami)

    return TsunamiPredictionResponse(
        predictedTsunami=bool(prediction),
        probability=round(probability * 100, 2)
    )