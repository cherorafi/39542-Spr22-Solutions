"""
Quiz 3b:  Return 'F' if more females, 'M' if more males
"""

def overallCount(df):
    f = df[ df['Sex'] == 'F' ].sum()
    m = df[ df['Sex'] == 'M' ].sum()
    if f > m:
        return('F')
    else:
        return('M')
