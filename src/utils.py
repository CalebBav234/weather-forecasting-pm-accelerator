"""
utils.py

Reusable utility functions for the Weather Forecasting project.

These functions are intentionally generic and can be reused throughout
the project without introducing dependencies on specific ML models.

Author:
    Caleb Mario Baving Auza

Project:
    PM Accelerator - Advanced Weather Forecasting and Climate Analytics
"""

from __future__ import annotations

import random
from pathlib import Path

import numpy as np
import pandas as pd


def set_random_seed(seed: int) -> None:
    """
    Set random seeds for reproducibility.

    Parameters
    ----------
    seed : int
        Random seed value.
    """

    random.seed(seed)
    np.random.seed(seed)


def create_directory(directory: Path) -> None:
    """
    Create a directory if it does not already exist.

    Parameters
    ----------
    directory : Path
        Directory path.
    """

    directory.mkdir(parents=True, exist_ok=True)

def dataframe_memory_usage(df: pd.DataFrame) -> float:
    """
    Calculate the memory usage of a DataFrame.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    float
        Memory usage in megabytes.
    """

    memory = df.memory_usage(deep=True).sum()
    return memory / (1024 ** 2)


def load_dataframe(path: Path) -> pd.DataFrame:
    """
    Load a CSV dataset.

    Parameters
    ----------
    path : Path

    Returns
    -------
    pd.DataFrame

    Raises
    ------
    FileNotFoundError
        If the dataset does not exist.
    """

    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    return pd.read_csv(path)


def save_dataframe(
    df: pd.DataFrame,
    output_path: Path,
    index: bool = False,
) -> None:
    """
    Save a DataFrame to CSV.

    Parameters
    ----------
    df : pd.DataFrame

    output_path : Path

    index : bool
        Whether to save the index.
    """

    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path, index=index)



def print_section_header(title: str) -> None:
    """
    Print a formatted section header.

    Parameters
    ----------
    title : str
    """

    line = "=" * 70

    print()
    print(line)
    print(title.upper())
    print(line)