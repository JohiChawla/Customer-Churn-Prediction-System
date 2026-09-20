import streamlit as st
import requests


st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)


st.title(
    "📊 Customer Churn Prediction System"
)

st.write(
    "Predict customer churn probability "
    "using a machine learning model."
)


col1, col2 = st.columns(2)


with col1:

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    senior = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

    tenure = st.number_input(
        "Tenure (months)",
        min_value=0,
        max_value=100,
        value=12
    )

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=50.0
    )


with col2:

    contract = st.selectbox(
        "Contract",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )

    internet = st.selectbox(
        "Internet Service",
        [
            "DSL",
            "Fiber optic",
            "No"
        ]
    )

    payment = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["Yes", "No", "No internet service"]
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=500.0
    )


if st.button("Predict Churn"):

    payload = {
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,

        "tenure": tenure,

        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": internet,

        "OnlineSecurity": "No",
        "OnlineBackup": "No",
        "DeviceProtection": "No",
        "TechSupport": tech_support,

        "StreamingTV": "No",
        "StreamingMovies": "No",

        "Contract": contract,
        "PaperlessBilling": "Yes",
        "PaymentMethod": payment,

        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,

        "ServiceCount": 1,

        "AverageMonthlySpend": (
            total_charges /
            max(tenure, 1)
        ),

        "HighMonthlyCharge": 0,

        "TenureGroup": (
            "New"
            if tenure <= 12
            else "Growing"
        ),

        "HasTechnicalSupport": int(
            tech_support == "Yes"
        ),

        "UsesElectronicPayment": int(
            "Electronic"
            in payment
        )
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=payload
    )

    if response.status_code == 200:

        result = response.json()

        st.success(
            f"Prediction: "
            f"{result['churn_prediction']}"
        )

        st.metric(
            "Churn Probability",
            f"{result['churn_probability']:.2%}"
        )

        st.info(
            f"Risk Level: "
            f"{result['risk_level']}"
        )

    else:

        st.error(
            "Prediction API is unavailable."
        )