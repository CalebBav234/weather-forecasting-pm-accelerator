"""
Feature engineering utility functions.

Provides reusable helper functions used
throughout the machine learning pipeline.
"""

from __future__ import annotations

from pathlib import Path
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split


def split_dataset(
    X: pd.DataFrame,
    y: pd.Series,
    test_size: float = 0.20,
    random_state: int = 42,
):
    """
    Split dataset into training and testing sets.
    """

    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
    )


def save_object(
    obj,
    filepath: str,
) -> None:
    """
    Save a Python object using joblib.
    """

    filepath = Path(filepath)

    filepath.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    joblib.dump(
        obj,
        filepath,
    )


def load_object(
    filepath: str,
):
    """
    Load a previously saved Python object.
    """

    return joblib.load(filepath)