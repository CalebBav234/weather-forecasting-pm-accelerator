"""
Feature Engineering Package

Provides reusable preprocessing functions.
"""

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

from .feature_selection import (
    select_numeric_features,
    remove_high_correlation,
    split_features_target,
)

from .utils import (
    split_dataset,
    save_object,
    load_object,
)

from .pipeline import (
    preprocess_pipeline,
)

__all__ = [
    "extract_datetime_features",
    "encode_categorical_features",
    "clip_outliers_iqr",
    "scale_features",
    "select_numeric_features",
    "remove_high_correlation",
    "split_features_target",
    "split_dataset",
    "save_object",
    "load_object",
    "preprocess_pipeline",
]