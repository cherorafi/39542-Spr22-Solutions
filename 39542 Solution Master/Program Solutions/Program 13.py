"""
Name:  Katherine St. John
Email: katherine.stjohn@hunter.cuny.edu
Resources: Using https://jakevdp.github.io/PythonDataScienceHandbook/ & OpenDataNYC
"""
import pandas as pd
import numpy as np
import pandasql as psql

def make_df(file_name):
    """
    :param file_name: the name of a CSV file containing 911 System Calls from OpenData NYC.
    :return: df with only ambulance calls.  Drops rows with null values for
    the type description, incident date, and latitue and longitude
    """
    df = pd.read_csv(file_name)
    #Drop rows with nulls in type description, incident date, and latitue and longitude
    df = df.dropna(subset=['TYP_DESC','INCIDENT_DATE','INCIDENT_TIME','BORO_NM'])
    return(df)


def select_boro_column(df):
    """
    Return the column BORO_NM from the table:
    SELECT BORO_NM
    FROM <insert data table name>
    """
    q = f'SELECT BORO_NM FROM df'
    return(psql.sqldf(q))

def select_by_boro(df, boro_name):
    """
    Return all rows for the dataset, where the borough is boro_name
    SELECT *
    FROM <insert data table name>
    WHERE BORO_NM = ‘Bronx’
    """
    q = f'SELECT * FROM df WHERE BORO_NM = "{boro_name.upper()}"'
    return(psql.sqldf(q))

def new_years_count(df, boro_name):
    """
    How many incidents were called in on New Year’s Day Jan 1, 2021, in the specified borough?
    SELECT COUNT(*)
    FROM <insert data table name>
    WHERE incident_date = ’01/01/2021’
    AND BORO_NM = ‘boro_name’
    """
    q = f'SELECT COUNT(*) FROM df WHERE incident_date = "01/01/2021" AND BORO_NM = "{boro_name.upper()}"'
    return(psql.sqldf(q))

def incident_counts(df):
    """
    How many incident counts per radio code (TYP_DESC), sorted alphabetically by radio code
    SELECT typ_desc, COUNT(*)
    FROM <insert data table name>
    GROUP BY 1
    ORDER BY 1
    """
    q = '''
    SELECT typ_desc, COUNT(*)
    FROM df
    GROUP BY 1
    ORDER BY 1
    '''
    return(psql.sqldf(q))

def top_10(df, boro_name):
    """
    Find the top 10 most commonly occurring incidence by radio code, and the number of incident occurrences, in specified borough.
    SELECT typ_desc, COUNT(*)
    FROM <insert data table name>
    WHERE BORO_NM = ‘boro_name’
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT 10
    """
    q = f'SELECT typ_desc, COUNT(*) FROM df WHERE BORO_NM = "{boro_name.upper()}" GROUP BY 1 ORDER BY 2 DESC LIMIT 10'
    return(psql.sqldf(q))
