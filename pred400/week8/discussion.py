######################################################################################################
# The fundamental thorem of calculus brings together the two subjects of defferentitaion and interation
# The theorm says F(x) = intergral (x-a) f(t)dt
# the way i think about it is on the interval [a,b] the derivative of F(x) is 
# equal to the limit of the sum of f(t) where t = (x-a)/h as h appoaches infinity



# An example I use that applies this theorm has to do with planning project costs.
# A project maybe given a budget before a detailed project schedule is built.
# Based on a customers requet for date of delivery and type of project we can usually estimate
# the number of months it will take to complete the project +/- a few.

# Generally we need to forecast our projects by month before a project manager has built 
# a detailed monthly budget. One way to solve this problem is take the project budget and 
# divide it by the duration of the projects in months. month spend = budget/# of months

# This works, but not great. Projects tend to spend less and more slowly during design, then 
# as construction starts increases quickly, and finally drops to almost zero during closeout. If the
# costs are spread evenly in the budget it will seem as though projects in design are under spending,
# projects in construction are blowing the budget, and under spending again in closeout. 

# One way to create a more accurate monthly estimate for project is to model it after completed projects 
# monthly spend that we think behaved normally. To do this we fit a polynomial function to a series of 
# points (x, y) using excel where:

# x = % complete a project is (month of spend/# of months for project_i) for each i
# y = % of project spend (monthly spend / total project cost for project_i) for each i


# After some tweaking and normalizing I have a function f(t) and the definite intergral (1-0) f(t)dt = 1.
# To find the monthly cashflows you would sum up f(month/months)*(budget/months). Unfortunetly, because the number of 
# months is sometimes small this sum will be less than the buget. As the number of months approches infinity the sum
# approaches the budget. Try as we might we can't increase the number of months to completion to infinity.

# To get around this we use the fundamental theorm of calculus. It stats that (b to a)f(t)dt. = F(b) - F(a)
# If we take the antiderivative of f(x) we get F(x). For this function F(1) = 1 & F(1)*budget = budget.

# To get the monthly cashflows using this method we create the serires month_i = F(month_i+1)*budget - F(i)*budget
# for i = 0 to number of months.
# Here is a python script to graph and compute the cashflows monthly.

#
#
############################################################################################################
import cPickle as pickle
import numpy as np
import matplotlib.pyplot as plt


g = pickle.load(open('gof1.p', 'rb'))

x3 = -14.8442136613
x2 =  16.509555714
x1 = -1.66964426846
x0 =  0.042690311559

g = np.poly1d([x3,x2,x1,x0])


budget = 378000
months = 18 + 1
xs = np.array([float(month)/months for month in range(months)])
ys = np.array([g(x)*(float(budget)/months) for x in xs])

print sum(ys)

plt.xlim(0,1.1)
plt.bar(xs,ys,width=(1.0/months *.85))
plt.title('monthly cashflow = f(x)*delta x * cashflow amount')
plt.plot(xs,ys,c='r')

plt.show()

Fg = g.integ()

print Fg(1)

ys1 = np.array([(Fg(x+1./months)*budget)-(Fg(x)*budget) for x in xs])

print sum(ys - ys1)
print sum(ys1)

plt.figure()
plt.bar(xs,ys1,width=(1.0/months *.85))
plt.plot(xs,ys1,c='r')
plt.title('monthly cashflow = F(x+1)*budget - F(x)*budget')
plt.show()

ys2 = np.array([(Fg(x)*budget) for x in xs])

plt.figure()
plt.bar(xs,ys2,width=(1.0/months *.85))
plt.plot(xs,ys2,c='r')
plt.title('cumlative spend, the last month = budget exactly')
plt.show()
