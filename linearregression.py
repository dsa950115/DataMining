# -*- coding: utf-8 -*-
"""LinearRegression

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dgEZhXGUWS2ZlP5zAx7iNf7WSN_XOAQH
"""

import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

X,y = datasets.make_regression(n_samples=100, n_features=1, noise=20, random_state=4)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

import numpy as np
from collections import Counter

class LinearRegression:
  def __init__(self, lr=0.001, n_iters=1000):
    self.lr = lr
    self.n_iters = n_iters
    self.weights = None
    self.bias = None

  def fit(self, X, y):
    n_samples, n_features = X.shape
    self.weights = np.zeros(n_features)
    self.bias = 0

    for _ in range(self.n_iters):
      y_predicted = np.dot(X, self.weights) + self.bias

      dw = (1/n_samples) * np.dot(X.T, (y_predicted - y))
      db = (1/n_samples) * np.sum(y_predicted - y)

      self.weights -= self.lr * dw
      self.bias -= self.lr * db

  def predict(self, X):
    y_predicted = np.dot(X, self.weights) + self.bias
    return y_predicted

reg = LinearRegression()
reg.fit(X_train, y_train)
reg.predict(X_test)