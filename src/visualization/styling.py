"""
Shared visualization styling utilities.

Provides reusable helper functions for initializing,
formatting, displaying, and saving plots.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt



DEFAULT_FIGSIZE = (12, 6)



def initialize_plot(figsize: tuple = DEFAULT_FIGSIZE) -> None:
    """
    Initialize a new matplotlib figure.
    """

    plt.figure(figsize=figsize)




def finalize_plot(
    title: str,
    xlabel: str,
    ylabel: str,
) -> None:
    """
    Apply standardized formatting.
    """

    plt.title(title)

    plt.xlabel(xlabel)

    plt.ylabel(ylabel)

    plt.grid(
        alpha=0.30,
    )

    plt.tight_layout()




def save_figure(
    filename: str,
    category: str,
) -> None:
    """
    Save figure inside outputs/figures/<category>.
    """

    output_dir = (
        Path("outputs")
        / "figures"
        / category
    )

    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    plt.savefig(
        output_dir / filename,
        dpi=300,
        bbox_inches="tight",
    )




def display_plot() -> None:
    """
    Display current figure.
    """

    plt.show()