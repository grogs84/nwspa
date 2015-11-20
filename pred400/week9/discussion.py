


import numpy as np
import matplotlib.pyplot as plt
from math import exp as e
from math import sqrt, pi, erf

def normal_dist(x,u,sigma):
	a = 1./sigma*sqrt(2*pi)
	b = -(u-x)**2
	c = 2*sigma**2
	return a * e(b/c)

def percentage_of_area_under_std_normal_curve_from_zcore(z_score):
    return .5 * (erf(z_score / 2 ** .5) + 1)

def zscore(x, u, sigma):
	return (x-u)/sigma

u = 2.5
sigma = .2
six_sigmas = .02*6

xs = np.arange(u-six_sigmas, u+six_sigmas, .001)
ys = np.array([normal_dist(x,u,sigma) for x in xs])

# plt.plot(xs, ys)
# plt.show()


# probability > 2.7?
# within 1.2 standard deviations of the mean

print "probability > 2.7"

z_score = zscore(2.7, u, sigma)
print 1-percentage_of_area_under_std_normal_curve_from_zcore(z_score)
print "\n"

print "probability within 1.2 standard deviations of mean"

uu = u+sigma+(sigma*.2)
lu = u-sigma+(sigma*.2)

print "uu: {}".format(uu)
print "lu: {}".format(lu)
aluu = percentage_of_area_under_std_normal_curve_from_zcore(zscore(uu,u,sigma))
allu = percentage_of_area_under_std_normal_curve_from_zcore(zscore(lu,u,sigma))
print "areas to the left of uu: {}".format(aluu)
print "areas to the left of lu: {}".format(allu)
print "probability within 1.2 standard deviations of mean: {}".format(aluu-allu)