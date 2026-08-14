# Matthew Chew — Data Science Portfolio

[![Portfolio checks](https://github.com/mattcw9090/data-science-portfolio/actions/workflows/portfolio-quality.yml/badge.svg)](https://github.com/mattcw9090/data-science-portfolio/actions/workflows/portfolio-quality.yml)

End-to-end projects across predictive modeling, financial analysis, natural language processing, recommender systems, and computer vision. The work emphasizes reproducible workflows, appropriate evaluation, and clear communication of results and limitations.

## Featured case studies

These notebooks are the best starting points because they include saved results and a clear analytical narrative.

| Project | Problem and approach | Saved result |
|---|---|---|
| **[Customer Churn Classification](customer_churn_predictor.ipynb)** | Leakage-aware preprocessing and resampling inside stratified cross-validation, followed by model comparison and holdout evaluation. | Logistic regression reached **0.846 mean CV ROC-AUC** and **78.6% churn recall** on the holdout set. |
| **[S&P 500 Return Analysis](stock_return.ipynb)** | Batched data acquisition, coverage checks, normalized performance, annualized risk/return, and correlation analysis. | Analyzed **456 equities across 2,513 trading sessions**; the average pairwise daily-return correlation was **0.327**. |
| **[Neural Network from Scratch](neural_network_from_scratch.ipynb)** | A fully connected regression network implemented in NumPy, including forward propagation, backpropagation, and mini-batch gradient descent. | Achieved **0.0229 validation MSE** on a nonlinear synthetic regression task. |
| **[House Price Regression](house_prices.ipynb)** | Mixed-type feature engineering and comparison of linear, regularized, ensemble, and boosting models. | XGBoost reached a notebook-reported **0.1244 five-fold CV RMSE** on the log-transformed target. |
| **[Student Placement Analysis](student_placement_eda.ipynb)** | Data-quality validation, distribution analysis, group comparisons, and correlation analysis across student outcomes. | Profiled **100,000 records**, including a **54.5% placement rate** and a **13.32 LPA** mean salary among placed students. |

## Project index

### Applied machine learning

- **[Customer Churn Classification](customer_churn_predictor.ipynb)** — Imbalanced classification with `ColumnTransformer`, in-fold random oversampling, multi-metric cross-validation, and holdout evaluation.
- **[House Price Regression](house_prices.ipynb)** — Feature engineering, ElasticNet, XGBoost, cross-validation, and prediction ensembling on mixed tabular data.
- **[Titanic Survival Classification](titanic.ipynb)** — EDA-driven passenger and group features, stratified evaluation, and tuned logistic regression/XGBoost models.
- **[Iris Species Classification](iris_flower_classification.ipynb)** — Multiclass baseline comparison, hyperparameter tuning, and final SVM evaluation.

### Financial and time-series analysis

- **[S&P 500 Return Analysis](stock_return.ipynb)** — Ten-year cross-sectional analysis of normalized prices, annualized return and volatility, and daily-return correlations.
- **[S&P 500 Next-Day Direction](stock_market_price_predictor.ipynb)** — Random-forest classification with lagged multi-horizon features and expanding-window backtesting.

### Natural language processing and recommendation

- **[Twitter Sentiment Analysis](sentiment_analysis.ipynb)** — TF–IDF unigram/bigram features, logistic regression, error analysis, and coefficient-based interpretation.
- **[Movie Recommendation Systems](recommendation_system.ipynb)** — Weighted popularity ranking, item-to-item correlation, and sparse cosine-neighbor retrieval.

### Deep learning and computer vision

- **[Neural Network from Scratch](neural_network_from_scratch.ipynb)** — A framework-free walkthrough of dense-network mathematics and implementation.
- **[Cats vs Dogs Classification](cats_vs_dogs_classification.ipynb)** — A TensorFlow `tf.data` image pipeline and custom convolutional neural network.
- **[Real-Time Face Verification](real_time_facial_recognition.ipynb)** — An experimental local prototype using OpenCV and a Siamese neural network; it requires a webcam and private reference images.

### Exploratory analysis and foundations

- **[Student Placement Analysis](student_placement_eda.ipynb)** — An executive-style EDA focused on data quality, placement outcomes, and salary associations.
- **[Linear Regression from Scratch](linear_regression_model_from_scratch.ipynb)** — A scikit-learn-style linear regressor trained with batch gradient descent.

## Skills demonstrated

| Capability | Evidence in this repository |
|---|---|
| Data analysis and communication | Pandas, NumPy, Seaborn, Matplotlib, executive summaries, and limitation-aware conclusions |
| Validation and model selection | Stratified cross-validation, holdout testing, hyperparameter search, and expanding-window backtesting |
| Feature engineering | Customer, housing, passenger, text, image, and market-derived features |
| Machine learning | Linear models, SVM, KNN, random forests, XGBoost, imbalanced classification, and regression |
| Deep learning | CNNs, Siamese networks, TensorFlow input pipelines, and backpropagation implemented from first principles |
| NLP and recommenders | TF–IDF text classification, weighted ranking, collaborative filtering, and sparse nearest neighbors |

## Repository layout

```text
.
├── *.ipynb               # One self-contained portfolio project per notebook
├── datasets/             # Small source datasets plus provenance documentation
├── portfolio_utils/      # Reusable preprocessing shared by notebooks
├── scripts/              # Lightweight repository validation
├── requirements.txt      # Shared Python 3.12 notebook environment
└── README.md              # Portfolio index and reviewer guide
```

The notebooks remain at the repository root so existing links and relative dataset paths stay stable.

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

Open a notebook and run its cells from top to bottom. Several projects download their data on first run through KaggleHub or `yfinance`; Kaggle-hosted datasets may require local Kaggle credentials. Hardware-dependent and long-running notebooks state their additional requirements near the top.

To run the fast repository checks without executing model training:

```bash
python scripts/validate_portfolio.py
```

## Data sources and limitations

- Dataset sources, local paths, access methods, and usage notes are documented in **[datasets/README.md](datasets/README.md)**.
- Downloaded datasets, model files, submissions, checkpoints, market-data caches, and private face images are intentionally excluded from version control.
- The S&P 500 analyses use the current constituent list across historical prices, so results are subject to survivorship and membership bias. They are analytical demonstrations, not investment advice.
- The face-verification notebook is a local learning prototype, not a production biometric system. Reference images should remain private and must not be committed.
- Third-party datasets retain their original licenses and terms; this repository does not grant additional rights to them.
