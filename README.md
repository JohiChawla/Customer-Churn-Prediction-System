# 📊 Customer Churn Prediction & Retention System

An end-to-end Machine Learning project that predicts customer churn probability and identifies factors associated with customer churn.

The project covers the complete ML lifecycle:

**Data Analysis → Feature Engineering → Model Training → Evaluation → Explainable AI → REST API → Interactive Dashboard → Docker**

---

## 🚀 Project Overview

Customer churn is a major business problem for subscription-based companies.

The goal of this project is to build a machine learning system that can:

* Predict whether a customer is likely to churn
* Estimate the probability of churn
* Classify customers into Low, Medium and High risk
* Identify important factors contributing to predictions
* Expose the trained model through a REST API
* Provide an interactive dashboard for predictions

---

## 🎯 Problem Statement

Given customer demographic, service, contract and billing information, predict whether the customer is likely to leave the company.

### Target

```text
0 → Customer stayed
1 → Customer churned
```

---

## 📂 Dataset

The project uses the IBM Telco Customer Churn sample dataset.

Dataset characteristics:

* 7,043 customer records
* 21 original columns
* Binary churn target
* Customer demographic information
* Service information
* Contract information
* Billing information

The dataset is a sample dataset for a fictional telecommunications company.

Source:

IBM Telco Customer Churn Dataset

https://github.com/IBM/telco-customer-churn-on-icp4d

---

## 🧠 Machine Learning Pipeline

```text
Raw Customer Data
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Train/Test Split
        ↓
Preprocessing Pipeline
        ↓
Model Training
        ↓
Model Comparison
        ↓
Hyperparameter Tuning
        ↓
Final Model
        ↓
SHAP Explainability
        ↓
FastAPI
        ↓
Streamlit Dashboard
```

---

## 🔍 Exploratory Data Analysis

The analysis investigates relationships between churn and:

* Contract type
* Customer tenure
* Monthly charges
* Total charges
* Payment method
* Internet service
* Technical support
* Online security
* Number of subscribed services

---

## ⚙️ Feature Engineering

Additional features are created from the original customer attributes.

### Service Count

Number of subscribed services.

### Average Monthly Spend

```text
Total Charges / Tenure
```

### High Monthly Charge

Binary indicator based on the dataset's median monthly charge.

### Tenure Group

Customers are grouped into:

* New
* Growing
* Established
* Loyal
* Long Term

### Technical Support Indicator

Combines technical support and online security information.

### Electronic Payment Indicator

Identifies customers using electronic payment.

---

## 🤖 Models

The following classification algorithms are evaluated:

1. Logistic Regression
2. Decision Tree
3. Random Forest
4. XGBoost
5. LightGBM

Models are compared using:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC

Because churn is an imbalanced classification problem, the project does not rely on accuracy alone.

---

## 📊 Model Evaluation

The current experiment produced the following results:

| Model               |     Accuracy |    Precision |       Recall |     F1 Score |      ROC-AUC |
| ------------------- | -----------: | -----------: | -----------: | -----------: | -----------: |
| Logistic Regression |     0.725657 |     0.490132 |     0.796791 |     0.606925 | **0.835134** |
| Decision Tree       |     0.733475 |     0.499165 | **0.799465** | **0.614594** |     0.818165 |
| Random Forest       |     0.764748 |     0.548533 |     0.649733 |     0.594859 |     0.816146 |
| XGBoost             | **0.779673** | **0.596386** |     0.529412 |     0.560907 |     0.821851 |
| LightGBM            |     0.769012 |     0.574468 |     0.505348 |     0.537696 |     0.817214 |

### Evaluation Summary

The models show different trade-offs across the evaluation metrics:

* **XGBoost** achieved the highest accuracy at **77.97%**.
* **Logistic Regression** achieved the highest ROC-AUC at **83.51%**.
* **Decision Tree** achieved the highest recall at **79.95%**.
* **Decision Tree** also achieved the highest F1 score at **61.46%**.
* Logistic Regression also achieved a high recall of **79.68%**.

Since customer churn detection can prioritize identifying potential churners, recall and F1 score are considered alongside accuracy and ROC-AUC rather than relying on accuracy alone.

