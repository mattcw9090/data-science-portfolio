# Dataset provenance and usage

This directory contains a small number of source snapshots used by the notebooks. Larger, frequently updated, generated, or private datasets are downloaded or created locally and ignored by Git.

Third-party datasets retain their original licenses and terms. Inclusion of a source link here is not a grant of redistribution or commercial-use rights; review the provider's current terms before reusing any data.

## Data catalog

| Project | Local asset or cache | Source and access method | Repository policy |
|---|---|---|---|
| Cats vs Dogs Classification | KaggleHub cache | [Microsoft Cats vs Dogs](https://www.kaggle.com/datasets/shaunthesheep/microsoft-catsvsdogs-dataset), slug `shaunthesheep/microsoft-catsvsdogs-dataset` | Downloaded on first run; not tracked |
| Customer Churn Classification | KaggleHub cache | [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn), slug `blastchar/telco-customer-churn` | Downloaded on first run; not tracked |
| Face Verification | `datasets/facial-recognition/` plus KaggleHub cache | [LFW Dataset](https://www.kaggle.com/datasets/jessicali9530/lfw-dataset), slug `jessicali9530/lfw-dataset`; user-captured reference images | Downloaded/generated locally; all biometric images are private and ignored |
| House Price Regression | `datasets/house-prices/train.csv`, `test.csv` | [Kaggle House Prices competition](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data) | Small competition snapshot tracked; Kaggle terms apply |
| Iris Classification | Bundled by scikit-learn | [`sklearn.datasets.load_iris`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html), originally from the UCI Iris dataset | Loaded from the installed package; no local copy |
| Movie Recommendation Systems | `datasets/.cache/ml-100k.zip` and extracted `datasets/movie-lens-dataset-100k/` | [MovieLens 100K](https://grouplens.org/datasets/movielens/100k/) from GroupLens; TMDB metadata via KaggleHub slug `tmdb/tmdb-movie-metadata` | Downloaded from the providers on first run; caches are ignored |
| S&P 500 Return Analysis | `datasets/sp500_close_10y.csv` | Current constituents from [Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies); adjusted prices from Yahoo Finance through `yfinance` | Regenerable cache; ignored |
| S&P 500 Next-Day Direction | `sp500.csv` | Historical `^GSPC` index data from Yahoo Finance through `yfinance` | Regenerable cache; ignored |
| Sentiment Analysis | KaggleHub cache | [Sentiment140](https://www.kaggle.com/datasets/kazanova/sentiment140), slug `kazanova/sentiment140` | Downloaded on first run; not tracked |
| Student Placement Analysis | KaggleHub cache | [Student Placement Prediction Dataset 2026](https://www.kaggle.com/datasets/sehaj1104/student-placement-prediction-dataset-2026), slug `sehaj1104/student-placement-prediction-dataset-2026` | Downloaded on first run; not tracked |
| Titanic Survival Classification | `datasets/titanic/train.csv`, `test.csv` | [Kaggle Titanic competition](https://www.kaggle.com/competitions/titanic/data) | Small competition snapshot tracked; Kaggle terms apply |

## Tracked snapshot checksums

These SHA-256 checksums make the small checked-in competition files auditable:

```text
1e18addf81e5e4d347cc17ee6075bbe4a42b7fa26b9e5b063e8f692a5f929d41  house-prices/train.csv
8fdd3d829d4d986b58f845c9553b225e67dd8383624d90fb6ca1d4bed5798c1e  house-prices/test.csv
4a437fde05fe5264e1701a7387ac6fb75393772ba38bb2c9c566405af5af4bd7  titanic/train.csv
5c78320a80dc159b35c408363be46a5d93f078183d539db75ee42a796d6a4e95  titanic/test.csv
```

## Important limitations

- MovieLens 100K requires acknowledgement and carries provider-specific restrictions. The archive is fetched from GroupLens at runtime instead of being redistributed in this repository. See the source README before use.
- The financial notebooks use the current S&P 500 membership across historical prices. This creates survivorship and membership bias and should not be interpreted as a historically investable universe.
- Yahoo Finance, Wikipedia, and Kaggle-hosted data can change. A fresh run may not reproduce an older market snapshot byte-for-byte.
- The student-placement data is appropriate for demonstrating analysis technique, not for making real admissions, hiring, or compensation decisions.
- Face images and trained biometric artifacts must remain local. Do not commit identifiable images, embeddings, checkpoints, or model files.
