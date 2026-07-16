"""
Categorical feature encoding utilities.

Provides reusable functions for encoding
categorical variables.
"""

from __future__ import annotations

import pandas as pd
from sklearn.preprocessing import LabelEncoder


def encode_categorical_features(
    df: pd.DataFrame,
    columns: list[str],
    method: str = "onehot",
) -> pd.DataFrame:
    """
    Encode categorical columns.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe.

    columns : list[str]
        Columns to encode.

    method : str
        Encoding method.
        Options:
            - "onehot"
            - "label"

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

    if method == "onehot":

        df = pd.get_dummies(
            df,
            columns=columns,
            drop_first=False,
            dtype=int,
        )

    elif method == "label":

        encoder = LabelEncoder()

        for column in columns:

            df[column] = encoder.fit_transform(
                df[column].astype(str)
            )

    else:

        raise ValueError(
            "method must be 'onehot' or 'label'."
        )

    return df