---

## 🔬 Explainable AI

SHAP is used to understand model predictions.

The system provides:

* Global feature importance
* Feature contribution
* Individual customer explanations

Example:

```text
Prediction: High Churn Risk

Important contributing factors:

• Short customer tenure
• Month-to-month contract
• High monthly charges
• Lack of technical support
• Payment behavior
```

---

## 🌐 FastAPI

The trained model is exposed through a REST API.

### Endpoint

```text
POST /predict
```

### Example Request

```json
{
  "gender": "Female",
  "SeniorCitizen": 0,
  "Partner": "No",
  "Dependents": "No",
  "tenure": 5,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "DSL",
  "OnlineSecurity": "No",
  "OnlineBackup": "No",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "No",
  "StreamingMovies": "No",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 70.0,
  "TotalCharges": 350.0,
  "ServiceCount": 1,
  "AverageMonthlySpend": 70.0,
  "HighMonthlyCharge": 1,
  "TenureGroup": "New",
  "HasTechnicalSupport": 0,
  "UsesElectronicPayment": 1
}
```

### Example Response

```json
{
  "churn_prediction": "Yes",
  "churn_probability": 0.84,
  "risk_level": "High"
}
```

---

## 🖥️ Streamlit Dashboard

The project includes an interactive dashboard where users can enter customer information and receive:

* Churn prediction
* Churn probability
* Risk level

Run:

```bash
streamlit run dashboard/app.py
```

---

## 🐳 Docker

Build the image:

```bash
docker build -t customer-churn-api .
```

Run:

```bash
docker run -p 8000:8000 customer-churn-api
```

---

## 📁 Project Structure

```text
customer-churn-prediction/

│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_feature_engineering.ipynb
│   └── 04_model_training.ipynb
│
├── src/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── features.py
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
│
├── models/
│   ├── churn_model.joblib
│   └── model_metadata.joblib
│
├── outputs/
│   ├── figures/
│   └── reports/
│
├── api/
│   └── main.py
│
├── dashboard/
│   └── app.py
│
├── tests/
│   └── test_prediction.py
│
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

---

## 🛠️ Tech Stack

### Programming

* Python

### Data Science

* Pandas
* NumPy
* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn
* XGBoost
* LightGBM

### Explainable AI

* SHAP

### Backend

* FastAPI
* Pydantic

### Frontend / Dashboard

* Streamlit

### Deployment

* Docker

### Version Control

* Git
* GitHub

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/JohiChawla/Customer-Churn-Prediction-System.git

cd customer-churn-prediction
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 📥 Dataset Setup

Download the IBM Telco Customer Churn dataset and place it at:

```text
data/raw/Telco-Customer-Churn.csv
```

Then run the notebooks in order:

```text
01_data_exploration.ipynb
02_eda.ipynb
03_feature_engineering.ipynb
04_model_training.ipynb
```

---

## 🚀 Run the API

```bash
uvicorn api.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

## 📊 Run the Dashboard

Start the API first:

```bash
uvicorn api.main:app --reload
```

Then:

```bash
streamlit run dashboard/app.py
```

---

## 🧪 Run Tests

```bash
pytest
```

---

## 📌 Key Learning Outcomes

This project demonstrates practical experience with:

* Binary classification
* Exploratory data analysis
* Data preprocessing
* Feature engineering
* Handling categorical variables
* Imbalanced classification
* Model comparison
* Hyperparameter tuning
* Model evaluation
* Explainable AI
* REST API development
* Interactive ML dashboards
* Docker
* Automated testing
* Git/GitHub project organization

---

## 🔮 Future Improvements

Possible future improvements include:

* MLflow experiment tracking
* Model monitoring
* Automated retraining
* Cloud deployment
* CI/CD pipeline
* Customer segmentation
* Retention campaign recommendation
* Cost-sensitive threshold optimization
* Batch prediction for large customer datasets

---

## 👨‍💻 Author

**Johi Chawla**

Computer Science Graduate | AI/ML Engineer

GitHub: https://github.com/JohiChawla

LinkedIn: https://linkedin.com/in/johi-chawla-55648a267
