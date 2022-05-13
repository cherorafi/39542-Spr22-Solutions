def serFilm(g):
    if 'Drama' in g or 'Documentary' in g:
        return 1
    else:
        return 0

def clean_data(df):
    # Write your code here
    df['Serious Film'] = df['Genre'].apply(serFilm)
    df['Num Times'] = df['Times'].apply(lambda t: t.count(";")+1 )
    return(df)
