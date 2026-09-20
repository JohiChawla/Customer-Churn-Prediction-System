from fastapi import FastAPI
from pydantic import BaseModel

from src.predict import predict_churn


app = FastAPI(
    title="Customer Churn Prediction API",
    description=(
        "API for predicting customer churn "
        "using machine learning."
    ),
    version="1.0.0"
)


class Customer(BaseModel):

    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str

    tenure: int

    PhoneService: str
    MultipleLines: str
    InternetService: str

    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str

    StreamingTV: str
    StreamingMovies: str

    Contract: str
    PaperlessBilling: str
    PaymentMethod: str

    MonthlyCharges: float
    TotalCharges: float

    ServiceCount: int
    AverageMonthlySpend: float
    HighMonthlyCharge: int
    TenureGroup: str
    HasTechnicalSupport: int
    UsesElectronicPayment: int


@app.get("/")
def home():

    return {
        "message":
        "Customer Churn Prediction API"
    }


@app.post("/predict")
def predict(customer: Customer):

    return predict_churn(
        customer.model_dump()
    )