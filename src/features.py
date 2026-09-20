import pandas as pd


def create_features(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    # Number of subscribed services
    service_columns = [
        "PhoneService",
        "MultipleLines",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies"
    ]

    df["ServiceCount"] = 0

    for col in service_columns:
        df["ServiceCount"] += (
            df[col]
            .isin(["Yes"])
            .astype(int)
        )

    # Average monthly spend
    df["AverageMonthlySpend"] = (
        df["TotalCharges"] /
        df["tenure"].replace(0, 1)
    )

    # High monthly charge indicator
    median_charge = df["MonthlyCharges"].median()

    df["HighMonthlyCharge"] = (
        df["MonthlyCharges"] > median_charge
    ).astype(int)

    # Customer tenure groups
    df["TenureGroup"] = pd.cut(
        df["tenure"],
        bins=[-1, 12, 24, 48, 60, 100],
        labels=[
            "New",
            "Growing",
            "Established",
            "Loyal",
            "LongTerm"
        ]
    )

    # Support/security indicator
    df["HasTechnicalSupport"] = (
        (df["TechSupport"] == "Yes") |
        (df["OnlineSecurity"] == "Yes")
    ).astype(int)

    # Electronic payment indicator
    df["UsesElectronicPayment"] = (
        df["PaymentMethod"]
        .str.contains("electronic", case=False, na=False)
    ).astype(int)

    return df