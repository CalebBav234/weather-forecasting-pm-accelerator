"""
Scatter plot visualization utilities.
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


def plot_scatter(
    df: pd.DataFrame,
    x: str,
    y: str,
    title: str,
    xlabel: str,
    ylabel: str,
    filename: str,
    alpha: float = 0.20,
    size: int = 8,
) -> None:
    """
    Create a standardized scatter plot.
    """

    if x not in df.columns:
        raise ValueError(f"{x} not found.")

    if y not in df.columns:
        raise ValueError(f"{y} not found.")

    initialize_plot(figsize=(8, 6))

    plt.scatter(
        df[x],
        df[y],
        alpha=alpha,
        s=size,
    )

    finalize_plot(
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
    )

    save_figure(
        filename=filename,
        category="scatter",
    )

    display_plot()