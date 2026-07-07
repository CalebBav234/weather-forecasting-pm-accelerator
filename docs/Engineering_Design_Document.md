# Engineering Design Document
## Advanced Weather Forecasting and Climate Analytics Platform
### PM Accelerator Data Scientist Technical Assessment

**Version:** 1.0

**Author:** Caleb Mario Baving Auza

**Date:** July 2026

---

# Executive Summary

## Purpose

This document defines the engineering architecture, software design principles, implementation strategy, and technical standards for the Advanced Weather Forecasting and Climate Analytics Platform developed as part of the PM Accelerator Data Scientist Technical Assessment.

The objective of this project is not only to satisfy the assessment requirements but to demonstrate the engineering mindset expected from a modern Data Scientist. The repository will be designed using modular software engineering principles, reproducible machine learning workflows, comprehensive documentation, and production-inspired project organization.

Rather than building a collection of independent notebooks, this project will follow a layered architecture where each component has a clearly defined responsibility. Data ingestion, preprocessing, feature engineering, forecasting, evaluation, explainability, and visualization will all exist as separate modules that interact through well-defined interfaces.

This approach improves maintainability, reproducibility, extensibility, and readability while reflecting industry best practices commonly found in production machine learning systems.

---

# Project Objectives

The project has six primary objectives.

## 1. Build a Robust Data Engineering Pipeline

Develop a reproducible preprocessing pipeline capable of:

- Validating incoming data
- Handling missing values
- Removing duplicate observations
- Correcting inconsistent data types
- Detecting invalid measurements
- Preparing clean datasets for downstream analysis

The preprocessing workflow must be deterministic, modular, and reusable.

---

## 2. Perform Advanced Exploratory Data Analysis

Conduct comprehensive exploratory analysis to understand:

- Distribution of weather variables
- Relationships between atmospheric measurements
- Seasonal patterns
- Geographic variation
- Climate trends
- Air quality indicators
- Correlation structures
- Missing data patterns
- Statistical summaries

Visualizations should provide meaningful insights rather than simply describing the data.

---

## 3. Develop Multiple Forecasting Models

Implement multiple forecasting approaches suitable for time-series prediction.

Candidate models include:

- Baseline forecasting methods
- ARIMA
- SARIMA (if seasonality is identified)
- Prophet (where appropriate)
- Gradient Boosting models using engineered temporal features
- LSTM (if justified by the characteristics of the dataset)

Rather than selecting models based solely on popularity, model selection will be guided by empirical evaluation, forecasting accuracy, computational efficiency, and interpretability.

---

## 4. Create an Ensemble Forecasting Strategy

Compare individual forecasting models using appropriate time-series evaluation techniques.

If supported by validation results, combine the strongest-performing models into an ensemble forecasting framework designed to improve predictive performance and robustness.

The ensemble strategy will be selected based on quantitative evidence rather than assumptions.

---

## 5. Build an Interactive Analytics Dashboard

Develop a Streamlit dashboard enabling users to:

- Explore historical weather observations
- Visualize forecasting results
- Analyze climate trends
- Investigate air quality metrics
- Compare forecasting models
- Review feature importance
- Explore geographic patterns through interactive visualizations

The dashboard should provide an intuitive interface suitable for technical and non-technical audiences.

---

## 6. Demonstrate Professional Software Engineering Practices

The project should resemble a simplified production machine learning system rather than a traditional academic notebook.

Key characteristics include:

- Modular architecture
- Reusable Python modules
- Configuration-driven execution
- Version control using Git
- Comprehensive documentation
- Consistent coding standards
- Automated testing where appropriate
- Reproducible experiments

---

# Assessment Success Criteria

The project will be considered successful if it satisfies the following objectives.

## Data Engineering

- Missing values are appropriately handled.
- Duplicate observations are removed.
- Invalid values are detected.
- Data types are validated.
- Data quality checks are reproducible.
- Preprocessing is modular and reusable.

---

## Exploratory Data Analysis

Perform comprehensive exploratory analysis including:

- Statistical summaries
- Distribution analysis
- Correlation analysis
- Missing value visualization
- Seasonal trend analysis
- Geographic comparisons
- Climate analysis
- Air quality analysis
- Outlier analysis

Visualizations should answer meaningful analytical questions.

---

## Machine Learning

Develop a rigorous forecasting framework by:

- Establishing baseline forecasting performance.
- Implementing multiple forecasting approaches.
- Comparing model performance using time-series validation.
- Optimizing hyperparameters where appropriate.
- Evaluating residual behavior.
- Explaining model predictions.
- Constructing an ensemble model if supported by evaluation results.

Forecasting decisions should always be supported by empirical evidence.

---

## Software Engineering

The repository should demonstrate:

- Clean architecture
- Modular implementation
- Separation of concerns
- Reusable code
- Comprehensive documentation
- Logging
- Error handling
- Configuration management
- Professional Git history

---

## Final Deliverables

The completed project will include:

