
from plotting import *

def drange(start, stop, step):
	r = start
	while r < stop:
		yield r
		r += step
	
def line_segment(pt1, pt2, samples=100):
	return [(float(i)/samples)*pt1 + (1-float(i)/samples)*pt2 for i in range(samples+1)]


def find_slope_intercept(u, v):
    """
    inputs: 2 lists of 2 element vectors
    outputs the slope and intercept of a line between the two vectors
    """
    slope = (u[1] - v[1]*1.0) / (u[0] - v[0])
    intercept = u[1] - (slope * u[0])
    return slope, intercept

def generate_points(line_params, points):
    """
    inputs: a list with the slope and intercept describing a line 
            a range numbers to use as the 'x' input  for the line
    outputs: a list of lists that has the points for line
    """
    return [[i, line_params[0] * i + line_params[1]] for i in points]

def scalar_vec_mult(alpha, v):
    """
    inputs: a scalar and a vector
    outputs: a vector mulitplied by the scalar
    """
    return [alpha * x for x in v]

def vector_add(u, v):
    return [ u[i] + v[i] for i in range(len(u))]


def generate_convex_points(u,v,num_points):
	"""
	inputs: two vectors, and the number of points to plot
	outputs: a list of points that are convex combinations of the 
	         two vectors
	"""

	L = []
	points = num_points *1.0
	for i in range(num_points):
		u1 = scalar_vec_mult(i/points, u)
		v1 = scalar_vec_mult(1-(i/points), v)
		pt = vector_add(u1, v1)
		L.append(pt)
	return L

	def zero_vec(D):
		"""
		input: a set D
		output: an instance of Vec representing a D-vector with all
		        0 entries
		"""

		return Vec(D, {})

class Vec:
	"""docstring for Vec"""
	def __init__(self, lables, function):
		self.D = lables
		self.f = function
	def __setitem__(self, key, item):
		pass
	def __getitem__(self, d):
		return self.f[d] if d in self.f else 0


		