"""
Solution for Quiz 12a:  return size of largest cluster computed via K-Means
"""
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from scipy.stats import mode
from sklearn.metrics import accuracy_score


def max_cluster_size(X, K, random_state):
    kmeans = KMeans(n_clusters=K, random_state=random_state)
    kmeans.fit(X)
    y = kmeans.predict(X)
    counts = [0]*K
    for l in y:
        counts[l] += 1
    return max(counts)
