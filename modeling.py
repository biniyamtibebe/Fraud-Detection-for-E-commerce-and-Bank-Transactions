import imblearn.pipeline as Pipeline
from imblearn.over_sampling import SMOTE
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from src.data_utils import load_csv
from src.feature_engineering import engineer_fraud_features
from src.preprocessing import build_preprocessor
from src.modeling import build_model_pipeline

from sklearn.model_selection import train_test_split
from sklearn.metrics import average_precision_score


def build_model_pipeline(preprocessor, model_type="logistic"):
    if model_type == "logistic":
        model = LogisticRegression(max_iter=1000)
    elif model_type == "rf":
        model = RandomForestClassifier(
            n_estimators=200,
            max_depth=10,
            random_state=42,
            n_jobs=-1
        )
    else:
        raise ValueError("Unsupported model type")

    return Pipeline(steps=[
        ('preprocess', preprocessor),
        ('smote', SMOTE(random_state=42)),
        ('model', model)
    ])
