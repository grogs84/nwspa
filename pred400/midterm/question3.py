# midterm question 3

import numpy as np
# [1,1,1,]     [x1]  = 225 total tablets
# [13,18,23] * [x2]  = 4300 mg of niacin
# [11,14,36]   [x3]  = 5200 IU vitamin E
A = np.array([[1,1,1,],
	           [13,18,23],
	           [11,14,36]])

b = np.array([225,4300,5200])

x = np.linalg.solve(A,b)

tablets = ['A', 'B', 'C']

for i in enumerate(x):
	print 'There are {} of tablet {}'.format(i[1], tablets[i[0]])

print 'Ax = {}'.format(A.dot(x))
print 'b = {}'.format(b)
