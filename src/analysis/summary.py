"""
Dataset summary utilities.
"""

from __future__ import annotations

import pandas as pd


def dataset_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return a high-level summary of the dataset.
    """

    summary = pd.DataFrame(
        {
            "Metric": [
                "Rows",
                "Columns",
                "Missing Values",
                "Duplicate Rows",
                "Memory Usage (MB)",
            ],
            "Value": [
                len(df),
                len(df.columns),
                df.isnull().sum().sum(),
                df.duplicated().sum(),
                round(
                    df.memory_usage(deep=True).sum() / 1024**2,
                    2,
                ),
            ],
        }
    )

    return summary