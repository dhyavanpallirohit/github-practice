def check_risk(score):
    if score < 0 or score > 100:
        raise ValueError("Risk score must be between 0 and 100")

    if score >= 75:
        return "High Risk"

    return "Low Risk"