- Public GitHub Repository
- Engineering Design Document
- Technical Report
- Interactive Streamlit Dashboard
- Forecasting Pipeline
- Exploratory Analysis
- Feature Engineering Pipeline
- Explainability Analysis
- Presentation Slides
- Demonstration Video

---

# Project Philosophy

This project follows three guiding principles.

## Technical Excellence

Every engineering decision should be supported by technical reasoning.

Algorithms will be selected because they are appropriate for the problem rather than because they are popular.

Model complexity should only be introduced when justified by measurable improvements.

---

## Maintainability

Code should be easy to understand, modify, test, and extend.

Modules should have clearly defined responsibilities.

Reusable components should minimize duplication throughout the repository.

Future contributors should be able to navigate the project with minimal onboarding.

---

## Scientific Rigor

Analytical conclusions should be evidence-based.

Forecasting models should be evaluated using proper time-series validation procedures.

Performance claims should be supported by quantitative metrics rather than visual inspection alone.

Statistical assumptions should be verified whenever possible.

---

# Project Scope

The project intentionally extends beyond the minimum assessment requirements by incorporating production-inspired software engineering practices.

Additional capabilities include:

- Modular preprocessing pipeline
- Automated data validation
- Advanced feature engineering
- Multiple anomaly detection techniques
- Explainable machine learning
- Interactive dashboard
- Reproducible experimentation
- Professional project organization
- Comprehensive technical documentation

These enhancements are intended to demonstrate engineering maturity while remaining directly relevant to the assessment objectives.

---

# Engineering Principles

Every implementation throughout this project will follow the following principles.

1. Readability is more important than cleverness.
2. Simplicity is preferred over unnecessary complexity.
3. Reproducibility takes precedence over convenience.
4. Modular architecture is preferred over monolithic notebooks.
5. Configuration should replace hardcoded values whenever possible.
6. Every function should have a single, well-defined responsibility.
7. Code should be documented sufficiently to support future maintenance.
8. Machine learning decisions should be justified using empirical evaluation.
9. Visualizations should communicate insights rather than decorate reports.
10. Every deliverable should be suitable for presentation during a technical interview.

---

# Expected Outcomes

Upon completion, this project will demonstrate competencies in:

- Data Engineering
- Exploratory Data Analysis
- Feature Engineering
- Time-Series Forecasting
- Ensemble Machine Learning
- Explainable Artificial Intelligence
- Data Visualization
- Dashboard Development
- Software Engineering
- Version Control
- Technical Communication

The final repository should resemble a professional machine learning project that is maintainable, reproducible, and interview-ready while exceeding the expectations of the PM Accelerator Advanced Data Scientist Technical Assessment.

---

**End of Part 1**
# Part 2 — System Architecture & Repository Design

---

# System Overview

## Architectural Vision

The Advanced Weather Forecasting and Climate Analytics Platform is designed as a modular, production-inspired machine learning system. Rather than relying on a single notebook containing every step of the analysis, the project separates responsibilities into reusable Python modules, ensuring that each component has a single, well-defined purpose.

The architecture follows a layered workflow beginning with raw data ingestion and ending with an interactive analytics dashboard and reproducible deliverables. Every layer depends only on the outputs of the previous layer, minimizing coupling and making the system easier to test, maintain, and extend.

---

# High-Level Data Flow

```text
                    Kaggle Weather Dataset
                              │
                              ▼
                    Data Validation Layer
                              │
                              ▼
                    Data Cleaning Layer
                              │
                              ▼
                Feature Engineering Layer
                              │
                              ▼
             Exploratory Data Analysis Layer
                              │
                              ▼
               Forecasting & Modeling Layer
                              │
                              ▼
              Model Evaluation & Backtesting
                              │
                              ▼
            Explainability & Feature Analysis
                              │
                              ▼
               Streamlit Dashboard & Reports
                              │
                              ▼
                GitHub Repository Deliverables
```

---

# Layer Responsibilities

## Layer 1 — Data Validation

Purpose:

Verify that the raw dataset satisfies basic quality requirements before any transformations occur.

Responsibilities:

- Validate schema
- Validate column names
- Detect missing columns
- Verify data types
- Detect duplicate observations
- Detect impossible values
- Generate validation summary

Output:

Validated raw dataframe.

---

## Layer 2 — Data Cleaning

Purpose:

Prepare reliable data for analysis.

Responsibilities:

- Handle missing values
- Remove duplicates
- Correct data types
- Standardize categorical values
- Handle invalid observations
- Remove unnecessary columns (if justified)

Output:

Clean dataframe.

---

## Layer 3 — Feature Engineering

Purpose:

Transform cleaned observations into informative predictive features.

Planned feature groups:

### Temporal Features

- Hour
- Day
- Week
- Month
- Quarter
- Year
- Weekend indicator

---

### Cyclical Features

Encode:

- Hour
- Month
- Day of year

using sine/cosine transformations.

---

### Rolling Statistics

Examples:

- Rolling temperature mean
- Rolling humidity average
- Rolling pressure trend

---

### Lag Features

Examples:

Temperature(t-1)

