"""
XGBoost regression model.

Provides reusable functions for training
and evaluating an XGBoost Regressor.
"""

from __future__ import annotations

import pandas as pd

from xgboost import XGBRegressor

from .evaluation import evaluate_regression


def train_xgboost(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    X_test: pd.DataFrame,
    y_test: pd.Series,
    n_estimators: int = 100,
    learning_rate: float = 0.10,
    max_depth: int = 6,
    random_state: int = 42,
):
    """
    Train and evaluate an XGBoost Regressor.
    """

    model = XGBRegressor(
        n_estimators=n_estimators,
        learning_rate=learning_rate,
        max_depth=max_depth,
        random_state=random_state,
        objective="reg:squarederror",
        n_jobs=-1,
    )

    model.fit(
        X_train,
        y_train,
    )

    predictions = model.predict(
        X_test,
    )

    metrics = evaluate_regression(
        y_test,
        predictions,
    )

    return (
        model,
        metrics,
        predictions,
    )