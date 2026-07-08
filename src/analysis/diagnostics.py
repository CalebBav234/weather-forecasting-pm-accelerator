"""
Dataset diagnostics.
"""

from __future__ import annotations

import pandas as pd


def missing_values(df: pd.DataFrame) -> pd.Series:
    """
    Return missing values by column.
    """

    return (
        df.isnull()
        .sum()
        .sort_values(ascending=False)
    )


def duplicate_rows(df: pd.DataFrame) -> int:
    """
    Return duplicate row count.
    """

    return int(
        df.duplicated().sum()
    )