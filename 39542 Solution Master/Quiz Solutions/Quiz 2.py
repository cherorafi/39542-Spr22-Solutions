"""
One way to do the quiz question, checking to see if there
are any entries in Names by making sure the length of the
string is positive.

The overwriting of NumInParty with give a warning (discussed
in lecture and Chapter 6).  Second version of function avoids
this by using assign.
"""

def cleanReservations(df):
    # Write your code here
    df = df[ df['Names'].str.len() > 0 ]
    df['NumInParty'] = df['Names'].str.count(' ')+1
    return(df)

"""
Another way-- using the notnull() to select columns.  Also uses
assign to avoid the overwriting warnings.
"""

def cleanReservations2(df):
    # Write your code here
    df = df[ df['Names'].notnull() ]
    df = df.assign(NumInParty=df['Names'].str.count(' ')+1)
    return(df)
