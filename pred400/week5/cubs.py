import numpy as np

from math import factorial as f

def m_choose_n(m,n):
	k = m-n
	return float(f(m))/(f(k)*f(n))

def bernoulli_trial(p,n,k):
	m = n-k
	q = 1.0 - p
	return m_choose_n(n,k)*(p**k)*(q**m)


prob_of_winning = .0504
years = 107
wins = 0

prob_of_zero_wins = bernoulli_trial(prob_of_winning, years, wins)
print 'The probability of 0 world series winds for the cubs: {}'.format(prob_of_zero_wins)

#### find expected number of wins ###

# probability of winninng 0 - 107 world series
probs = [bernoulli_trial(prob_of_winning,years,i) for i in range(years)]

# index of world series wins 0-107
total_wins = [i for i in range(years)]

# convert to numpy arrays to take advantage of element wise multiplication
probs = np.array(probs)
total_wins = np.array(total_wins)

probabilities = probs*total_wins

expected_wins = sum(probabilities)
print 'The expected world series wins in 107 years is: {}'.format(expected_wins)