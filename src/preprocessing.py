"""
preprocessing.py

Data preprocessing utilities for the Global Weather Repository dataset.

Author:
    Caleb Mario Baving Auza

Project:
    PM Accelerator - Advanced Weather Forecasting and Climate Analytics
"""

from __future__ import annotations

import pandas as pd

from src.logger import get_logger

logger = get_logger(__name__)


def convert_datetime_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert datetime columns to pandas datetime objects.
    """

    datetime_columns = [
        "last_updated",
    ]

    for column in datetime_columns:
        logger.info("Converting %s to datetime...", column)
        df[column] = pd.to_datetime(df[column])

    return df


def sort_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Sort dataset chronologically.
    """

    logger.info("Sorting dataset by last_updated...")

    return df.sort_values("last_updated").reset_index(drop=True)


def remove_duplicate_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows if any exist.
    """

    before = len(df)

    df = df.drop_duplicates()

    removed = before - len(df)

    logger.info("%s duplicate rows removed.", removed)

    return df


def preprocess_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Complete preprocessing pipeline.
    """

    logger.info("=" * 60)
    logger.info("Starting preprocessing pipeline...")
    logger.info("=" * 60)

    df = convert_datetime_columns(df)
    df = remove_duplicate_rows(df)
    df = sort_dataset(df)

    logger.info("Preprocessing complete.")

    return df