"""
Feature selection utilities.

Provides reusable functions for selecting
features for machine learning models.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def select_numeric_features(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Return only numeric columns.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    pandas.DataFrame
    """

    return df.select_dtypes(include=np.number)


def remove_high_correlation(
    df: pd.DataFrame,
    threshold: float = 0.90,
) -> pd.DataFrame:
    """
    Remove highly correlated features.

    Parameters
    ----------
    df : pandas.DataFrame

    threshold : float

    Returns
    -------
    pandas.DataFrame
    """

    numeric_df = df.select_dtypes(include=np.number)

    corr = numeric_df.corr().abs()

    upper = corr.where(
        np.triu(
            np.ones(corr.shape),
            k=1,
        ).astype(bool)
    )

    to_drop = [
        column
        for column in upper.columns
        if any(
            upper[column] > threshold
        )
    ]

    return df.drop(columns=to_drop)


def split_features_target(
    df: pd.DataFrame,
    target: str,
) -> tuple[pd.DataFrame, pd.Series]:
    """
    Split dataframe into X and y.

    Parameters
    ----------
    df : pandas.DataFrame

    target : str

    Returns
    -------
    X
    y
    """

    if target not in df.columns:

        raise ValueError(
            f"{target} not found."
        )

    X = df.drop(columns=[target])

    y = df[target]

    return X, y