"""
LightGBM regression model.

Provides reusable functions for training
and evaluating a LightGBM Regressor.
"""

from __future__ import annotations

import pandas as pd

from lightgbm import LGBMRegressor

from .evaluation import evaluate_regression


def train_lightgbm(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    X_test: pd.DataFrame,
    y_test: pd.Series,
    n_estimators: int = 100,
    learning_rate: float = 0.10,
    random_state: int = 42,
):
    """
    Train and evaluate a LightGBM Regressor.
    """

    model = LGBMRegressor(
        n_estimators=n_estimators,
        learning_rate=learning_rate,
        random_state=random_state,
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