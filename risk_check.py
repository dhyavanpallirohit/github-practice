def check_risk(score):
    if score < 0 or score > 100:
        raise ValueError("Risk score must be between 0 and 100")

    if score >= 65:
        return "High Risk"

    return "Low Risk"


score = 85
result = check_risk(score)

print(f"Risk score: {score}")
print(f"Prediction: {result}")