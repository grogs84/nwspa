## Task 2
def dict2list(dct, keylist): 
	
	myList = [dct[x] for x in keylist]

	return myList	


def list2dict(L, keylist):

	myDict = {k:v for k,v in zip(keylist,L)}

	return myDict

## Task 3
def listrange2dict(L):
    """
    Input: a list
    Output: a dictionary that, for i = 0, 1, 2, . . . , len(L), maps i to L[i]

    You can use list2dict or write this from scratch
    """
    myDict = {k:v for k,v in zip(range(len(L)),L)}

    return myDict


def quadratic(a,b,c):
	import math

	discriminant = math.sqrt((b*b) - (4*a*c))
	return ((-b + discriminant) / (2*a), (-b - discriminant)/ (2*a))

def print_greater_quadratic(L):
		a, b, c = L
		plus, minus = quadratic(a,b,c)
		if plus > minus:
			print(plus)
		else:
			print(minus)


def myNewFunction():
	pass