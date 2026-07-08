"""
data_profiler.py

Generate a professional profile of the weather dataset.

Author:
    Caleb Mario Baving Auza
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.logger import get_logger

logger = get_logger(__name__)


def generate_data_profile(
    df: pd.DataFrame,
    output_path: Path,
) -> None:
    """
    Generate a detailed dataset profile.
    """

    logger.info("Generating data profile...")

    report = []

    report.append("=" * 80)
    report.append("GLOBAL WEATHER DATA PROFILE")
    report.append("=" * 80)
    report.append("")

    report.append(f"Rows: {len(df):,}")
    report.append(f"Columns: {len(df.columns)}")
    report.append("")

    report.append("DATA TYPES")
    report.append("-" * 80)
    report.append(str(df.dtypes.value_counts()))
    report.append("")

    report.append("NUMERIC FEATURES")
    report.append("-" * 80)

    numeric = df.select_dtypes(include="number").columns

    for column in numeric:
        report.append(column)

    report.append("")

    report.append("CATEGORICAL FEATURES")
    report.append("-" * 80)

    categorical = df.select_dtypes(include="object").columns

    for column in categorical:
        report.append(column)

    report.append("")

    report.append("TOP COUNTRIES")
    report.append("-" * 80)

    report.append(
        str(
            df["country"]
            .value_counts()
            .head(10)
        )
    )

    report.append("")

    report.append("TOP CITIES")
    report.append("-" * 80)

    report.append(
        str(
            df["location_name"]
            .value_counts()
            .head(10)
        )
    )

    report.append("")

    report.append("WEATHER CONDITIONS")
    report.append("-" * 80)

    report.append(
        str(
            df["condition_text"]
            .value_counts()
            .head(20)
        )
    )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        output_path,
        "w",
        encoding="utf-8",
    ) as file:
        file.write("\n".join(report))

    logger.info("Profile saved.")