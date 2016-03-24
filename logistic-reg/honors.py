

import pandas as pd
import numpy as np

from gradient_descent import sigmoid, cost, predict

df = pd.read_csv("sample.csv")

df['intercept'] = 1

X = np.array(df[['intercept', 'female']])
y = np.array(df['hon'])

y.shape = (200,1)
theta = np.array([1,1])

delta = np.inf
for i in range(2000):
	p = predict(theta,X)
	h = sigmoid(p)
	c = cost(h,y)
	theta1 = theta - .0005*sum(cost(h,y)*X)
	if sum(theta-theta1) >= delta:
		break
	else:
		delta = sum(theta-theta1)

	if i % 100 == 0:
		print sum(theta - theta1)
	theta = theta1


print "theta: {}".format(theta)
print "last predict: {}".format(h)
print "rounds: {}".format(i)