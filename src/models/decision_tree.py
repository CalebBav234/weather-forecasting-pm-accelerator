"""
Decision Tree regression model.

Provides reusable functions for training
and evaluating a Decision Tree Regressor.
"""

from __future__ import annotations

import pandas as pd

from sklearn.tree import DecisionTreeRegressor

from .evaluation import evaluate_regression


def train_decision_tree(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    X_test: pd.DataFrame,
    y_test: pd.Series,
    random_state: int = 42,
):
    """
    Train and evaluate a Decision Tree Regressor.
    """

    model = DecisionTreeRegressor(
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