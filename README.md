# Big Mart Sales Prediction using Machine Learning with Python

## Key Concepts:

- Supervised Learning: We'll be using supervised learning, specifically regression, as we have labeled data (sales figures) to predict future sales.
- Data Preprocessing: We'll cover essential data preprocessing steps, including handling missing values, encoding categorical variables, and feature engineering.
- Model Training: We'll train a machine learning model (XGBoost Regressor in this case) on the data to learn the relationship between features and sales.
- Model Evaluation: We'll evaluate the model's performance using metrics like R-squared and compare its predictions on training and testing data to assess overfitting.
  
## Project Steps:

* **Data Collection and Analysis**: Load the Big Mart sales dataset, explore the data, identify missing values and categorical features, and perform basic statistical analysis.
* **Data Preprocessing**: Handle missing values, encode categorical variables, and potentially create new features.
* **Model Selection and Training**: Choose a suitable regression model (XGBoost Regressor in this video) and train it on the prepared data.
* **Model Evaluation**: Evaluate the model's performance on both training and testing data using appropriate metrics.

### Further Exploration:

Experiment with different regression models (e.g., Linear Regression, Random Forest, Support Vector Regression).
Fine-tune model hyperparameters to improve performance.
Explore more advanced feature engineering techniques.

## run the setup tools

`.` stands for current folder.
```shell
pip install -e .
```
## streamlit run
use any one command to run the streamlit app:
```shell
python -m streamlit run main.py
streamlit run main.py
```