def check_risk(score):
    if score >= 70:
        return "High Risk"
    return "Low Risk"


score = 85
result = check_risk(score)

print(f"Risk score: {score}")
print(f"Prediction: {result}")