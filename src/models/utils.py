"""
Model utility functions.
"""

from __future__ import annotations

import pandas as pd


def summarize_dataset(
    X: pd.DataFrame,
    y,
) -> None:
    """
    Print dataset summary.
    """

    print(
        f"Features Shape: {X.shape}"
    )

    print(
        f"Target Shape: {y.shape}"
    )