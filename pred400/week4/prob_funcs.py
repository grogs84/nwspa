

from math import factorial as f

def m_choose_n(m,n):
	k = m-n
	return float(f(m))/(f(k)*f(n))

def bernoulli_trial(p,n,k,):
	m = n-k
	q = 1.0 - p
	return m_choose_n(n,k)*(p**k)*(q**m)

