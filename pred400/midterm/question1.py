# question 1

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,60,1)


marginal_cost = 3.5
fixed_cost = 90
# total_cost = marginal_cost*x + fixed_cost

# marginal_rev = 7*x
marginal_rev = 7

remainder = 90%3.5

break_even = 90//(7.0 - 3.5)

# you can't sell fractions of a shirt. 
# You have to round up if there is a remainder.
if remainder > 0: break_even += 1

def cost(x):
	return marginal_cost*x + fixed_cost

def revenue(x):
	return marginal_rev*x

plt.xlim(0,60)
plt.ylim(0,300)
plt.xlabel('Sales')
plt.ylabel('$ Amount')


plt.plot(x,cost(x))
plt.plot(x,revenue(x))
plt.scatter(break_even, 7*break_even)
plt.legend(['Total Cost: 3.5x + 90','Marginal Reveune: 7x=y'],loc='best')

plt.show()

print 'They must sell {} to break even'.format(break_even)


