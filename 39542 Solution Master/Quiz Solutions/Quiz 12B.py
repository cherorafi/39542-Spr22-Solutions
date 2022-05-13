"""
Name:  Katherine St. John
Email: katherine.stjohn@hunter.cuny.edu
Resources: Using https://jakevdp.github.io/PythonDataScienceHandbook/ & OpenDataNYC
"""
import pandas as pd
import numpy as np

def filter_adventure(df):
    # Write your code here
    df = df.dropna()
    df = df[ df['Genre'].str.contains('Adventure') ]
    return(df)
