"""
Name: Katherine St. John
Email: katherine.stjohn@hunter.cuny.edu
Resources:  Used pandas documentation for stats functions.
"""

import pandas as pd
import re
import datetime


def make_housing_df(file_name):
    """
    Reads file_name into a df.
    If the 'total' is null, that row is dropped.
    The resulting DataFrame is returned.
    Rename the nta2010 to be NTA Code
    """

    df = pd.read_csv(file_name,low_memory=False)
    df = df[ df['total'].notnull() ]
    df = df.rename(columns={'nta2010' : 'NTA Code'})
    return df

def make_pop_df(file_name):
    """
    Reads file_name into a df, keeping only 2010 demographic information.
    The resulting DataFrame is returned.
    """
    df = pd.read_csv(file_name,low_memory=False)
    df = df[ df['Year'] == 2010 ]
    return df

def combine_df(housing_df, pop_df, cols):
    """
    Join on NTA Code, new dataframe should have only columns specified in cols
    """
    df = pd.merge(housing_df, pop_df,on='NTA Code')
    return df[cols]

def compute_density(df, col = 'Density'):
    """
    Add a new column
    Given a row containing columns 'Population' and 'Shape_Area',
    returns the population density (i.e. the population divided by the area)
    as a float.
    """
    df[col] = df['Population']/df['Shape__Area']
    return(df)

def most_corr(df, y = 'total', xes = ['Population','Shape__Area','Density','comp2010']):
    """
    Returns the column name from xes that has the highest absolute correlation
    with y (absolute value of Pearson's R )
    """
    best = ""
    best_r = 0
    for x in xes:
        r = abs(df[y].corr(df[x]))
        print(x,r)
        if r > best_r:
            best_r = r
            best = x
    return best,best_r

def convert_std_units(ser):
    """
    Takes a Series of numeric values and converts to standard units,
    that is, it computes the mean and standard deviation of ser, and for
    each s in ser, returns (s - mean)/(standard deviation)
    """
    return( (ser - ser.mean())/ser.std() )
