import pandas as pd

def compute_lin_reg(df,threshold):
    """
    This function takes two Series, and returns theta_0,theta_1 for their regression line, where theta_1 is the slope (r*(std of x)/(std of y)) and theta_0 is the y-intercept ( (ave of y) - theta_1*(ave of x)).
    """
    df = df[ df['Population'] >= threshold]
    x = df['Population']
    y = df['total']
    theta_1 = x.corr(y)*y.std()/x.std()
    theta_0 = y.mean() - theta_1*x.mean()
    return theta_0,theta_1
