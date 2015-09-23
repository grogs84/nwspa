import numpy as np
import matplotlib.pyplot as plt


years = [2010,2011,2012,2013,2014]
pcts = [0.643,0.875,0.846,0.8,0.778]

n = len(years)


# m = n*(x.dot(y)) - (sum(x) * sum(y)) / n*(x.dot(x)) - (sum(x)**2)
# b = sum(y) - m(sum(x)) / n

def make_coef(x, y):
	n = len(years)
	x = np.array(years)
	y = np.array(pcts)
	m1 = n*(x.dot(y)) - (sum(x)*sum(y))
	m2 = n*(x.dot(x)) - sum(x)**2
	m = float(m1)/m2
	b = float((sum(y) - m*(sum(x))))/n
	return m, b, x, y

def predict(x):
	return (m*x) + b



m, b , x, y = make_coef(years, pcts)

print "m is {}".format(m)
print "b is {}".format(b)


plt.plot(x,y,'yo', x, predict(x), '--k')
plt.xlim(2009,2016)
plt.ylim(0,1)
plt.ylabel('Steelers Field Goal Percentage from 40-49 Yards')
plt.xlabel('Years Since 2009')
plt.suptitle('With 2010 Included')
plt.show()

years = years[1:]
pcts = pcts[1:]

m, b , x, y = make_coef(years, pcts)

def predict(x):
	return (m*x) + b

print "m is {}".format(m)
print "b is {}".format(b)


plt.plot(x,y,'yo', x, predict(x), '--k')
plt.xlim(2010,2016)
plt.ylim(0,1)
plt.ylabel('Steelers Field Goal Percentage from 40-49 Yards')
plt.xlabel('Years Since 2010')
plt.suptitle('With 2010 Excluded')
plt.show()
# x = np.array(years)
# y = np.array(pcts)

# m1 = n*(x.dot(y)) - (sum(x)*sum(y))
# m2 = n*(x.dot(x)) - sum(x)**2

# m = float(m1)/m2

# print m

# print '\n'

# b = float((sum(y) - m*(sum(x))))/n

# print b

# # y = m*x + b

# def predict(x, m, b):
# 	return (m*x) + b

# print predict(2015)

# plt.plot(x,y,'yo', x, predict(x), '--k')
# plt.xlim(2009,2016)
# plt.ylim(0,1)
# plt.ylabel('Steelers Field Goal Percentage from 40-49 Yards')
# plt.xlabel('Years Since 2009')
# plt.suptitle('With 2010 Included')
# plt.show()

# plt.plot(x,y,'yo', x, predict(x), '--k')
# plt.xlim(2009,2016)
# plt.ylim(0,1)
# plt.ylabel('Steelers Field Goal Percentage from 40-49 Yards')
# plt.xlabel('Years Since 2009')
# plt.suptitle('With 2010 Included')
# plt.show()


##### using numpy #####

# A = np.vstack([x, np.ones(len(x))]).T
# m, c = np.linalg.lstsq(A,y)[0]

# print m, c