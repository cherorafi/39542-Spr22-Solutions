#10b:  make a dataset linearly separable by adding a third dimension
#df has columns: x,y,isyellow
#Find mean of yellow points, and then compute RBF based there.

import pandas as pd
import numpy as np

def transform(df):
    df_yell = df[ df['is_yellow'] > 0]
    mu_x = df_yell['x'].mean()
    mu_y = df_yell['y'].mean()
    df['x'] = df['x'] - mu_x
    df['y'] = df['y'] - mu_y
    df['z'] = np.exp(-(df['x']**2 + df['y']**2))
    return(df)
