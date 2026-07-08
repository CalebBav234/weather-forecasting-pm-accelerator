"""
Categorical visualizations.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd

from .styling import (
    DEFAULT_FIGSIZE,
    save_figure,
    set_plot_style,
)


def bar_chart(
    data: pd.Series,
    title: str,
    xlabel: str,
    ylabel: str,
    filename: str,
) -> None:
    """
    Create a standardized categorical bar chart.
    """

    set_plot_style()

    plt.figure(figsize=DEFAULT_FIGSIZE)

    data.plot(
        kind="bar",
        edgecolor="black",
    )

    plt.title(title)

    plt.xlabel(xlabel)

    plt.ylabel(ylabel)

    plt.xticks(rotation=45)

    plt.grid(axis="y", alpha=0.3)

    save_figure(
        filename,
        "categorical",
    )

    plt.show()