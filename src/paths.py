"""
paths.py

Centralized project path management.

This module defines all important directories used throughout the project.
Using pathlib ensures compatibility across Windows, macOS, and Linux.

Author:
    Caleb Mario Baving Auza

Project:
    PM Accelerator - Advanced Weather Forecasting and Climate Analytics
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

EXTERNAL_DATA_DIR = DATA_DIR / "external"

SRC_DIR = PROJECT_ROOT / "src"

DOCS_DIR = PROJECT_ROOT / "docs"

MODELS_DIR = PROJECT_ROOT / "models"

OUTPUTS_DIR = PROJECT_ROOT / "outputs"

FIGURES_DIR = OUTPUTS_DIR / "figures"

METRICS_DIR = OUTPUTS_DIR / "metrics"

PREDICTIONS_DIR = OUTPUTS_DIR / "predictions"

LOGS_DIR = OUTPUTS_DIR / "logs"

DASHBOARD_DIR = PROJECT_ROOT / "dashboard"

NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"

TESTS_DIR = PROJECT_ROOT / "tests"

WEATHER_DATASET = RAW_DATA_DIR / "GlobalWeatherRepository.csv"