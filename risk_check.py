import os

RISK_THRESHOLD = int(os.getenv("RISK_THRESHOLD", "75"))


def check_risk(score):
    if score < 0 or score > 100:
        raise ValueError(
            "Risk score must be between 0 and 100"
        )

    if score >= RISK_THRESHOLD:
        return "High Risk"

    return "Low Risk"