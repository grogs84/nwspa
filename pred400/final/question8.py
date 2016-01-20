


def der(f,x,h):
	return (f(x+h) - f(x))/h


def f(x):
	return x**4 -13*x**3 +44*x**2 -55*x +20



print der(f,3,.001)

