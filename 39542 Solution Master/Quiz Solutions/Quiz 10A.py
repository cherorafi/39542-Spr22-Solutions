#Quiz 10a:  fit SVC to data and return ...


from sklearn.naive_bayes import GaussianNB
import pickle
import numpy as np

def fit_clf(x_train, y_train):
    """
    :param x_train: the independent variable(s) for the analysis.
    :param y_train: the dependent variable for the analysis.
    :return: the resulting model, pickled, as a bytestream
    """

    clf = GaussianNB()
    clf.fit(x_train, y_train)
    return pickle.dumps(clf)
