"""
Categorical visualization utilities.

Provides standardized plotting functions for categorical variables.
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


def plot_bar_chart(
    data: pd.Series,
    title: str,
    xlabel: str,
    ylabel: str,
    filename: str,
) -> None:
    """
    Plot a standardized categorical bar chart.

    Parameters
    ----------
    data : pandas.Series
        Series containing category counts.
    title : str
        Plot title.
    xlabel : str
        X-axis label.
    ylabel : str
        Y-axis label.
    filename : str
        Output filename.
    """

    initialize_plot()

    data.plot(
        kind="bar",
        edgecolor="black",
    )

    finalize_plot(
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
    )

    plt.xticks(rotation=45, ha="right")

    save_figure(
        filename=filename,
        category="categorical",
    )

    display_plot()


def plot_horizontal_bar_chart(
    data: pd.Series,
    title: str,
    xlabel: str,
    ylabel: str,
    filename: str,
) -> None:
    """
    Plot a standardized horizontal bar chart.
    """

    initialize_plot(figsize=(10, 6))

    data.plot(
        kind="barh",
        edgecolor="black",
    )

    finalize_plot(
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
    )

    save_figure(
        filename=filename,
        category="categorical",
    )

    display_plot()