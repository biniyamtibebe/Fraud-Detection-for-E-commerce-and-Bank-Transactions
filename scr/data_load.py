from pathlib import Path
import pandas as pd


class DataLoader:
    """
    Centralized data loading and validation for the fraud detection project.
    """

    def __init__(self, data_dir: str = "data/raw"):
        self.data_dir = Path(data_dir)

        if not self.data_dir.exists():
            raise FileNotFoundError(f"Data directory not found: {self.data_dir}")

    def _load_csv(self, filename: str) -> pd.DataFrame:
        """
        Internal helper to load a CSV with consistent error handling.
        """
        file_path = self.data_dir / filename

        if not file_path.exists():
            raise FileNotFoundError(f"Missing data file: {file_path}")

        try:
            df = pd.read_csv(file_path)
        except Exception as e:
            raise RuntimeError(f"Failed to load {filename}: {e}")

        if df.empty:
            raise ValueError(f"{filename} was loaded but is empty")

        return df

    def load_fraud_data(self) -> pd.DataFrame:
        """
        Load e-commerce fraud transaction data.
        """
        required_cols = {
            "user_id", "signup_time", "purchase_time",
            "purchase_value", "device_id", "source",
            "browser", "sex", "age", "ip_address", "class"
        }

        df = self._load_csv(r"C:\Users\hp\Music\Adey Innovations inc\Fraud-Detection-for-E-commerce-and-Bank-Transactions\data\raw\Fraud_Data.csv")
        self._validate_columns(df, required_cols, "Fraud_Data.csv")
        return df

    def load_ip_country_data(self) -> pd.DataFrame:
        """
        Load IP to country mapping data.
        """
        required_cols = {
            "lower_bound_ip_address",
            "upper_bound_ip_address",
            "country"
        }

        df = self._load_csv(r"C:\Users\hp\Music\Adey Innovations inc\Fraud-Detection-for-E-commerce-and-Bank-Transactions\data\raw\IpAddress_to_Country.csv")
        self._validate_columns(df, required_cols, "IpAddress_to_Country.csv")
        return df

    def load_creditcard_data(self) -> pd.DataFrame:
        """
        Load bank transaction fraud data.
        """
        df = self._load_csv(r"c:\Users\hp\Music\Adey Innovations inc\Fraud-Detection-for-E-commerce-and-Bank-Transactions\data\raw\creditcard.csv")

        if "Class" not in df.columns:
            raise ValueError("creditcard.csv must contain 'Class' column")

        return df

    @staticmethod
    def _validate_columns(df: pd.DataFrame, required_cols: set, name: str):
        """
        Validate required columns exist.
        """
        missing = required_cols - set(df.columns)
        if missing:
            raise ValueError(f"{name} missing required columns: {missing}")
