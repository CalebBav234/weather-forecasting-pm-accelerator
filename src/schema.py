"""
schema.py

Dataset schema definitions for the Global Weather Repository.

This module defines the expected columns and feature groupings used
throughout the project.

Author:
    Caleb Mario Baving Auza

Project:
    PM Accelerator - Advanced Weather Forecasting and Climate Analytics
"""

from __future__ import annotations

EXPECTED_COLUMNS = [
    "country",
    "location_name",
    "latitude",
    "longitude",
    "timezone",
    "last_updated_epoch",
    "last_updated",
    "temperature_celsius",
    "temperature_fahrenheit",
    "condition_text",
    "wind_mph",
    "wind_kph",
    "wind_degree",
    "wind_direction",
    "pressure_mb",
    "pressure_in",
    "precip_mm",
    "precip_in",
    "humidity",
    "cloud",
    "feels_like_celsius",
    "feels_like_fahrenheit",
    "visibility_km",
    "visibility_miles",
    "uv_index",
    "gust_mph",
    "gust_kph",
    "air_quality_Carbon_Monoxide",
    "air_quality_Ozone",
    "air_quality_Nitrogen_dioxide",
    "air_quality_Sulphur_dioxide",
    "air_quality_PM2.5",
    "air_quality_PM10",
    "air_quality_us-epa-index",
    "air_quality_gb-defra-index",
    "sunrise",
    "sunset",
    "moonrise",
    "moonset",
    "moon_phase",
    "moon_illumination",
]

NUMERIC_COLUMNS = [
    "latitude",
    "longitude",
    "temperature_celsius",
    "temperature_fahrenheit",
    "wind_mph",
    "wind_kph",
    "wind_degree",
    "pressure_mb",
    "pressure_in",
    "precip_mm",
    "precip_in",
    "humidity",
    "cloud",
    "feels_like_celsius",
    "feels_like_fahrenheit",
    "visibility_km",
    "visibility_miles",
    "uv_index",
    "gust_mph",
    "gust_kph",
    "air_quality_Carbon_Monoxide",
    "air_quality_Ozone",
    "air_quality_Nitrogen_dioxide",
    "air_quality_Sulphur_dioxide",
    "air_quality_PM2.5",
    "air_quality_PM10",
    "air_quality_us-epa-index",
    "air_quality_gb-defra-index",
    "moon_illumination",
]

CATEGORICAL_COLUMNS = [
    "country",
    "location_name",
    "timezone",
    "condition_text",
    "wind_direction",
    "moon_phase",
]

DATETIME_COLUMNS = [
    "last_updated",
    "sunrise",
    "sunset",
    "moonrise",
    "moonset",
]