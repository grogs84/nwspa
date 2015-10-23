# midterm question 3

import numpy as np

A = np.array([[1,1,1,],
	           [13,18,23],
	           [11,14,36]])

b = np.array([225,4300,5200])

x = np.linalg.solve(A,b)

print 'Ax = {}'.format(A.dot(x))
print 'b = {}'.format()
print A.dot(x) == b