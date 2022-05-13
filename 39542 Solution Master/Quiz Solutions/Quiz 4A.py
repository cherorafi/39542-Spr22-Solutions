"""
Quiz 4a:  Trip Times
"""

def clean_trips(df):
    #Drop all rows where the Start or End is blank.
    df = df[ df['Start'].notnull() ]
    df = df[ df['End'].notnull() ]
    #Convert the dates from strings to datetimes:
    starts = pd.to_datetime(df['Start'])
    ends = pd.to_datetime(df['End'])
    df['Start'] = starts
    df['End'] = ends
    #Adjust Length to be the length of the trip in days:
    df['Length'] = (df['End'] - df['Start']).dt.days
    #Adjust Day to be the day of the week for start:
    df['Day'] = df['Start'].dt.weekday
    return(df)
