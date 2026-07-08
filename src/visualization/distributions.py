"""
Distribution visualization utilities.

Provides standardized plotting functions for numerical variables.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd

from .styling import (
    display_plot,
    finalize_plot,
    initialize_plot,
    save_figure,
)


def plot_histogram(
    df: pd.DataFrame,
    column: str,
    title: str,
    xlabel: str,
    filename: str,
    bins: int = 40,
) -> None:
    """
    Plot a standardized histogram.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataset.
    column : str
        Numeric column to visualize.
    title : str
        Plot title.
    xlabel : str
        Label for x-axis.
    filename : str
        Output filename.
    bins : int, default=40
        Number of histogram bins.
    """

    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame.")

    initialize_plot()

    plt.hist(
        df[column],
        bins=bins,
        edgecolor="black",
    )

    finalize_plot(
        title=title,
        xlabel=xlabel,
        ylabel="Frequency",
    )

    save_figure(
        filename=filename,
        category="distributions",
    )

    display_plot()


def plot_boxplot(
    df: pd.DataFrame,
    column: str,
    title: str,
    xlabel: str,
    filename: str,
) -> None:
    """
    Plot a standardized horizontal boxplot.
    """

    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame.")

    initialize_plot(figsize=(12, 4))

    plt.boxplot(
        df[column],
        vert=False,
    )

    finalize_plot(
        title=title,
        xlabel=xlabel,
        ylabel="",
    )

    save_figure(
        filename=filename,
        category="distributions",
    )

    display_plot()