"""
config.py

Centralized project configuration.

This module contains configurable settings used throughout the project.
Changing values here should modify the behavior of the entire pipeline
without requiring changes elsewhere in the code.

Author:
    Caleb Mario Baving Auza

Project:
    PM Accelerator - Advanced Weather Forecasting and Climate Analytics
"""

from src.constants import RANDOM_SEED

PROJECT_NAME: str = "Advanced Weather Forecasting and Climate Analytics"

AUTHOR: str = "Caleb Mario Baving Auza"

SEED: int = RANDOM_SEED

TRAIN_TEST_SPLIT: float = 0.20

VALIDATION_SPLIT: float = 0.10

FORECAST_HORIZON: int = 24

TARGET_VARIABLE: str | None = None
"""
Will be assigned after the dataset schema is validated.
"""

ENABLE_HYPERPARAMETER_TUNING: bool = True

ENABLE_ENSEMBLE: bool = True

ENABLE_SHAP_ANALYSIS: bool = True

SAVE_TRAINED_MODELS: bool = True


ENABLE_DASHBOARD: bool = True


LOG_LEVEL: str = "INFO"