from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier


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
