import joblib
import pandas as pd


MODEL_PATH = "models/churn_model.joblib"


model = joblib.load(
    MODEL_PATH
)


def predict_churn(customer_data: dict):

    df = pd.DataFrame(
        [customer_data]
    )

    probability = model.predict_proba(
        df
    )[0, 1]

    prediction = int(
        probability >= 0.5
    )

    if probability >= 0.70:
        risk = "High"

    elif probability >= 0.40:
        risk = "Medium"

    else:
        risk = "Low"

    return {
        "churn_prediction": (
            "Yes"
            if prediction == 1
            else "No"
        ),

        "churn_probability": round(
            float(probability),
            4
        ),

        "risk_level": risk
    }