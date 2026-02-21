# Data Science Portfolio

## Machine Learning
* **[Titanic Survival Prediction (Kaggle)](https://github.com/mattcw9090/data-science-portfolio/blob/main/titanic.ipynb)** — End-to-end binary classification project predicting passenger survival on the Titanic. Conducted exploratory data analysis to guide imputation and feature design, addressing skewed and imbalanced variables. Extensive feature engineering was performed, including title extraction from names, family and ticket group features, fare normalization, cabin/deck indicators, and age-based flags. Models were evaluated using stratified k-fold cross-validation with F1-score due to class imbalance. Logistic Regression and XGBoost models were tuned via GridSearchCV and RandomizedSearchCV, with XGBoost achieving the strongest cross-validated performance.

* **[Iris Species Classification](https://github.com/mattcw9090/data-science-portfolio/blob/main/iris_flower_classification.ipynb)** — Multiclass classification project using the Iris dataset. Baseline models (Logistic Regression, KNN, SVM, and Random Forest) were evaluated with 5-fold cross-validation and tuned via GridSearchCV. A tuned SVM achieved 96.7% test accuracy with balanced class performance.

* **[Linear Regression from Scratch (Gradient Descent)](https://github.com/mattcw9090/data-science-portfolio/blob/main/linear_regression_model_from_scratch.ipynb)** — Implemented linear regression from first principles using batch gradient descent and mean squared error (MSE) loss. The project derives the gradient analytically, handles intercept terms explicitly, and follows a scikit-learn–style API (`fit`, `predict`, `coef_`, `intercept_`). Emphasis is placed on understanding optimization dynamics rather than relying on closed-form solvers.

## Exploratory Data Analysis

* **[Student Placement Prediction Dataset 2026](https://github.com/mattcw9090/data-science-portfolio/blob/main/student_placement_eda.ipynb)** — Exploratory data analysis of student placement outcomes, examining key academic and skill-based factors associated with placement rates and salary packages among placed students.
