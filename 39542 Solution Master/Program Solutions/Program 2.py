"""
Name: Katherine St. John
Email: katherine.stjohn@hunter.cuny.edu
Resources:  Used CSci 127 textbook for files and pandas documentation for keyword args
"""

import pandas as pd



def make_df(file_name):
    """
    Opens file_name and reads into a DataFrame, keeping only the columns:
    Summons Number,Plate ID,Registration State,Plate Type,Issue Date,Violation Code,Violation Time,
    Violation In Front Of Or Opposite,House Number,Street Name,Vehicle Color
    Return the resulting DataFrame.
    """

    df = pd.read_csv(file_name,low_memory=False)
    df = df[ ['Summons Number','Plate ID','Registration State','Plate Type',\
            'Issue Date','Violation Code','Violation Time',\
            'Violation In Front Of Or Opposite','House Number',\
            'Street Name','Vehicle Color'] ]
    return df


def filter_reg(df, keep = ["COM", "PAS"]):
    """
    This function takes two inputs:
    df: a DataFrame that including the Plate Type column.
    keep: a list of values for the Plate Type column. The default value is ["COM", "PAS"].
    The function returns the DataFrame with only rows that have Registration with a value from the list keep. All rows where the Registration column contains a different value are dropped.
    """

    return(df[ df['Plate Type'].isin(keep) ] )

def add_indicator(reg_state):
    """
    This function takes one input:
    reg_state: a string containing the state of registation.
    The function should return 1 when reg_state is in ["NY","NJ","CT"] and 0 otherwise.
    """

    if reg_state in ["NY","NJ","CT"]:
        return 1
    else:
        return 0

def find_tickets(df, plate_id):
    """
    This function takes two inputs:
    df: a DataFrame that including the Plate ID column.
    plate_id: a string containing a license plate (combination of letters, numbers and spaces).
    returns, as a list, the Violation Code for all tickets issued to that plate_id. If that plate_id has no tickets in the DataFrame, then an empty list is returned.
    """

    df_tick = df[ df['Plate ID'] == plate_id ]
    return( list( df_tick['Violation Code'] ) )

def make_dict(file_name, skip_rows = 1):
    """
    This function takes two inputs:
    file_name: a string containing the name of a file.
    skip_rows: the number of rows to skip at the beginning of file. The default value is 1.
    Make a dictionary from a text file named file_name, where each line, after those that are skipped, makes a dictionary entry. The key for each entry is the string upto the first comma (',') and the value is the string between the first and second commas. All characters after the second comma on a line are ignored.
    """

    dict = {}

    with open(file_name) as fd:
        #Read in skip_row lines before processing the rest of the file:
        for i in range(skip_rows):
            fd.readline()
        #Split up the remaining lines and add to dictionary:
        for line in fd:
            words = line.split(",")
            dict[words[0]] = words[1]
    return dict
