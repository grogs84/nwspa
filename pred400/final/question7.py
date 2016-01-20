
# import numpy as np
from math import log as ln

def p(t):
	return ((t*t) + 100)*ln(t+2)

def f(x):
	return x**2

def der(f,x,h):
	return (f(x+h) - f(x))/h


if __name__ == '__main__':

	# print der(f, 1, .00001)
	print der(p, 16, .00001)

