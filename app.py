from fastapi import FastAPI, HTTPException

from risk_check import check_risk


app = FastAPI(
    title="Risk Prediction API",
    version="1.0.0"
)


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