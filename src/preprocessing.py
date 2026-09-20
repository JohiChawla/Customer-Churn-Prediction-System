import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Load raw customer churn data."""

    df = pd.read_csv(path)

    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and prepare raw churn dataset."""

    df = df.copy()

    # Convert TotalCharges to numeric
    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    # Remove rows where TotalCharges is missing
    df = df.dropna(subset=["TotalCharges"])

    # Remove duplicate customer IDs
    df = df.drop_duplicates(subset=["customerID"])

    return df