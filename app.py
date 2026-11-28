
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from auth import verify_api_key

from risk_check import check_risk


app = FastAPI(
    title="Risk Prediction API",
    version="1.2.0"
)


class RiskRequest(BaseModel):
    score: int


@app.get("/")
def home():
    return {
        "message": "Risk Prediction API is running"
    }


@app.get(
    "/predict",
    dependencies=[Depends(verify_api_key)]
)
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


@app.post(
    "/predict",
    dependencies=[Depends(verify_api_key)]
)
def predict_post(request: RiskRequest):
    return predict(request.score)

@app.get("/version")
def get_version():
    return {
        "application": "risk-api",
        "version": app.version
    }