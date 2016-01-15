# 
# The normal distribution is a probability distribution described by 2 parameters u and sigma.
# u and sigma are the expected value and standard deviation of the random variable described by the normal distribution.
# 
# The normal curve is a graph on the normal distribution. The graph is generally bell shaped, but can vary depending 
# on the values of u and sigma from the random variable X. 68.26% of the area under the curve will lie between +/- 1
# standard deviation from them mean. 99.44% will be within +/- 2 standard devaiations, and 99.74% will be with in +/- 3 
# standard deviations. 
# 
# One convient technique for working with data normally distributed is to use the standard normal probability function.
# This normal distribution has a mean of zero and a standard deviation of 1. Probabilities from the standard normal
# distribution come from the definite interal (a to b) 1/sqrt(2pi) * e(-x^2/2)dx. The 1/sqrt(2pi) is a constant factor
# used to normalize e(-x^2/2). To find areas under a normal distribution with u <> 0 and sigma >0 and <> 1, z scores are calculated. A z score can then be
# used to determine the area to the left of that value on the standard normal distribution.
# 
# 
# To show an example of this I will work problem 33 on page 980 of Lial et al using python.
# Supposed a machine produces screws with a mean of 2.5cm and a standard deviation of 0.2cm. Find the probabilities that 
# a screw produced by this machine has lengths:
# a) > 2.7cm
# b) within 1.2 standard deviations of the mean.
# 
# 
# 


import numpy as np
import matplotlib.pyplot as plt
from math import exp as e
from math import sqrt, pi, erf

def normal_dist(x,u,sigma):
	a = 1./sigma*sqrt(2*pi)
	b = -(u-x)**2
	c = 2*sigma**2
	return a * e(b/c)

def zscore2area(z_score):
    return .5 * (erf(z_score / 2 ** .5) + 1)

def zscore(x, u, sigma):
	return (x-u)/sigma

u = 2.5
sigma = 0.2
six_sigmas = .2*6

xs = np.arange(u-six_sigmas, u+six_sigmas, .001)
ys = np.array([normal_dist(x,u,sigma) for x in xs])
rightsd = normal_dist(u+sigma,u,sigma)


# plt.plot(xs, ys)
# plt.scatter(u-sigma, leftsd, c='r')
# plt.show()


# probability > 2.7?
# within 1.2 standard deviations of the mean

print "probability > 2.7"

plt.ylim(0,15)
plt.title("Probability of screw > 2.7cm")
plt.plot(xs, ys)
plt.scatter(u+sigma, rightsd, c='r')
plt.fill_between(xs,ys,where=(xs >= u+sigma),color='grey', alpha='0.3')
plt.text(1,13,'There is a 15.8% chance a screw will be > 2.7cm')
plt.show()


z_score = zscore(2.7, u, sigma)
print 1-zscore2area(z_score)
print "\n"



print "probability within 1.2 standard deviations of mean"

up = u+(sigma+(sigma*.2))
um = u-(sigma+(sigma*.2))

print "u plus 1.2 standard deviations: {}".format(up)
print "u minus 1.2 standard deviations: {}".format(um)
alup = zscore2area(zscore(up,u,sigma))
alum = zscore2area(zscore(um,u,sigma))
print "areas to the left of uu: {}".format(alup)
print "areas to the left of lu: {}".format(alum)
print "probability within 1.2 standard deviations of mean: {}".format(alup-alum)


plt.figure()
plt.ylim(0,15)
plt.plot(xs, ys)
plt.title("Probability within 1.2 standard deviations of mean")
plt.scatter(up, normal_dist(up,u,sigma), c='r')
plt.scatter(um, normal_dist(um,u,sigma), c='r')
plt.fill_between(xs,ys,where=(xs >= -6),color='grey', alpha='0.3')
plt.fill_between(xs,ys,where=(xs >= up),color='white', alpha='0.3')
plt.fill_between(xs,ys,where=(xs <= um),color='white', alpha='0.3')
plt.text(1,13,'There is a 77% chance a screw will be +/- 1.2\n standard devaiations of the mean')
plt.show()