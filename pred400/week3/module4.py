# exersices and answers

import numpy as np
import matplotlib.pyplot as plt

# Exercise: Refer to Lial Section 3.1 page 118. Write the code to reproduce
# Figure 10.  Compare your code and the resulting plot to the answer sheet.

# x + 2y <= 12
# 2x + y <= 12
# x, y >= 0


x = np.arange(0,15,1)

y1 = -0.5*x + 6
y2 = -2*x + 12

plt.xlim(0,14)
plt.ylim(0,14)

plt.hlines(0,0,15,color='k')
plt.vlines(0,0,15,color='k')
plt.grid(True)

plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.plot(x,y1, color='b')
plt.plot(x,y2, color='b')

plt.fill_between(x,y1,where=(y1<=y2), color='grey')
plt.fill_between(x,y2,where=(y2<=y1), color='grey')

plt.scatter(3,2, c='g')

plt.show()


# Exercise:  Refer to Lial Section 3.2 Example 3.  Using matrix methods  
# evaluate the objective function at each corner point and determine both
# the maximum and the minimum.  Compare your code and solutions with the 
# answer sheet. 

# find max and min of z = x + 10y by evaluating a function of the corner points


xs = [0, 6, 6, 4]
ys = [3, 6, 3, 2]

A = np.transpose(np.array([xs,ys]))

print 'corner matrix A: \n{}'.format(A)
print '\n'

x = np.array([1,10])
print 'coeffients of goal function: x: {}, y: {}'.format(x[0], x[1])
print '\n'


zs = A.dot(x)

_min, _max = min(zs), max(zs)
_min_index, _max_index = np.argmin(zs), np.argmax(zs)

print 'The values of all the corners are {}\n'.format(zs)
print 'The minimum value is: {} found a the point {}\n'.format(_min, A[_min_index])
print 'The maximum value is: {} found a the point {}\n'.format(_max, A[_max_index])