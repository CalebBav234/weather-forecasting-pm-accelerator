"""
Datetime feature engineering utilities.

Creates additional calendar-based features from
timestamp columns.
"""

from __future__ import annotations

import pandas as pd


def extract_datetime_features(
    df: pd.DataFrame,
    datetime_column: str = "last_updated",
) -> pd.DataFrame:
    """
    Extract useful calendar features from a datetime column.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe.

    datetime_column : str
        Datetime column.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing additional datetime features.
    """

    if datetime_column not in df.columns:
        raise ValueError(
            f"Column '{datetime_column}' not found."
        )

    df = df.copy()

    df[datetime_column] = pd.to_datetime(df[datetime_column])

    df["year"] = df[datetime_column].dt.year

    df["month"] = df[datetime_column].dt.month

    df["day"] = df[datetime_column].dt.day

    df["hour"] = df[datetime_column].dt.hour

    df["day_of_week"] = df[datetime_column].dt.dayofweek

    df["week_of_year"] = (
        df[datetime_column]
        .dt.isocalendar()
        .week
        .astype(int)
    )

    df["quarter"] = df[datetime_column].dt.quarter

    df["is_weekend"] = (
        df["day_of_week"] >= 5
    ).astype(int)

    return df