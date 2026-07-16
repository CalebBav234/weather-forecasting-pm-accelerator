"""
Baseline regression model.

Provides a reusable baseline model using
scikit-learn's DummyRegressor.
"""

from __future__ import annotations

import pandas as pd

from sklearn.dummy import DummyRegressor

from .evaluation import evaluate_regression


def train_baseline_model(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    X_test: pd.DataFrame,
    y_test: pd.Series,
    strategy: str = "mean",
):
    """
    Train and evaluate a baseline regression model.

    Parameters
    ----------
    X_train : pandas.DataFrame
        Training features.

    y_train : pandas.Series
        Training target.

    X_test : pandas.DataFrame
        Testing features.

    y_test : pandas.Series
        Testing target.

    strategy : str, default="mean"
        DummyRegressor strategy.

    Returns
    -------
    model
        Trained DummyRegressor.

    metrics
        Evaluation metrics.

    predictions
        Model predictions.
    """

    model = DummyRegressor(
        strategy=strategy,
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