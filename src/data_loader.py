"""
data_loader.py

Functions for loading datasets used throughout the Weather Forecasting project.

Author:
    Caleb Mario Baving Auza

Project:
    PM Accelerator - Advanced Weather Forecasting and Climate Analytics
"""

from __future__ import annotations

import pandas as pd

from src.logger import get_logger
from src.paths import WEATHER_DATASET

logger = get_logger(__name__)


def load_weather_dataset() -> pd.DataFrame:
    """
    Load the primary weather dataset.

    Returns
    -------
    pd.DataFrame
        Weather dataset.
    """

    logger.info("Loading weather dataset...")

    df = pd.read_csv(WEATHER_DATASET)

    logger.info(
        "Dataset loaded successfully (%s rows, %s columns).",
        len(df),
        len(df.columns),
    )

    return df