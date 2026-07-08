"""
Smoke tests for the visualization package.

Verifies that all reusable plotting utilities execute successfully
and save figures to the expected output directories.
"""

from pathlib import Path
import sys

# ---------------------------------------------------------------------
# Project Root
# ---------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# ---------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------

from src.data_loader import load_weather_dataset
from src.preprocessing import preprocess_dataset

from src.visualization.distributions import (
    plot_histogram,
    plot_boxplot,
)

from src.visualization.categorical import (
    plot_bar_chart,
)

from src.visualization.correlation import (
    plot_correlation_heatmap,
    get_high_correlations,
)

# ---------------------------------------------------------------------
# Load Dataset
# ---------------------------------------------------------------------

print("=" * 70)
print("Loading dataset...")
print("=" * 70)

df = preprocess_dataset(
    load_weather_dataset()
)

print(f"Dataset Shape: {df.shape}")

print()

# ---------------------------------------------------------------------
# Histogram
# ---------------------------------------------------------------------

print("=" * 70)
print("Testing Histogram...")
print("=" * 70)

plot_histogram(
    df=df,
    column="temperature_celsius",
    title="Temperature Distribution",
    xlabel="Temperature (°C)",
    filename="temperature_histogram.png",
)

print("✓ Histogram Passed\n")

# ---------------------------------------------------------------------
# Boxplot
# ---------------------------------------------------------------------

print("=" * 70)
print("Testing Boxplot...")
print("=" * 70)

plot_boxplot(
    df=df,
    column="temperature_celsius",
    title="Temperature Boxplot",
    xlabel="Temperature (°C)",
    filename="temperature_boxplot.png",
)

print("✓ Boxplot Passed\n")

# ---------------------------------------------------------------------
# Bar Chart
# ---------------------------------------------------------------------

print("=" * 70)
print("Testing Bar Chart...")
print("=" * 70)

country_counts = (
    df["country"]
      .value_counts()
      .head(10)
)

plot_bar_chart(
    data=country_counts,
    title="Top 10 Countries",
    xlabel="Country",
    ylabel="Observations",
    filename="top_countries.png",
)

print("✓ Bar Chart Passed\n")

# ---------------------------------------------------------------------
# Correlation Heatmap
# ---------------------------------------------------------------------

print("=" * 70)
print("Testing Correlation Heatmap...")
print("=" * 70)

plot_correlation_heatmap(
    df=df,
    title="Weather Feature Correlation Matrix",
    filename="correlation_heatmap.png",
)

print("✓ Heatmap Passed\n")

# ---------------------------------------------------------------------
# High Correlations
# ---------------------------------------------------------------------

print("=" * 70)
print("Testing Correlation Table...")
print("=" * 70)

high_corr = get_high_correlations(
    df,
    threshold=0.90,
)

print(high_corr.head(20))

print()

print("✓ Correlation Table Passed")

# ---------------------------------------------------------------------
# Verify Files
# ---------------------------------------------------------------------

print()
print("=" * 70)
print("Checking Output Files...")
print("=" * 70)

expected_files = [
    Path("outputs/figures/distributions/temperature_histogram.png"),
    Path("outputs/figures/distributions/temperature_boxplot.png"),
    Path("outputs/figures/categorical/top_countries.png"),
    Path("outputs/figures/correlation/correlation_heatmap.png"),
]

missing = False

for file in expected_files:

    if file.exists():
        print(f"✓ {file}")

    else:
        missing = True
        print(f"✗ Missing: {file}")

print()

if missing:

    print("Some visualization outputs were not generated.")

else:

    print("All visualization tests passed successfully.")

print("=" * 70)