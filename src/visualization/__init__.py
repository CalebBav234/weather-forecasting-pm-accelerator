"""
Visualization package.
"""

from .distributions import (
    plot_histogram,
    plot_boxplot,
)

from .categorical import (
    plot_bar_chart,
)

from .correlation import (
    plot_correlation_heatmap,
    get_high_correlations,
)

from .geographic import (
    plot_scatter_map,
)
from .scatter import (
    plot_scatter,  
)  

__all__ = [
    "plot_histogram",
    "plot_boxplot",
    "plot_bar_chart",
    "plot_correlation_heatmap",
    "get_high_correlations",
    "plot_scatter",
    "plot_scatter_map",
]