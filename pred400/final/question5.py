
from math import exp as e

def der(f,x,h):
	return (f(x+h)-f(x)) / h


def f(x):
	return 100*e(-0.0482*x)


h = .0001

# print der(f,5,h)

print "The rate of change of '%' of cars still on the road afer 5 years is: {}".format(der(f,5,h))