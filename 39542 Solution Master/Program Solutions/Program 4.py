"""
Name: Katherine St. John
Email: katherine.stjohn@hunter.cuny.edu
Resources:  Used pandas documentation for groupby args.
"""

import pandas as pd
import re
import datetime


def make_insp_df(file_name):
    """
    Reads file_name into a df, keeping only:
    'CAMIS', 'DBA', 'BORO', 'PHONE', 'CUISINE DESCRIPTION', 'INSPECTION DATE', 'RECORD DATE', 'GRADE'</code></pre>
    If the 'GRADE' is null, that row is dropped.
    The resulting DataFrame is returned.
    """

    df = pd.read_csv(file_name,low_memory=False)
    df = df[ ['CAMIS', 'DBA', 'BORO', 'PHONE', 'CUISINE DESCRIPTION', 'INSPECTION DATE', 'RECORD DATE', 'GRADE'] ]
    df = df[ df['GRADE'].notnull() ]
    return df

def clean_phone(phone_str):
    """
    Takes a string returns (NNN)-NNN-NNNN if the string contains 10 digits, else returns None
    """
    if re.search(r'[0-9]{10}',phone_str):
        s = f'({phone_str[:3]})-{phone_str[3:6]}-{phone_str[6:]}'
        return s
    else:
        return None

def convert_dates(df):
    """
    Converts the columns, 'INSPECTION DATE' and 'RECORD DATE' into datetime objects, using the format string 'MM/DD/YYYY'.
    Returns the resulting DataFrame
    """
    date_format = "%m/%d/%Y"
    insp_dates = pd.to_datetime(df['INSPECTION DATE'], format=date_format)
    grade_dates = pd.to_datetime(df['RECORD DATE'], format=date_format)
    df['INSPECTION DATE'] = insp_dates
    df['RECORD DATE'] = grade_dates
    return df

def insp_day_of_week(insp):
    """
    Takes the inspection date and returns the number corresponding to the day of the week of the inspection: 0 for Monday, 1 for Tuesday, ... 6 for Sunday. If the date is January 1, 1900, then the establishment has not yet had an inspection, and your function should return None.
    """

    sentinel = datetime.datetime(1900,1,1)
    if insp - sentinel == 0:
        return None
    else:
        return insp.weekday()

def days_since(insp_date, report_date):
    """
    Returns the number of days between insp_date & report_date if both are nonnull and insp_date not January 1, 1900.
    """
    if insp_date != None and report_date != None:
        sentinel = datetime.datetime(1900,1,1)
        if insp_date - sentinel == 0:
            return None
        else:
            return (report_date-insp_date).days
    else:
        return None

def group_df(df,categories=['INSP DAY','BORO']):
    """
    Returns a df with category and the average of values for each category
    """
    grouped = df.groupby(categories).size()
    return(grouped.to_frame())
