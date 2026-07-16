"""
Model evaluation utilities.

Provides reusable evaluation metrics for
regression models.
"""

from __future__ import annotations

import pandas as pd

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)


def evaluate_regression(
    y_true,
    y_pred,
) -> pd.Series:
    """
    Evaluate regression predictions.

    Parameters
    ----------
    y_true

    y_pred

    Returns
    -------
    pandas.Series
        Regression metrics.
    """

    mae = mean_absolute_error(
        y_true,
        y_pred,
    )

    mse = mean_squared_error(
        y_true,
        y_pred,
    )

    rmse = mse ** 0.5

    r2 = r2_score(
        y_true,
        y_pred,
    )

    return pd.Series(
        {
            "MAE": mae,
            "MSE": mse,
            "RMSE": rmse,
            "R2": r2,
        }
    )