
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from risk_check import check_risk


app = FastAPI(
    title="Risk Prediction API",
    version="1.1.0"
)


class RiskRequest(BaseModel):
    score: int


@app.get("/")
def home():
    return {
        "message": "Risk Prediction API is running"
    }


@app.get("/predict")
def predict(score: int):
    try:
        prediction = check_risk(score)

        return {
            "score": score,
            "prediction": prediction
        }

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@app.post("/predict")
def predict_post(request: RiskRequest):
    return predict(request.score)
