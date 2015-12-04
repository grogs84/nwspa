
import numpy as np
import matplotlib.pyplot as plt
import math


def f(x):
    f = (1./85)*math.exp(float(-x)/85)    
    return f


def integrate(a,b,delta):    #
    sum = 0.0
    i = 0
    n = int(float((b-a)/delta))
    if b == a:
        return
    else:
        while i < n:
            x0 = a+delta*i
            x1 = x0+delta/2
            x2 = x0+delta
            sum = sum + delta*(f(x0)+4.0*f(x1)+f(x2))/6
            i = i+1
        return sum

def delta(start, stop, n):
    return float((stop - start)/n)

start = 0
stops = [68.0, 457.0]
n = 1500

probs = [integrate(start, stop, delta(start, stop, n)) for stop in stops]


print "The probability that a goal is scored in no more than 68 minutes is {}".format(probs[0])
print "The probability that a goal is scored in no more than 457 minutes is {}".format(probs[1])