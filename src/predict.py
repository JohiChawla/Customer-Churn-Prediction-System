from pathlib import Path
import joblib
import pandas as pd


# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Model path
MODEL_PATH = BASE_DIR / "models" / "churn_model.joblib"

print("Loading model from:", MODEL_PATH)

model = joblib.load(MODEL_PATH)


def predict_churn(customer_data: dict):

    df = pd.DataFrame([customer_data])

    probability = model.predict_proba(df)[0, 1]

    prediction = int(probability >= 0.5)

    if probability >= 0.70:
        risk = "High"
    elif probability >= 0.40:
        risk = "Medium"
    else:
        risk = "Low"

    return {
        "churn_prediction": (
            "Yes" if prediction == 1 else "No"
        ),
        "churn_probability": round(
            float(probability),
            4
        ),
        "risk_level": risk
    }