Temperature(t-3)

Temperature(t-6)

Temperature(t-24)

Humidity lags

Pressure lags

---

### Interaction Features

Examples:

Temperature × Humidity

Wind × Pressure

Humidity × Dew Point

---

Output:

Model-ready dataset.

---

## Layer 4 — Exploratory Data Analysis

Purpose:

Understand the dataset before modeling.

Questions answered:

- Which variables are most correlated?
- Are seasonal patterns visible?
- Which countries exhibit different climates?
- Are air quality indicators related to weather variables?
- Which variables contain outliers?
- Which variables change over time?

Deliverables:

- Heatmaps
- Correlation matrices
- Histograms
- Geographic visualizations
- Trend plots
- Boxplots
- Pairplots (where appropriate)

---

## Layer 5 — Forecasting

Purpose:

Predict future weather variables.

Candidate models:

- Baseline Forecast
- ARIMA
- SARIMA
- Prophet
- XGBoost
- LightGBM
- CatBoost
- LSTM (if justified)

Final models will be selected based on objective evaluation rather than preference.

---

## Layer 6 — Evaluation

Responsibilities:

- Time-series cross-validation
- Residual analysis
- Error metrics
- Forecast comparison
- Statistical interpretation

Primary metrics:

- RMSE
- MAE
- MAPE
- R² (where appropriate)

---

## Layer 7 — Explainability

Purpose:

Explain why models make predictions.

Methods:

- SHAP values
- Feature importance
- Partial dependence plots (if appropriate)

Deliverables:

- Global explanations
- Local explanations
- Feature ranking

---

## Layer 8 — Dashboard

Purpose:

Provide an interactive interface for exploring the project.

Planned sections:

- Dataset Overview
- Exploratory Analysis
- Climate Trends
- Air Quality
- Forecast Results
- Model Comparison
- Explainability
- About the Project

---

# Repository Architecture

The repository follows a modular structure where each directory has a clearly defined responsibility.

## src/

Contains reusable Python modules.

No exploratory code should exist here.

---

## notebooks/

Contains exploratory notebooks only.

Responsibilities:

- Data exploration
- Visualization
- Experimentation

No production logic should be duplicated here.

---

## data/

Contains:

Raw data

Processed data

External resources

The raw dataset should never be modified directly.

---

## models/

Stores trained model artifacts when appropriate.

Large files should not be committed unless explicitly required.

---

## outputs/

Stores generated results.

Examples:

- Figures
- Metrics
- Predictions
- Logs

Outputs should be reproducible.

---

## docs/

Contains documentation.

Examples:

- Engineering Design Document
- Technical Report
- Presentation
- Architecture diagrams

---

## dashboard/

Contains the Streamlit application.

---

## tests/

Contains automated tests.

Every reusable module should eventually have corresponding tests.

---

# Module Responsibilities

Each Python module has one primary responsibility.

## config.py

Stores configurable project parameters.

Examples:

Random seed

Target variable

Forecast horizon

Feature flags

---

## paths.py

Centralizes filesystem paths.

No hardcoded paths elsewhere.

---

## constants.py

Stores constant values shared across the project.

Examples:

Column names

Metric names

Default settings

---

## utils.py

Reusable helper functions.

Must remain generic.

No forecasting logic.

---

## preprocessing.py

Responsible ONLY for:

- Cleaning
- Validation
- Missing values
- Duplicates
- Data types

No feature engineering.

---

## feature_engineering.py

Responsible ONLY for creating predictive features.

Must never perform cleaning.

---

## visualization.py

Generates reusable visualizations.

Should not modify datasets.

---

## forecasting.py

Responsible for training forecasting models.

No visualization logic.

---

## evaluation.py

Responsible for performance metrics and model comparison.

---

## ensemble.py

Combines forecasting models.

No preprocessing.

---

## dashboard.py

Interfaces with Streamlit.

Should not train models.

---

# Module Dependency Rules

Allowed flow:

```
config

↓

paths

↓

preprocessing

↓

feature_engineering

↓

forecasting

↓

evaluation

↓

dashboard
```

Forbidden dependencies:

- Dashboard importing preprocessing logic.
- Forecasting importing dashboard code.
- Visualization modifying datasets.
- Utilities importing forecasting modules.

Dependencies should always point forward through the pipeline.

---

# Configuration Strategy

Configuration should be centralized.

Avoid hardcoded values.

Every configurable parameter should exist in:

config.py

Future changes should require modifying configuration rather than implementation.

---

# Logging Strategy

Every major pipeline stage should produce informative logs.

Suggested logging levels:

INFO

WARNING

ERROR

Logging should capture:

- Pipeline execution
- Data validation results
- Model training
- Evaluation summaries
- Errors

---

# Design Principles

The project follows the following engineering principles:

- Single Responsibility Principle
- Separation of Concerns
- DRY (Don't Repeat Yourself)
- KISS (Keep It Simple)
- Reproducibility First
- Configuration Over Hardcoding
- Explicit Is Better Than Implicit

---

# End of Part 2