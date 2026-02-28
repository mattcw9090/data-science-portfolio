# Data Science Portfolio

## Deep Learning
* **[Cats vs Dogs Image Classification](https://github.com/mattcw9090/data-science-portfolio/blob/main/cats_vs_dogs_classification.ipynb)** — Binary image classification using a custom CNN built with TensorFlow/Keras. Implemented an end-to-end pipeline including data cleaning, train/validation splitting, `tf.data` input pipelines, regularization (dropout), and global average pooling. Evaluated using accuracy on a held-out validation set.

## Machine Learning
* **[Customer Churn Prediction](https://github.com/mattcw9090/data-science-portfolio/blob/main/customer_churn_predictor.ipynb)** — End-to-end churn classification pipeline using the Telco Customer Churn dataset. Cleaned and validated data types (including robust numeric conversion for `TotalCharges`), performed EDA, and built models with leakage-safe preprocessing and resampling using an imbalanced-learn pipeline (`SMOTE` inside CV). Compared multiple classifiers with stratified cross-validation and evaluated on a held-out test set using ROC-AUC, F1-score, precision/recall, and confusion matrices. Included model interpretation via feature importance/coefficients (where applicable) and saved the final trained pipeline for reuse.

* **[Twitter Sentiment Analysis (Sentiment140)](https://github.com/mattcw9090/data-science-portfolio/blob/main/sentiment_analysis.ipynb)** — Large-scale binary sentiment classification on 1.6M tweets using the Sentiment140 dataset. Built a reproducible end-to-end NLP pipeline with lightweight tweet preprocessing, TF–IDF feature extraction (unigrams + bigrams), and Logistic Regression. Evaluated performance using precision, recall, F1-score, and confusion matrices; conducted error analysis and interpreted model behavior via top weighted n-grams. Optimized for laptop-scale training with stratified sampling and saved the final sklearn pipeline for reuse.

* **[House Prices Prediction (Kaggle)](https://github.com/mattcw9090/data-science-portfolio/blob/main/house_prices.ipynb)** — Regression on the Ames Housing dataset with a log-transformed target. Evaluated linear, regularized, and tree-based models using 5-fold CV; ElasticNet and XGBoost performed best and were used for Kaggle submissions.

* **[Titanic Survival Prediction (Kaggle)](https://github.com/mattcw9090/data-science-portfolio/blob/main/titanic.ipynb)** — End-to-end binary classification project using EDA-driven feature engineering (titles, family and ticket groups, fare normalization, cabin indicators). Models were evaluated with stratified k-fold cross-validation using F1-score to address class imbalance. Logistic Regression and XGBoost were tuned via GridSearchCV and RandomizedSearchCV, with XGBoost performing best.

* **[Iris Species Classification](https://github.com/mattcw9090/data-science-portfolio/blob/main/iris_flower_classification.ipynb)** — Multiclass classification on the Iris dataset. Baseline models (Logistic Regression, KNN, SVM, Random Forest) were evaluated with 5-fold cross-validation, and a tuned SVM achieved 96.7% test accuracy with balanced class performance.

* **[Linear Regression from Scratch (Gradient Descent)](https://github.com/mattcw9090/data-science-portfolio/blob/main/linear_regression_model_from_scratch.ipynb)** — Implemented linear regression from first principles using batch gradient descent and MSE loss, deriving gradients analytically and following a scikit-learn–style API.

## Exploratory Data Analysis
* **[Student Placement Prediction Dataset 2026](https://github.com/mattcw9090/data-science-portfolio/blob/main/student_placement_eda.ipynb)** — Exploratory analysis of student placement outcomes, identifying academic and skill-based factors associated with placement rates and salary levels.
