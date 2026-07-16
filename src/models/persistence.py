"""
Model persistence utilities.

Provides reusable save/load functions
for trained models.
"""

from __future__ import annotations

from pathlib import Path

import joblib


def save_model(
    model,
    filepath: str,
) -> None:
    """
    Save trained model.
    """

    filepath = Path(filepath)

    filepath.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    joblib.dump(
        model,
        filepath,
    )


def load_model(
    filepath: str,
):
    """
    Load trained model.
    """

    return joblib.load(
        filepath
    )