"""
logger.py

Centralized logging configuration for the Weather Forecasting project.

Author:
    Caleb Mario Baving Auza

Project:
    PM Accelerator - Advanced Weather Forecasting and Climate Analytics
"""

from __future__ import annotations

import logging

from src.constants import DATE_FORMAT, LOG_FORMAT
from src.paths import LOGS_DIR

LOGS_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOGS_DIR / "weather_forecasting.log"


def get_logger(name: str) -> logging.Logger:
    """
    Create and configure a logger.

    Parameters
    ----------
    name : str
        Name of the logger (usually __name__).

    Returns
    -------
    logging.Logger
        Configured logger instance.
    """

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt=LOG_FORMAT,
        datefmt=DATE_FORMAT,
    )

    # Console output
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File output
    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger