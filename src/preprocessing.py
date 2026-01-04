"""
preprocessing.py

Reusable feature selection and preprocessing utilities
for the Early Warning Churn Risk System (SME Customers).
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def prepare_model_data(
    df: pd.DataFrame,
    feature_cols: list,
    target_col: str,
    test_size: float = 0.2,
    random_state: int = 42,
):
    """
    Prepare train/test datasets with leakage-safe preprocessing.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataset
    feature_cols : list
        List of feature column names
    target_col : str
        Target column name
    test_size : float
        Fraction of data to use as test set
    random_state : int
        Random seed for reproducibility

    Returns
    -------
    X_train_scaled, X_test_scaled, y_train, y_test, scaler
    """

    X = df[feature_cols]
    y = df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        stratify=y,
        random_state=random_state,
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test, scaler
