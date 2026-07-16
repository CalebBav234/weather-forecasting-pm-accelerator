"""
Complete feature engineering pipeline.

Combines all preprocessing steps into a
single reusable function.
"""

from __future__ import annotations

import pandas as pd

from .datetime_features import (
    extract_datetime_features,
)

from .encoding import (
    encode_categorical_features,
)

from .outliers import (
    clip_outliers_iqr,
)

from .scaling import (
    scale_features,
)


def preprocess_pipeline(
    df: pd.DataFrame,
    categorical_columns: list[str],
    numerical_columns: list[str],
    encoding_method: str = "onehot",
    scaling_method: str = "standard",
):
    """
    Complete preprocessing pipeline.

    Parameters
    ----------
    df : pandas.DataFrame

    categorical_columns : list[str]

    numerical_columns : list[str]

    encoding_method : str

    scaling_method : str

    Returns
    -------
    processed dataframe
    fitted scaler
    """

    processed_df = df.copy()



    processed_df = extract_datetime_features(
        processed_df
    )

    

    processed_df = encode_categorical_features(
        processed_df,
        columns=categorical_columns,
        method=encoding_method,
    )

    

    processed_df = clip_outliers_iqr(
        processed_df,
        columns=numerical_columns,
    )

    

    processed_df, scaler = scale_features(
        processed_df,
        columns=numerical_columns,
        method=scaling_method,
    )

    return processed_df, scaler