# Matthew Chew — Data Science Portfolio

[![Portfolio checks](https://github.com/mattcw9090/data-science-portfolio/actions/workflows/portfolio-quality.yml/badge.svg)](https://github.com/mattcw9090/data-science-portfolio/actions/workflows/portfolio-quality.yml)

Three case studies in imbalanced classification, cross-sectional market analysis, and tabular reporting. Each notebook states the question, the checks, the result, and the limits of that result.

Honours research is maintained separately in [honours-project](https://github.com/mattcw9090/honours-project).

## Featured case studies

| Project | Problem and approach | Saved result |
|---|---|---|
| **[Customer Churn Classification](projects/customer-churn/customer_churn_predictor.ipynb)** | Leakage-aware preprocessing and resampling inside stratified cross-validation, followed by model comparison and holdout evaluation. | Logistic regression reached **0.846 mean CV ROC-AUC** and **78.6% churn recall** on the holdout set. |
| **[S&P 500 Return Analysis](projects/sp500-return-analysis/sp500_return_analysis.ipynb)** | Batched data acquisition, coverage checks, normalized performance, annualized risk/return, and correlation analysis. | Analyzed **456 equities across 2,513 trading sessions**; the average pairwise daily-return correlation was **0.327**. |
| **[Student Placement Analysis](projects/student-placement-eda/student_placement_eda.ipynb)** | Validation, a written cleaning rule, pandas groupings, KPI tables, three charts, and a short correlation check on a 100,000-row placement file. | **54.5%** placed. Among placed students the mean package is **13.32 LPA** and the median is **13.30 LPA**. Branch rates sit between **54.1%** and **55.2%**. |

## Project index

### Classification

- **[Customer Churn Classification](projects/customer-churn/customer_churn_predictor.ipynb)** — Imbalanced classification with `ColumnTransformer`, in-fold random oversampling, multi-metric cross-validation, and holdout evaluation. Logistic regression is the model selected by CV ROC-AUC. The comparison also includes a majority-class dummy, random forest, k-nearest neighbors, and XGBoost.

### Market analysis

- **[S&P 500 Return Analysis](projects/sp500-return-analysis/sp500_return_analysis.ipynb)** — Ten-year cross-sectional analysis of normalized prices, annualized arithmetic return and volatility, and daily-return correlations. This is a descriptive study, not a predictive model.

### Reporting

- **[Student Placement Analysis](projects/student-placement-eda/student_placement_eda.ipynb)** — A reporting pass over a file the publisher describes as synthetic: data-quality checks, pandas groupings, an Excel-style pivot, three charts, and correlations for pay. Placement is **54.5%**; the median package among placed students is **13.30 LPA**.

## Skills demonstrated

| Capability | Evidence in this repository |
|---|---|
| Data analysis and communication | Pandas, NumPy, Seaborn, and Matplotlib, with written findings and limitation-aware conclusions |
| Validation and model selection | Stratified cross-validation, an untouched holdout, and resampling confined to each training fold |
| Tabular machine learning | Logistic regression, random forests, k-nearest neighbors, and XGBoost on an imbalanced classification task, with scaling and one-hot encoding inside the pipeline |
| Market data | Constituent lookup, batched price downloads, daily returns, annualized risk and return, and pairwise correlation |

## Repository layout

```text
.
├── projects/
│   ├── customer-churn/
│   │   └── customer_churn_predictor.ipynb
│   ├── sp500-return-analysis/
│   │   └── sp500_return_analysis.ipynb
│   └── student-placement-eda/
│       └── student_placement_eda.ipynb
├── datasets/              # Provenance notes; downloaded caches are ignored
├── artifacts/             # Ignored model output from the churn notebook
├── portfolio_utils/       # Shared repository paths
├── scripts/               # Lightweight repository validation
├── requirements.txt       # Shared Python 3.12 notebook environment
└── README.md              # Portfolio index and reviewer guide
```

Each project is one notebook. Shared path constants live in `portfolio_utils`, so a notebook can be launched from its project directory or from the repository root. Dataset provenance is centralized in [datasets/README.md](datasets/README.md). The churn notebook writes its selected pipeline under `artifacts/`, and that file is not committed.

## Reproduce the projects

```bash
git clone https://github.com/mattcw9090/data-science-portfolio.git
cd data-science-portfolio

python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
jupyter lab
```

Open a notebook under `projects/` and run its cells from top to bottom. Customer churn and student placement download their data on first run through KaggleHub; Kaggle-hosted datasets may require local Kaggle credentials. The S&P 500 notebook reads the current constituent table from Wikipedia and can download prices with `yfinance`. A local price cache is written to `datasets/sp500_close_10y.csv` and is gitignored.

The churn notebook includes a random-forest grid search. That cell can take a while.

To run the fast repository checks without executing model training:

```bash
python scripts/validate_portfolio.py
```

## Data sources and limitations

- Dataset sources, local paths, access methods, and usage notes are documented in **[datasets/README.md](datasets/README.md)**.
- Downloaded datasets, the market-data cache, and the saved churn pipeline are intentionally excluded from version control.
- The S&P 500 analysis uses the current constituent list across historical prices, so the panel has survivorship and membership bias. Annualized return is mean daily return multiplied by 252, not CAGR, and the return-to-risk ratio does not subtract a risk-free rate. The notebook is a descriptive study, not investment advice.
- The placement file is described by its publisher as synthetic. The notebook is a reporting exercise. It is not a basis for hiring or pay decisions, and the associations are not estimates of what would happen if a student's record changed.
- The churn holdout comes from the same source and time context. Random oversampling does not reproduce a live churn rate, and model choice is based on predictive metrics rather than the cost of a missed churner versus an unnecessary offer.
- Third-party datasets retain their original licenses and terms; this repository does not grant additional rights to them.
