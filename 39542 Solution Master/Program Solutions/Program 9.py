"""
Name: Katherine St. John & Susan Sun
Email: katherine.stjohn@hunter.cuny.edu & susan.sun@hunter.cuny.edu
Resources:  sklearn documentation & http://www.textbook.ds100.org/ch/19/feature_engineering.html
"""

from typing import Union
import pandas as pd
import numpy as np
import pickle
import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
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


def add_boro(df, file_name) -> pd.DataFrame:
    """
    Add borough information for pickup & dropoff locations
    :param df: pandas dataframe, output of import_data()
    :param file_name:  name of file containing taxi_zone/boro info
    :return: pandas dataframe with additional columns for borough
    """
    boro_df = pd.read_csv(file_name)
    boro_df = boro_df[['LocationID', 'borough']]
    df = pd.merge(df,boro_df, how='left',left_on = 'PULocationID', right_on='LocationID')
    df = df.rename(columns={'borough' : 'PU_borough'})
    df = df.drop(columns=['LocationID'])
    df = pd.merge(df,boro_df, how='left',left_on = 'DOLocationID', right_on='LocationID')
    df = df.rename(columns={'borough' : 'DO_borough'})
    df = df.drop(columns=['LocationID'])
    return df

def crossing(row):
    if row['PU_borough'] == row['DO_borough']:
        return 0
    else:
        return 1

def add_flags(df) -> pd.DataFrame:
    """
    Add paid_tolls & cross_boro columns for those who paid tolls
    and trips started/ended in different borough
    :param df: pandas dataframe, output of import_data()
    :return: pandas dataframe with additional columns for borough
    """
    df['paid_toll'] = df['tolls_amount'].apply(lambda x : 0 if x > 0 else 1)
    df['cross_boro'] = df.apply(crossing,axis=1)
    return(df)

def encode_categorical_col(col,prefix) -> pd.DataFrame:
    """
    One hot encode categorical columns, remove last variable alphabetically, to get k-1 dummies out of k categorical levels
    :param df_cat_imputed: pandas dataframe, output of impute_categorical_cols()
    :return: pandas dataframe containing the one hot encoded categorical dataframe
    """
    df = pd.get_dummies(col, prefix_sep='',prefix=prefix)
    cols = sorted(df.columns)
    df = df[cols[:-1]]
    return df

def fit_logistic_regression(x_train, y_train,penalty='none',max_iter=1000):
    """
    :param x_train:
    :param y_train:
    :param penalty
    :return:
    """
    mod = LogisticRegression(solver='saga',penalty=penalty,max_iter=max_iter)
    mod.fit(x_train, y_train)
    pmod = pickle.dumps(mod)
    return pmod

def split_test_train(df, xes_col_names, y_col_name, test_size=0.25, random_state=12345):
    """
    :param df:
    :param y_col_name:
    :param df_cat_encoded:
    :param df_num_imputed:
    :param df_num_transformed:
    :param test_size:
    :param random_state:
    :return:
    """
    x_train, x_test, y_train, y_test = train_test_split(df[xes_col_names],
                                                        df[y_col_name],
                                                        test_size=test_size,
                                                        random_state=random_state)
    return x_train, x_test, y_train, y_test


def predict_using_trained_model(mod_pkl, x, y):
    """
    In testing code, run this twice!  to evaluate mse and r2 and see diff between
    apply to training dataset versus testing dataset
    :param mod:
    :param x:
    :param y:
    :return:
    """
    y_true = y
    mod = pickle.loads(mod_pkl)
    y_pred = mod.predict(x)
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return mse, r2
