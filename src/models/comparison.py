"""
Model comparison utilities.

Provides reusable helper functions for comparing
multiple regression models.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def compare_models(
    results: dict,
    sort_by: str = "RMSE",
    ascending: bool = True,
    decimals: int = 4,
) -> pd.DataFrame:
    """
    Create a ranked comparison table.

    Parameters
    ----------
    results : dict
        Dictionary containing evaluation metrics.

    sort_by : str
        Metric used for ranking.

    ascending : bool
        Sort direction.

    decimals : int
        Number of decimal places.

    Returns
    -------
    pandas.DataFrame
    """

    comparison_df = pd.DataFrame(results).T

    comparison_df.index.name = "Model"

    comparison_df = comparison_df.sort_values(
        by=sort_by,
        ascending=ascending,
    )

    comparison_df = comparison_df.round(
        decimals,
    )

    comparison_df.insert(
        0,
        "Rank",
        range(
            1,
            len(comparison_df) + 1,
        ),
    )

    return comparison_df


def get_best_model(
    comparison_df: pd.DataFrame,
):
    """
    Return the name and metrics of the
    highest-ranked model.

    Parameters
    ----------
    comparison_df : pandas.DataFrame

    Returns
    -------
    tuple
    """

    best_name = comparison_df.index[0]

    best_metrics = comparison_df.iloc[0]

    return (
        best_name,
        best_metrics,
    )


def save_comparison(
    comparison_df: pd.DataFrame,
    filepath: str,
) -> None:
    """
    Save comparison table.

    Parameters
    ----------
    comparison_df : pandas.DataFrame

    filepath : str
    """

    filepath = Path(filepath)

    filepath.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    comparison_df.to_csv(
        filepath,
        index=True,
    )