"""
Categorical analysis utilities.
"""

from __future__ import annotations

import pandas as pd


def top_categories(
    df: pd.DataFrame,
    column: str,
    n: int = 10,
) -> pd.Series:
    """
    Return the top N categories.
    """

    return (
        df[column]
        .value_counts()
        .head(n)
    )