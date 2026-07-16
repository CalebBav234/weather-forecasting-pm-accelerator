"""
CatBoost regression model.

Provides reusable functions for training
and evaluating a CatBoost Regressor.
"""

from __future__ import annotations

import pandas as pd

from catboost import CatBoostRegressor

from .evaluation import evaluate_regression


def train_catboost(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    X_test: pd.DataFrame,
    y_test: pd.Series,
    iterations: int = 100,
    learning_rate: float = 0.10,
    depth: int = 6,
    random_state: int = 42,
):
    """
    Train and evaluate a CatBoost Regressor.
    """

    model = CatBoostRegressor(
        iterations=iterations,
        learning_rate=learning_rate,
        depth=depth,
        random_seed=random_state,
        verbose=0,
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