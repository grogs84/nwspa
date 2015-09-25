from orthogonalization import *
from vecutil import list2vec

eps = 1E-10

print '\n'

a = [2,2]
b = [1,3]

v1 = list2vec(a)
v2 = list2vec(b)

print "v1 is {}".format(v1)
print '\n'
print "v2 is {}".format(v2)
print '\n'

projection_of_v1_along_v2, sigma = project_along_w_sigma(v1,v2)

print "the ratio of v1*v2 to v2*v2 = sigma = {}".format(sigma)
print '\n'

print "sigma * v2 is {}".format(sigma*v2)
print '\n'

print "projection of v1 onto v2 is = x {}".format(projection_of_v1_along_v2)
print '\n'

print 'x - v1 = k {}'.format(projection_of_v1_along_v2-v1)
print '\n'

k = projection_of_v1_along_v2-v1

if k*v2 < eps:
	o = 0
else:
	o = k*v2

print "k is orthogonal to v2: k*v2 = {}".format(o)
print '\n'

print "v1 + k is {}".format(v1+k)
print '\n'