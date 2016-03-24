

import numpy as np

def predict(theta, X):
	return theta.dot(X.transpose())

def sigmoid(x):
	return 1/(1 + np.exp(-x))


def cost(p,y):
	return np.mean(-y*np.log(p) - (1-y)*np.log(1-p))

def cost_func(theta, X, y):
	p = predict(theta, X)
	h = sigmoid(p)
	return cost(h,y)

def gradient(theta, X, y):
	err = sigmoid(predict(theta,X)) - y
	grad = err.T.dot(X)
	return grad


def gradient_descent(theta, X, y, alpha=.001, eps=.001):
	X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
	cost_iter = []
	cost = cost_func(theta, X, y)
	cost_iter.append([0, cost])
	change_cost = 1
	i = 1
	while(change_cost > eps):
		old_cost = cost
		theta = theta - (alpha * gradient(theta, X, y))
		cost = cost_func(theta, X, y)
		cost_iter.append([i, cost])
		change_cost = old_cost - cost
		i += 1
	return theta, np.array(cost_iter)

