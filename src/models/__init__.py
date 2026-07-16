"""
Machine Learning Models Package.
"""

from .evaluation import (
    evaluate_regression,
)

from .comparison import (
    compare_models,
    get_best_model,
    save_comparison,
)

from .persistence import (
    save_model,
    load_model,
)

from .utils import (
    summarize_dataset,
)
from .baseline import (
    train_baseline_model,
)

from .linear_regression import (
    train_linear_regression,
)

from .decision_tree import (
    train_decision_tree,
)

from .random_forest import (
    train_random_forest,
)

from .xgboost_model import (
    train_xgboost,
)

from .lightgbm_model import (
    train_lightgbm,
)

from .catboost_model import (
    train_catboost,
)

from .tuning import (
    tune_model,
)

__all__ = [
    "evaluate_regression",
    "compare_models",
    "save_model",
    "load_model",
    "summarize_dataset",
    "train_baseline_model",
    "train_linear_regression",
    "train_decision_tree",
    "train_random_forest",
    "train_xgboost",
    "train_lightgbm",
    "train_catboost",
    "tune_model",
    "get_best_model",
    "save_comparison",
]