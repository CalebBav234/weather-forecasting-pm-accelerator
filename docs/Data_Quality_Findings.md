# Data Quality Findings

This document records data quality observations identified during exploratory data analysis. These findings will guide preprocessing and feature engineering decisions.

## Wind Speed

- Maximum observed value: **2963.2 km/h**
- Physically unrealistic for atmospheric wind speeds.
- Likely caused by measurement, ingestion, or recording error.
- Planned action: investigate and cap/remove unrealistic values during feature engineering while preserving legitimate extreme weather events.

## Temperature

- Maximum observed value: **79.3°C**
- Unusually high but requires investigation before deciding whether it is erroneous.
- Planned action: verify against source data and evaluate using domain-informed thresholds.

## Atmospheric Pressure

- Maximum observed value: **3006 mb**
- Physically unrealistic atmospheric pressure.
- Likely caused by measurement or recording error.
- Planned action: investigate and cap or remove unrealistic observations during feature engineering.

## Visibility

- No significant anomalies identified.

## UV Index

- No significant anomalies identified.
- Maximum observed value (16.3) remains physically plausible.

## Precipitation

- Distribution is heavily zero-inflated.
- No unrealistic precipitation values identified.
- Consider feature transformations during model development.