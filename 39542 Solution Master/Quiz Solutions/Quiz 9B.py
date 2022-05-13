def fix_len(le):
    le = str(le)
    if 'hr' in le:
        x = le.find('hr')
        return(int(le[:x])*60+int(le[x+2:-3]))
    else:
        return int(le)

def clean_data(df):
    # Write your code here
    df['Year'] = df['Year'].fillna( df['Year'].median() ).astype(int)
    df['Rating'] = df['Rating'].fillna( 'NR' )
    df['Length'] = df['Length'].apply(fix_len)
    return(df)
