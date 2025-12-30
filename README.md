# Fraud Detection for E-Commerce and Bank Transactions

## Project Overview

This project focuses on building an end-to-end machine learning pipeline to detect fraudulent transactions in highly imbalanced financial datasets.  
The goal is not only to achieve strong predictive performance, but also to ensure **interpretability**, **robust evaluation**, and **actionable business insights**.

The project covers:
- Data ingestion and preprocessing
- Feature engineering
- Model training and evaluation under class imbalance
- Model explainability using SHAP
- Practical fraud prevention recommendations

---

## Datasets

The project uses multiple real-world style datasets:

| Dataset | Description | Target |
|------|------------|-------|
| `creditcard.csv` | Credit card transactions | `Class` |
| `Fraud_Data.csv` | E-commerce fraud data | `class` |
| `IpAddress_to_Country.csv` | IP → country mapping | — |

> ⚠️ All datasets are **highly imbalanced**, with fraud cases representing a very small fraction of total transactions.

---

## Repository Structure

 ```fraud-detection/
      ├── data/ # Raw and processed data (gitignored)
      │ ├──  processed
      │ ├── raw 
      ├── notebooks/ # Jupyter notebooks for each phase
      │ ├── eda-fraud-data.ipynb
      │ ├── eda-creditcard.ipynb
      │ ├── feature-engineering.ipynb
      │ ├── modeling.ipynb
      │ └── shap-explainability.ipynb
      ├── models/ # Saved trained model artifacts
      ├──scr 
      │ ├── __init__.py
      ├──Scripts 
      │ ├── __init__.py
      ├── tests 
      │ ├── __init__.py
      ├── requirements.txt # Project dependencies
      ├── README.md # This file
      └── .gitignore 
```
---

## Task 1 – Data Preparation & Feature Engineering

### Key Steps

- Parsed and standardized datetime features
- Created behavioral and temporal features:
  - Hour of day
  - Day of week
  - Time since signup
  - Transaction velocity (1h / 24h windows)
- Merged IP address data to derive geographic features
- Handled missing values and invalid records
- Separated numerical and categorical variables

### Output

- Fully processed datasets saved under `data/processed/`
- Ready for modeling without data leakage

---

## Task 2 – Model Building and Evaluation

### Baseline Model
- **Logistic Regression**
- Interpretable and fast
- Used as performance benchmark

### Ensemble Model
- **Random Forest Classifier**
- Handles non-linear relationships and interactions
- Trained with:
  - Class weighting
  - SMOTE for minority class oversampling
  - Hyperparameter tuning using GridSearchCV

### Evaluation Metrics

Because accuracy is misleading for fraud detection, the following metrics were used:

- **F1-Score**
- **AUC-PR (Precision-Recall AUC)**
- **Confusion Matrix**
- **Stratified 5-Fold Cross-Validation**

### Model Selection

The Random Forest model was selected as the final model due to:
- Superior AUC-PR and F1-Score
- Better recall on fraud cases
- Acceptable interpretability when combined with SHAP

---

 ## Task 3 – Model Explainability (SHAP)

### Built-in Feature Importance
- Extracted from Random Forest
- Visualized top 10 contributing features

### SHAP Analysis

- SHAP Summary Plot for global importance
- SHAP Force Plots for individual predictions:
  - True Positive (correct fraud detection)
  - False Positive (legitimate transaction flagged)
  - False Negative (missed fraud)

### Key Findings

Top fraud drivers included:
- Very short time since signup
- High transaction velocity
- Unusual transaction timing
- Certain geographic patterns
- High-risk categorical behaviors

SHAP results aligned well with Random Forest feature importance, increasing confidence in the model’s decisions.

---

## Business Recommendations

Based on SHAP insights:

1. **Enhanced Verification for New Accounts**  
   Transactions occurring shortly after signup should trigger additional checks.

2. **Velocity-Based Rules**  
   Multiple transactions within short time windows should be flagged or rate-limited.

3. **Risk-Based Transaction Monitoring**  
   High-risk combinations of time, location, and behavior should dynamically adjust fraud thresholds.

These recommendations are directly grounded in model explanations, not black-box assumptions.

---

## Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- Imbalanced-learn (SMOTE)
- SHAP
- Matplotlib / Seaborn

---

## How to Run the Project

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run preprocessing:
   ``` bash
   Copy code
   python src/data_loading.py
   python src/preprocessing.py
   ```

3. Train models:

  ```bash
  Copy code
  python src/modeling.py
  ```
  ---

4. Run explainability:

  ```bash
  Copy code
  python src/explainability.py
  ```