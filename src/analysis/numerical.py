"""
Numerical analysis utilities.
"""

from __future__ import annotations

import pandas as pd


def numerical_summary(
    df: pd.DataFrame,
    column: str,
) -> pd.Series:
    """
    Return summary statistics for a numeric feature.
    """

    return (
        df[column]
        .describe()
    )