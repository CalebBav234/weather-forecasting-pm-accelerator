"""
Feature scaling utilities.

Provides reusable functions for scaling
numerical features.
"""

from __future__ import annotations

import pandas as pd

from sklearn.preprocessing import (
    StandardScaler,
    MinMaxScaler,
)


def scale_features(
    df: pd.DataFrame,
    columns: list[str],
    method: str = "standard",
) -> tuple[pd.DataFrame, object]:
    """
    Scale numerical features.

    Parameters
    ----------
    df : pandas.DataFrame

    columns : list[str]

    method : str
        "standard"
        "minmax"

    Returns
    -------
    scaled dataframe
    fitted scaler
    """

    df = df.copy()

    for column in columns:

        if column not in df.columns:

            raise ValueError(
                f"Column '{column}' not found."
            )

    if method == "standard":

        scaler = StandardScaler()

    elif method == "minmax":

        scaler = MinMaxScaler()

    else:

        raise ValueError(
            "method must be 'standard' or 'minmax'."
        )

    df[columns] = scaler.fit_transform(
        df[columns]
    )

    return df, scaler