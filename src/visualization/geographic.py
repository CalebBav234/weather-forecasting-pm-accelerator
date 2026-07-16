"""
Geographic visualization utilities.

Provides standardized geographic scatter plots.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd

from .styling import (
    initialize_plot,
    finalize_plot,
    save_figure,
    display_plot,
)


def plot_scatter_map(
    df: pd.DataFrame,
    latitude_col: str = "latitude",
    longitude_col: str = "longitude",
    title: str = "Geographic Distribution of Weather Observations",
    filename: str = "geographic_distribution.png",
    alpha: float = 0.30,
    size: int = 8,
) -> None:
    """
    Plot observation locations using latitude and longitude.
    """

    if latitude_col not in df.columns:
        raise ValueError(f"Column '{latitude_col}' not found.")

    if longitude_col not in df.columns:
        raise ValueError(f"Column '{longitude_col}' not found.")

    initialize_plot(figsize=(12, 6))

    plt.scatter(
        df[longitude_col],
        df[latitude_col],
        alpha=alpha,
        s=size,
    )

    finalize_plot(
        title=title,
        xlabel="Longitude",
        ylabel="Latitude",
    )

    save_figure(
        filename=filename,
        category="geographic",
    )

    display_plot()