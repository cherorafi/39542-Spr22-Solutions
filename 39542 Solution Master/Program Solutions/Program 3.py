"""
Name: Katherine St. John
Email: katherine.stjohn@hunter.cuny.edu
Resources:  Used OpenDataNYC for data formats and pandas documentation for file args
"""
import pandas as pd

def make_insp_df(file_name):
    '''
    Takes the name of a CSV file of restaurant inspection data from
    data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/43nn-pn8j/data
    and returns a cleaned df.
    '''

    df = pd.read_csv(file_name)
    df = df[ ['CAMIS', 'DBA', 'BORO', 'BUILDING', 'STREET', 'ZIPCODE', 'SCORE', 'GRADE', 'NTA'] ]
    df = df[ df['SCORE'].notnull() ]
    return(df)

def predict_grade(num_violations):
    '''
    Takes the number of violations points and returns the letter grade.
    '''

    if num_violations <= 13:
        return 'A'
    elif num_violations <= 27:
        return 'B'
    else:
        return 'C'

def grade2num(grade):
    '''
    Takes the letter grade of A, B, C and returns its value on a 4.0 scale.
    Returns "" for all other values.
    '''
    if grade == "":
        return None
    elif grade == 'A':
        return 4.0
    elif grade == 'B':
        return 3.0
    elif grade == 'C':
        return 2.0
    else:
        return None

def compute_ave_grade(df, col):
    '''
    This function takes a df and groups on NTA and takes the average
    of the numeric values in col (i.e. mean(numeric_only=True)).
    Converts the groupby object into a df and returns the df.
    '''
    grouped = df.groupby('NTA')[col].mean(numeric_only=True)
    return(grouped.to_frame())

def make_nta_df(file_name):
    '''
    Takes the name of CSV file for Neighborhood Tabulation Areas and returns a
    DataFrame with the two columns:  NTACode and NTAName
    '''

    df = pd.read_csv(file_name)
    return(df[ ['NTACode','NTAName'] ])

def neighborhood_grades(ave_df,nta_df):
    '''
    This function takes a df containing NTACode and the nta_df containing
    NTA and returns the joins on these two columns, dropping both before returning.
    '''

    df = ave_df.merge(nta_df,left_on='NTA',right_on='NTACode')
    #return(df.drop(axis=1,columns = ['NTA','NTACode']))
    return(df)
