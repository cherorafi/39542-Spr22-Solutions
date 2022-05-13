"""
Quiz 4:  Datetimes
"""

def countFemales(df):
    #Restrict to rows with 'F':
    df = df[ df['Sex'] == 'F' ]
    #Group by year:
    grouped = df.groupby('Year')['Count'].sum()
    return( grouped.to_frame() )
