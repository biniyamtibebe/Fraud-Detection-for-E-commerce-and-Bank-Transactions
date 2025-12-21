import pandas as pd 
def clean_fraud_data(df: pd.DataFrame) -> pd.DataFrame:
    required_columns = [
        'user_id', 'signup_time', 'purchase_time',
        'purchase_value', 'age', 'source',
        'browser', 'sex', 'ip_address', 'class'
    ]

    missing = set(required_columns) - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df = df.copy()

    # Type enforcement
    df['signup_time'] = pd.to_datetime(df['signup_time'], errors='coerce')
    df['purchase_time'] = pd.to_datetime(df['purchase_time'], errors='coerce')

    # Drop rows with invalid timestamps
    df = df.dropna(subset=['signup_time', 'purchase_time'])

    # Remove duplicates
    df = df.drop_duplicates()

    return df

import pandas as pd


def clean_creditcard_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and validate the credit card fraud dataset.
    """
    df = df.copy()

    if "Class" not in df.columns:
        raise ValueError("creditcard data must contain 'Class' column")

    # Drop duplicates
    df = df.drop_duplicates()

    # Ensure numeric columns
    non_numeric = df.drop(columns=["Class"]).select_dtypes(exclude="number").columns
    if len(non_numeric) > 0:
        raise ValueError(f"Non-numeric columns found: {non_numeric}")

    # Basic sanity check
    if df.isnull().sum().sum() > 0:
        raise ValueError("creditcard dataset contains missing values")

    return df
