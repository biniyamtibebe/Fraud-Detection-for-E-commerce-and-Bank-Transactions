import pandas as pd
import numpy as np

def engineer_fraud_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Time features
    df['signup_time'] = pd.to_datetime(df['signup_time'])
    df['purchase_time'] = pd.to_datetime(df['purchase_time'])

    df['hour_of_day'] = df['purchase_time'].dt.hour
    df['day_of_week'] = df['purchase_time'].dt.dayofweek
    df['time_since_signup'] = (
        df['purchase_time'] - df['signup_time']
    ).dt.total_seconds() / 3600

    # Transaction velocity
    df = df.sort_values(['user_id', 'purchase_time'])
    df['tx_count'] = df.groupby('user_id').cumcount() + 1

    return df
