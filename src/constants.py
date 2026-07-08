"""
constants.py

Project-wide constants used throughout the Weather Forecasting project.

This module centralizes constant values to avoid hardcoding strings and
numeric values throughout the codebase.

Author:
    Caleb Mario Baving Auza

Project:
    PM Accelerator - Advanced Weather Forecasting and Climate Analytics
"""



RANDOM_SEED: int = 42



DEFAULT_FORECAST_HORIZON: int = 24  # hours
DEFAULT_TEST_SIZE: float = 0.20



EVALUATION_METRICS = [
    "MAE",
    "RMSE",
    "MAPE",
    "R2",
]



FORECASTING_MODELS = [
    "Baseline",
    "ARIMA",
    "SARIMA",
    "Prophet",
    "XGBoost",
    "LightGBM",
    "CatBoost",
    "LSTM",
]



LOG_FORMAT = (
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"



IMAGE_FORMATS = [
    ".png",
    ".jpg",
    ".jpeg",
    ".svg",
]



DATA_FILE_EXTENSIONS = [
    ".csv",
    ".parquet",
]