"""
validation.py

Validation utilities for the weather dataset.
"""

from __future__ import annotations

import pandas as pd

from src.logger import get_logger
from src.schema import EXPECTED_COLUMNS

logger = get_logger(__name__)


def validate_schema(df: pd.DataFrame) -> None:
    """
    Validate that the dataset contains all expected columns.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataset.

    Raises
    ------
    ValueError
        If expected columns are missing.
    """

    missing_columns = [
        column
        for column in EXPECTED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        logger.error("Schema validation failed.")
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    logger.info("Schema validation passed.")


def validate_duplicates(df: pd.DataFrame) -> None:
    """
    Validate duplicate rows.
    """

    duplicates = df.duplicated().sum()

    if duplicates > 0:
        logger.warning("%s duplicate rows detected.", duplicates)
    else:
        logger.info("No duplicate rows detected.")


def validate_missing_values(df: pd.DataFrame) -> None:
    """
    Validate missing values.
    """

    missing = df.isnull().sum().sum()

    if missing > 0:
        logger.warning("%s missing values detected.", missing)
    else:
        logger.info("No missing values detected.")