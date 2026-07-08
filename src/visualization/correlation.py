"""
Correlation visualization utilities.

Provides standardized correlation heatmaps and helper functions
for identifying highly correlated features.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from .styling import (
    display_plot,
    initialize_plot,
    save_figure,
)


def plot_correlation_heatmap(
    df: pd.DataFrame,
    title: str = "Correlation Matrix",
    filename: str = "correlation_heatmap.png",
    method: str = "pearson",
) -> None:
    """
    Plot a correlation heatmap for all numeric columns.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataset.
    title : str, default="Correlation Matrix"
        Plot title.
    filename : str, default="correlation_heatmap.png"
        Output filename.
    method : str, default="pearson"
        Correlation method ('pearson', 'spearman', or 'kendall').
    """

    numeric_df = df.select_dtypes(include=np.number)

    if numeric_df.empty:
        raise ValueError(
            "No numeric columns available for correlation analysis."
        )

    correlation_matrix = numeric_df.corr(method=method)

    initialize_plot(figsize=(14, 10))

    sns.heatmap(
        correlation_matrix,
        cmap="coolwarm",
        center=0,
        square=True,
        linewidths=0.5,
        annot=False,
        cbar_kws={"label": "Correlation"},
    )

    plt.title(title)

    save_figure(
        filename=filename,
        category="correlation",
    )

    display_plot()


def get_high_correlations(
    df: pd.DataFrame,
    threshold: float = 0.80,
    method: str = "pearson",
) -> pd.DataFrame:
    """
    Return feature pairs whose absolute correlation exceeds
    the specified threshold.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataset.
    threshold : float, default=0.80
        Minimum absolute correlation.
    method : str, default="pearson"
        Correlation method.

    Returns
    -------
    pandas.DataFrame
        Sorted table of highly correlated feature pairs.
    """

    numeric_df = df.select_dtypes(include=np.number)

    if numeric_df.empty:
        raise ValueError(
            "No numeric columns available for correlation analysis."
        )

    corr = numeric_df.corr(method=method).abs()

    upper_triangle = corr.where(
        np.triu(
            np.ones(corr.shape),
            k=1,
        ).astype(bool)
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
        high_corr["Correlation"] >= threshold
    ]

    high_corr = high_corr.sort_values(
        by="Correlation",
        ascending=False,
    ).reset_index(drop=True)

    return high_corr