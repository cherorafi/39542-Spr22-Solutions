"""
Name: Katherine St. John
Email: katherine.stjohn@hunter.cuny.edu
Resources:  http://www.textbook.ds100.org/ch/19/feature_engineering.html
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import pickle
from sklearn import datasets,metrics
from sklearn.decomposition import PCA
#digits = datasets.load_digits()



def select_data(data, target, labels = [0,1]):
    """
    :param data: a numpy array that includes rows of equal size flattened arrays,
    :param target: a numpy array that contains the labels for each row in data.
    :param labels: the labels from target that the rows to be selected.  The default value is [0,1].
    :return: the rows of data and target where the value of target is in labels.
    """
    selected = [(d,t) for (d,t) in zip(data,target) if t in labels]
    d_sel,t_sel = zip(*selected)
    return d_sel, t_sel


def run_pca(xes):
    """
    :param xes: a numpy array that includes rows of equal size flattened arrays,
    :return:  the fitted PCA model and the transformed xes
    """
    pca = PCA()
    pca.fit(xes)
    x_proj = pca.transform(xes)
    return pca, x_proj


def capture_85(mod):
    """
    :param mod: a model of sklearn.decomposition.PCA that has been fitted to a dataset.
    :return: Returns the number of elements needed to capture more than 85% of the variance.
    """
    arr = mod.explained_variance_
    for i in arr:
        if i < 85:
            elements_arr = np.where(arr == i)[0][0] + 1
            return elements_arr


def average_eigenvalue(mod):
    '''
    Takes a PCA model, extracts its explained_variannce, computes the average
    (avg = sum(arr)/len(arr)) and
    returns the number of elements greater than avg.
    '''
    arr = mod.explained_variance_
    avg = sum(arr)/len(arr)
    for i in range(len(arr)):
        if arr[i] < avg:
            return(i)
    return(i)


def approx_digits(mod, img, numComponents=8):
    approx = mod.mean_
    for i in range(numComponents):
      approx += img[i] * mod.components_[i]
    return(approx)
