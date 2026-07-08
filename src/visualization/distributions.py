"""
Distribution visualizations.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd

from .styling import (
    DEFAULT_FIGSIZE,
    save_figure,
    set_plot_style,
)


def histogram(
    df: pd.DataFrame,
    column: str,
    title: str,
    xlabel: str,
    filename: str,
    bins: int = 40,
) -> None:
    """
    Create a standardized histogram.
    """

    set_plot_style()

    plt.figure(figsize=DEFAULT_FIGSIZE)

    plt.hist(
        df[column],
        bins=bins,
        edgecolor="black",
    )

    plt.title(title)

    plt.xlabel(xlabel)

    plt.ylabel("Frequency")

    plt.grid(alpha=0.3)

    save_figure(
        filename,
        "distributions",
    )

    plt.show()