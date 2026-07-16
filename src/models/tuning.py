"""
Hyperparameter tuning utilities.

Provides reusable functions for tuning
machine learning models using
GridSearchCV and RandomizedSearchCV.
"""

from __future__ import annotations

import pandas as pd

from sklearn.model_selection import (
    GridSearchCV,
    RandomizedSearchCV,
)

from .evaluation import evaluate_regression


def tune_model(
    model,
    param_grid: dict,
    X_train: pd.DataFrame,
    y_train: pd.Series,
    X_test: pd.DataFrame,
    y_test: pd.Series,
    method: str = "grid",
    cv = 3,
    scoring: str = "neg_root_mean_squared_error",
    n_iter: int = 8,
    random_state: int = 42,
    n_jobs: int = 2,
):
    """
    Tune a regression model.

    Parameters
    ----------
    model
        Estimator to tune.

    param_grid : dict
        Hyperparameter search space.

    X_train : pandas.DataFrame

    y_train : pandas.Series

    X_test : pandas.DataFrame

    y_test : pandas.Series

    method : str
        "grid" or "random"

    cv : int

    scoring : str

    n_iter : int
        Number of iterations for RandomizedSearchCV.

    random_state : int

    n_jobs : int

    Returns
    -------
    best_model

    metrics

    predictions

    best_parameters
    """

    if method == "grid":

        search = GridSearchCV(
            estimator=model,
            param_grid=param_grid,
            cv=cv,
            scoring=scoring,
            n_jobs=n_jobs,
        )

    elif method == "random":

        search = RandomizedSearchCV(
            estimator=model,
            param_distributions=param_grid,
            n_iter=n_iter,
            cv=cv,
            scoring=scoring,
            random_state=random_state,
            n_jobs=n_jobs,
        )

    else:

        raise ValueError(
            "method must be 'grid' or 'random'."
        )

    search.fit(
        X_train,
        y_train,
    )

    best_model = search.best_estimator_

    predictions = best_model.predict(
        X_test,
    )

    metrics = evaluate_regression(
        y_test,
        predictions,
    )

    return (
        best_model,
        metrics,
        predictions,
        search.best_params_,
    )