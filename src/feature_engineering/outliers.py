"""
Outlier handling utilities.

Provides reusable functions for clipping outliers
using the Interquartile Range (IQR) method.
"""

from __future__ import annotations

import pandas as pd


def clip_outliers_iqr(
    df: pd.DataFrame,
    columns: list[str],
    multiplier: float = 1.5,
) -> pd.DataFrame:
    """
    Clip outliers using the IQR method.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe.

    columns : list[str]
        Numerical columns.

    multiplier : float, default=1.5
        IQR multiplier.

    Returns
    -------
    pandas.DataFrame
    """

    df = df.copy()

    for column in columns:

        if column not in df.columns:
            raise ValueError(
                f"Column '{column}' not found."
            )

        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)

        iqr = q3 - q1

        lower = q1 - multiplier * iqr
        upper = q3 + multiplier * iqr

        df[column] = df[column].clip(
            lower=lower,
            upper=upper,
        )

    return df