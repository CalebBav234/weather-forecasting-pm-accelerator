"""
Correlation visualization utilities.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from .styling import (
    initialize_plot,
    finalize_plot,
    save_figure,
    display_plot,
)


def plot_correlation_heatmap(
    correlation_matrix: pd.DataFrame,
    title: str,
    filename: str,
) -> None:
    """
    Plot a correlation heatmap.
    """

    initialize_plot(figsize=(14, 12))

    plt.imshow(
        correlation_matrix,
        interpolation="nearest",
        aspect="auto",
    )

    plt.colorbar(label="Correlation")

    plt.xticks(
        range(len(correlation_matrix.columns)),
        correlation_matrix.columns,
        rotation=90,
        fontsize=8,
    )

    plt.yticks(
        range(len(correlation_matrix.columns)),
        correlation_matrix.columns,
        fontsize=8,
    )

    finalize_plot(
        title=title,
        xlabel="Features",
        ylabel="Features",
    )

    save_figure(
        filename=filename,
        category="correlation",
    )

    display_plot()


def get_high_correlations(
    correlation_matrix: pd.DataFrame,
    threshold: float = 0.80,
) -> pd.DataFrame:
    """
    Return highly correlated feature pairs.
    """

    upper_triangle = correlation_matrix.where(
        np.triu(np.ones(correlation_matrix.shape), k=1).astype(bool)
    )

    high_corr = (
        upper_triangle.stack()
        .reset_index()
        .rename(
            columns={
                "level_0": "Feature 1",
                "level_1": "Feature 2",
                0: "Correlation",
            }
        )
    )

    high_corr = high_corr[
        high_corr["Correlation"].abs() >= threshold
    ]

    high_corr = high_corr.sort_values(
        by="Correlation",
        ascending=False,
    )

    return high_corr.reset_index(drop=True)