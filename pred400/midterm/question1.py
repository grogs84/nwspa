# question 1

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,60,1)


marginal_cost = 3.5
fixed_cost = 90
total_cost = marginal_cost*x + fixed_cost

marginal_rev = 7*x

remainder = 90%3.5

break_even = 90//(7.0 - 3.5)

if remainder > 0: break_even += 1

plt.plot(x,total_cost)
plt.plot(x,marginal_rev)
plt.scatter(break_even, 7*break_even)

plt.show()



