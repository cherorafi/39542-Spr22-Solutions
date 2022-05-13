"""
Name: Katherine St. John
Email: katherine.stjohn@hunter.cuny.edu
Resources:  sklearn documentation for classifiers + Python Data Science Handbook
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
import pickle
from sklearn import datasets,metrics
from typing import Union


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

def split_data(data, target, test_size = 0.25, random_state = 21):
    """
    :param data: a numpy array that includes rows of equal size flattened arrays,
    :param target: a numpy array that takes corresponding to the rows of data.
    :param test_size: the size of the test set created when the data is divided into test and training sets with train_test_split. The default value is 0.25.
    :param random_state: the random seed used when the data is divided into test and training sets with train_test_split. The default value is 21.
    :return: Returns the data split into 4 subsets returned by train_test_split.
    """
    x_train,x_test,y_train,y_test = train_test_split(data, target, test_size=test_size, random_state=random_state, stratify=target)
    return x_train, x_test, y_train, y_test


def fit_model(x_train, y_train, model_type='logreg'):
    """
    :param x_train: the independent variable(s) for the analysis.
    :param y_train: the dependent variable for the analysis.
    :param model_type: the type of model to use.  Possible values are 'logreg', 'svm', 'nbayes', and 'rforest'.  See below for the specified parameters for each model.  The default value for this parameter is 'logreg'.
    :return: the resulting model, pickled, as a bytestream
    """
    if model_type == 'logreg':
        clf = LogisticRegression(solver='saga',penalty='l2',max_iter=5000)
    elif model_type == 'svm':
        clf = SVC(kernel='rbf')
    elif model_type == 'nbayes':
        clf = GaussianNB()
    elif model_type == 'rforest':
        clf = RandomForestClassifier(n_estimators=100, random_state=0)
    else:
        #No type specified!  Return None!
        return None

    clf.fit(x_train, y_train)
    return pickle.dumps(clf)


def predict_model(mod_pkl, xes):
    """
    :param model: a object serialization of a trained model (i.e. a pickled bytestream).  The possible model approaches are logistic regression, support vector machine, naive Bayes, and random forest.
    :param xes: the independent variable(s) for the analysis with the same dimensions as which the model was trained.
    :return: the values that the model predicts for the inputted independent variables (that is, the "y_estimate" gives the xes).
    """
    mod = pickle.loads(mod_pkl)
    return mod.predict(xes)


def score_model(mod_pkl,xes,yes):
    """
    :param model: a object serialization of a trained model.  The possible model approaches are logistic regression, support vector machine, 'nbayes' for naive Bayes, and 'rforest' for random forest, using sklearn.
    :param xes: the independent variable(s) for the analysis with the same dimensions as which the model was trained.
    :param yes: the dependent variable(s) for the analysis with the same dimensions as which the model was trained.
    :return: the confusion matrix for the model.
    """
    y_true = yes
    mod = pickle.loads(mod_pkl)
    y_pred = mod.predict(xes)
    confuse_mx = metrics.confusion_matrix(y_true,y_pred)
    return(confuse_mx)

def compare_models(data, target, test_size = 0.25, random_state = 21, models = ['logreg','nbayes','svm','rforest']):
    """
    :param data: a numpy array of flattened arrays,
    :param target: a numpy array of labels for data,
    :param test_size: the size of the test set.  Default value = 0.25.
    :param random_state: the random seed used when the data is divided into test and training sets with train_test_split. Default value = 21.
    :param models: a list of names of models that fit_model accepts.  Default value is ['logreg','nbayes','svm','rforest'].

    Calls split_data, fits each model to the training data, and computes the accuracy.  The name of the model with highest accuracy score is returned.
    """
    x_train,x_test,y_train,y_test = split_data(data, target, test_size=test_size, random_state=random_state)

    best_mod = ""
    best_score = -1
    for m in models:
        m_pkl = fit_model(x_train, y_train, model_type=m)
        score = (pickle.loads(m_pkl)).score(x_test,y_test)
        if score > best_score:
            best_score = score
            best_mod = m
    return best_mod,best_score
