"""
Quiz 4b: Counting Weekend Trips
"""

def num_weekend_trips(df):
    #Group by Day, summing up lengths:
    df = df[ df['Day'] == 5 ]
    df = df[ df['Length'] == 2]
    return(len(df))
