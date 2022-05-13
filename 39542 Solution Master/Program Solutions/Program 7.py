"""
Name: Katherine St. John
Email: katherine.stjohn@hunter.cuny.edu
Resources:  Used textbook for step functions and notation.
"""

import pandas as pd
import numpy as np


def make_df(housing_file, pop_file):
    """
    The data in the two files are read and merged into a single DataFrame
    using nta2010 and NTA Codes as the keys.
    If the 'total' is null or Year is not 2010, that row is dropped.
    The columns the_geom, boro and nta2010 are dropped,
    and the resulting DataFrame is returned.
    """

    hdf = pd.read_csv(housing_file,low_memory=False)
    hdf = hdf.rename(columns={'nta2010' : 'NTA Code'})
    pdf = pd.read_csv(pop_file,low_memory=False)
    df = pd.merge(hdf,pdf, on = "NTA Code")
    df = df[ df['total'].notnull() ]
    df = df[ df['Year'] == 2010 ]
    df = df.drop(columns = ["the_geom","boro"])
    return df

def compute_lin_reg(x,y):
    """
    This function takes two Series, and returns theta_0,theta_1 for their regression line, where theta_1 is the slope (r*(std of x)/(std of y)) and theta_0 is the y-intercept ( (ave of y) - theta_1*(ave of x)).
    """

    theta_1 = x.corr(y)*y.std()/x.std()
    theta_0 = y.mean() - theta_1*x.mean()
    return theta_0,theta_1

def compute_boro_lr(df,xcol,ycol,boro=["All"]):
    """
    Add in description
    """
    if boro != ["All"]:
        df = df[ df['Borough'].isin(boro) ]
    return compute_lin_reg(df[xcol],df[ycol])

def MSE_loss(y_actual,y_estimate):
    """
    Returns the mean squared error loss of the two series.
    """
    return( np.mean( (y_actual-y_estimate)**2 ) )

def linear_model(thetas,X):
    return X @ thetas

def RMSE(y_actual,y_estimate):
    """
    Returns the mean squared error loss of the two series.
    """
    return( np.sqrt( MSE_loss(y_actual,y_estimate) ))


def compute_error(y_actual,y_estimate,loss_fnc=MSE_loss):
    """
    Computes the error for the two series, using the specified loss_fnc.
    """
    return loss_fnc(y_actual,y_estimate)
