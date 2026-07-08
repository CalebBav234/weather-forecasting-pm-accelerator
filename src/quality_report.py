"""
quality_report.py

Generate a comprehensive data quality report for the weather dataset.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.logger import get_logger
from src.utils import dataframe_memory_usage

logger = get_logger(__name__)


def generate_quality_report(
    df: pd.DataFrame,
    output_path: Path,
) -> None:
    """
    Generate a text-based data quality report.
    """

    logger.info("Generating data quality report...")

    report = []

    report.append("=" * 80)
    report.append("GLOBAL WEATHER DATASET - DATA QUALITY REPORT")
    report.append("=" * 80)

    report.append(f"Rows: {len(df):,}")
    report.append(f"Columns: {len(df.columns)}")
    report.append("")

    report.append(f"Memory Usage: {dataframe_memory_usage(df):.2f} MB")
    report.append("")

    report.append("DATA TYPES")
    report.append("-" * 80)
    report.append(str(df.dtypes.value_counts()))
    report.append("")

    report.append("MISSING VALUES")
    report.append("-" * 80)
    report.append(str(df.isnull().sum()))
    report.append("")

    report.append(f"Duplicate Rows: {df.duplicated().sum()}")
    report.append("")

    report.append("NUMERICAL SUMMARY")
    report.append("-" * 80)
    report.append(str(df.describe()))
    report.append("")

    report.append("TOP 10 CITIES")
    report.append("-" * 80)
    report.append(str(df["location_name"].value_counts().head(10)))
    report.append("")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write("\n".join(report))

    logger.info("Data quality report saved to %s", output_path)