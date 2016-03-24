from __future__ import division

from sklearn import datasets
import pandas as pd
import numpy as np

from gradient_descent import gradient_descent

data = datasets.load_iris()
X = data.data[:100, :2]
y = data.target[:100]
X_full = data.data[:100, :]


shape = X.shape[1]
y_flip = np.logical_not(y)
y = np.array(y_flip)*1
betas = np.zeros(shape)
fitted_values, cost_iter = gradient_descent(betas, X, y)
print fitted_values
