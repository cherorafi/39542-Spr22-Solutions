import pandas as pd

def MAE_loss(y_actual, y_estimate):
    return ((y_actual-y_estimate).abs()).mean()

def compute_loss(y_actual, y_estimate,loss_fnc):
    return loss_fnc(y_actual,y_estimate)
