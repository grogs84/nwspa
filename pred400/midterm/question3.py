# midterm question 3

import numpy as np

A = np.array([[1,1,1,],
	           [13,18,23],
	           [11,14,36]])

b = np.array([225,4300,5200])

x = np.linalg.solve(A,b)

tablets = ['A', 'B', 'C']

# results = enumerate(x)

for i in enumerate(x):
	print 'There are {} of tablet {}'.format(i[1], tablets[i[0]])

print 'Ax = {}'.format(A.dot(x))
print 'b = {}'.format(b)
print A.dot(x) == b