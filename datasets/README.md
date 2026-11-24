# Dataset provenance and usage

This directory records where the notebooks get their data. Downloaded, generated, and frequently updated files stay local and are ignored by Git. No source snapshot is checked in.

Third-party datasets retain their original licenses and terms. A source link here is not a grant of redistribution or commercial-use rights. Review the provider's current terms before reusing any data.

## Data catalog

| Project | Local asset or cache | Source and access method | Repository policy |
|---|---|---|---|
| Customer Churn Classification | KaggleHub cache | [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn), slug `blastchar/telco-customer-churn` | Downloaded on first run; not tracked |
| S&P 500 Return Analysis | `datasets/sp500_close_10y.csv` | Current constituents from [Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies); adjusted prices from Yahoo Finance through `yfinance` | Regenerable cache; ignored |
| Student Placement Analysis | KaggleHub cache | [Student Placement Prediction Dataset 2026](https://www.kaggle.com/datasets/sehaj1104/student-placement-prediction-dataset-2026), slug `sehaj1104/student-placement-prediction-dataset-2026` | Downloaded on first run; not tracked |

## Important limitations

- The market notebook applies the current S&P 500 membership to historical prices. That creates survivorship and membership bias and is not a historically investable universe.
- Yahoo Finance, Wikipedia, and Kaggle-hosted data can change. A fresh run may not reproduce an older snapshot byte for byte.
- The student-placement file is a synthetic dataset from its publisher. It is suitable for demonstrating analysis technique. It is not a basis for admissions, hiring, or compensation decisions.
