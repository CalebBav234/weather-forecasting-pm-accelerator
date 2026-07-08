"""
Shared plotting utilities.

All visualizations should use the same style, figure size,
resolution, and saving behavior.
"""

from pathlib import Path

import matplotlib.pyplot as plt

DEFAULT_FIGSIZE = (12, 6)
DEFAULT_DPI = 300


def set_plot_style() -> None:
    """
    Configure a consistent plotting style for the project.
    """

    plt.style.use("ggplot")

    plt.rcParams["axes.titlesize"] = 16
    plt.rcParams["axes.labelsize"] = 13
    plt.rcParams["xtick.labelsize"] = 11
    plt.rcParams["ytick.labelsize"] = 11
    plt.rcParams["legend.fontsize"] = 11


def save_figure(
    filename: str,
    category: str,
) -> None:
    """
    Save the current matplotlib figure.
    """

    output_directory = (
        Path("outputs")
        / "figures"
        / category
    )

    output_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    plt.tight_layout()

    plt.savefig(
        output_directory / filename,
        dpi=DEFAULT_DPI,
        bbox_inches="tight",
    )