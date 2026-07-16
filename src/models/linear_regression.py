"""
Linear Regression model.

Provides reusable functions for training
and evaluating a Linear Regression model.
"""

from __future__ import annotations

import pandas as pd

from sklearn.linear_model import LinearRegression

from .evaluation import evaluate_regression


def train_linear_regression(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    X_test: pd.DataFrame,
    y_test: pd.Series,
):
    """
    Train and evaluate a Linear Regression model.

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

    Returns
    -------
    model
        Trained LinearRegression model.

    metrics
        Evaluation metrics.

    predictions
        Model predictions.
    """

    model = LinearRegression()

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