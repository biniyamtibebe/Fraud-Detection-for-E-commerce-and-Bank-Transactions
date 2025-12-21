import pandas as pd

def load_csv(path: str, required_cols=None):
    """
    Load CSV with basic validation.
    """
    df = pd.read_csv(path)

    if required_cols:
        missing = set(required_cols) - set(df.columns)
        if missing:
            raise ValueError(f"Missing required columns: {missing}")

    return df
