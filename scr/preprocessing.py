from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def build_preprocessor(numerical_features, categorical_features):
    """
    Returns a ColumnTransformer with scaling and encoding.
    """
    return ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_features),
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
        ]
    )

from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as ImbPipeline
from sklearn.metrics import classification_report, roc_auc_score, average_precision_score


def build_model_pipeline(preprocessor, model, random_state=42):
    """
    Build a full modeling pipeline with explicit class imbalance handling.
    SMOTE is applied ONLY to the training data via the pipeline.
    """
    return ImbPipeline(steps=[
        ("preprocess", preprocessor),
        ("smote", SMOTE(random_state=random_state)),
        ("model", model)
    ])
