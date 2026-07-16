"""
Random Forest regression model.

Provides reusable functions for training
and evaluating a Random Forest Regressor.
"""

from __future__ import annotations

import pandas as pd

from sklearn.ensemble import RandomForestRegressor

from .evaluation import evaluate_regression


def train_random_forest(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    X_test: pd.DataFrame,
    y_test: pd.Series,
    n_estimators: int = 100,
    random_state: int = 42,
):
    """
    Train and evaluate a Random Forest Regressor.
    """

    model = RandomForestRegressor(
        n_estimators=n_estimators,
        random_state=random_state,
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