
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4.5,4.5,100)
axis = [0]*len(x)


def f(x):
	return x**3 + 2*x**2 -5*x -6

def f_prime(x):
	return 3*x**2 +4*x -5

def zero_line(x):
	return 0

plt.ylim(-20, 70)
plt.xlim(-4,4)



plt.plot(x,f(x), c='blue',  label='y=f(x)')
plt.plot(x,f_prime(x), c='black', label="y=f'(x)")
plt.scatter(-3,0,c='r')
plt.scatter(-2,f(-2),c='y')
plt.scatter(-1,0,c='r')
plt.scatter(1,f(1), c='y')
plt.scatter(2,0,c='r')
plt.plot(x,axis, c='green')
plt.legend(['y=f(x)', "y=f'(x)"], 'best')
plt.show()