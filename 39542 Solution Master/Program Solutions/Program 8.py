"""
Name: Susan Sun & Katherine St. John
Email: susan.sun@hunter.cuny.edu & katherine.stjohn@hunter.cuny.edu
Resources:  http://www.textbook.ds100.org/ch/19/feature_engineering.html
"""

import pandas as pd
import numpy as np
import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score


def import_data(file_name) -> pd.DataFrame:
    """
    Ingest raw data file as pandas DataFrame
    :param file_name: file containing OpenData NYC Yellow Taxi Data
    :return: DataFrame
    """
    df = pd.read_csv(file_name, low_memory=False)
    df = df[ df['total_amount'] > 0 ]
    return df

def add_tip_time_features(df) -> pd.DataFrame:
    """
    Add tip and time feature to the DataFrame
    :param df: df with Yellow Taxi Data
    :return: df with 3 additional columns:  percent_tip, duration, dayofweek
    """
    df['percent_tip'] = 100*df['tip_amount']/(df['total_amount']-df['tip_amount'])
    pickupT = pd.to_datetime(df['tpep_pickup_datetime'])
    dropoffT = pd.to_datetime(df['tpep_dropoff_datetime'])
    df['duration'] = (dropoffT - pickupT).dt.total_seconds()
    df['dayofweek'] = pickupT.dt.weekday
    return df


def impute_numeric_cols(df, x_num_cols) -> pd.DataFrame:
    """
    For numeric columns, impute missing data with the median
    :param df: pandas dataframe, output of import_data()
    :param x_num_cols: list of numerical X columns, output of application of split_columns_by_data_type()
    :return: pandas dataframe containing imputed numerical columns from input df
    """
    df_num = df[x_num_cols]
    df_num_imputed = df_num.fillna(df_num.median())
    return df_num_imputed

def transform_numeric_cols(df_num_imputed, degree_num=2,include_bias=False) -> pd.DataFrame:
    """
    :param df_num_imputed: df containing only numeric columns
    :param degree_num: degree used for PolynomialFeatures
    :return: a DataFrame with the transformed columns
    """
    poly_transform = PolynomialFeatures(degree=degree_num,include_bias=include_bias)
    df_num_transformed = poly_transform.fit_transform(df_num_imputed)
    return df_num_transformed

def fit_linear_regression(x_train, y_train):
    """
    :param x_train: an array of numeric columns with no null values.
    :param y_train: an array of numeric columns with no null values.
    :return: the intercept, the model coefficients, and model object
    """
    mod = LinearRegression()
    mod.fit(x_train, y_train)
    mod_intercept = mod.intercept_
    mod_coefficients = mod.coef_
    return mod_intercept, mod_coefficients, mod


def predict_using_trained_model(mod, x, y):
    """
    Predict and compare model outcomes for x with actual y
    :param mod: a trained model for the data.
    :param x:  an array or DataFrame of numeric columns with no null values.
    :param y:  an array or DataFrame of numeric columns with no null values.
    :return: the mean squared error and r2 score
    """
    y_true = y
    y_pred = mod.predict(x)
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return mse, r2
