"""
Name:  Katherine St. John
Email: katherine.stjohn@hunter.cuny.edu
Resources: Using https://jakevdp.github.io/PythonDataScienceHandbook/ & OpenDataNYC
"""
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from scipy.stats import mode
from sklearn.metrics import accuracy_score


def make_df(file_name):
    """
    :param file_name: the name of a CSV file.
    :return: df with only ambulance calls.  Drops rows with null values for
    the type description, incident date, and latitue and longitude.
    """
    df = pd.read_csv(file_name)
    #Filter for ambulance in the name:
    df = df[ df['TYP_DESC'].str.contains('AMBULANCE') ]
    #Drop rows with nulls in type description, incident date, and latitue and longitude
    df = df.dropna(subset=['TYP_DESC','INCIDENT_DATE','INCIDENT_TIME','Latitude','Longitude'])
    return(df)

def add_date_time_features(df):
    """
    :param df: a DataFrame containing 911 System Calls.
    :return: df with columns for WEEK_DAY and INCIDENT_MIN
    """
    df['WEEK_DAY'] = pd.to_datetime(df['INCIDENT_DATE']).dt.dayofweek
    df['INCIDENT_MIN'] = ( pd.to_datetime(df['INCIDENT_TIME']) -pd.to_datetime("0:00:00") ).dt.total_seconds()/60
    return(df)

def filter_by_time(df,days=None,times=[0,1439]):
    """
    This function takes three inputs:
    :param df: a DataFrame containing 911 System Calls.
    :param days: a list of integers ranging from 0 to 6.
    :param times: a list of two non-negative integer values.
    :returns: a DataFrame with entries restricted to weekdays in days (or all weekdays if None is given) and incident times in times.
    """

    if days != None:
        df = df[ df['WEEK_DAY'].isin(days) ]
    df = df[ times[0] <= df['INCIDENT_MIN'] ]
    df = df[ df['INCIDENT_MIN'] <= times[1] ]
    return(df)

def compute_locations(df, num_clusters = 8, random_state = 2022):
    """
    :param df: a DataFrame containing 911 System Calls.
    :param num_clusters: a positive integer.
    :param random_state: an integer to seed the model.
    :return: the centers and labels, computed via KMeans on latitude and longitude.
    """
    kmeans = KMeans(n_clusters=num_clusters, random_state=random_state)
    kmeans.fit(df[ ['Latitude','Longitude'] ])
    y_kmeans = kmeans.predict(df[ ['Latitude','Longitude'] ])
    return kmeans.cluster_centers_, y_kmeans

def compute_explained_variance(df, K =[1,2,3,4,5], random_state = 55):
    """
    :param df: a DataFrame containing 911 System Calls.
    :param K: values for num_clusters in run of models.
    :param random_state: an integer to seed the model.
    :return: a list of the expected variance for each element in K.
    """
    exp_var = [ (KMeans(k,random_state=random_state).fit(df[ ['Latitude','Longitude'] ])).inertia_ for k in K]
    return exp_var
