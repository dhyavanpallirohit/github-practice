FROM python:3.13-slim

WORKDIR /app

COPY risk_check.py .

CMD ["python", "risk_check.py"]