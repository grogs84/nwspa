# version code 761
# Please fill out this stencil and submit using the provided submission script.

from vec import Vec
from vecutil import *


## Problem 1
def vec_select(veclist, k): 
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_select([v1, v2, v3, v4], 'a') == [Vec(D,{'b': 1}), Vec(D,{'b': 2})]
    True
    '''
    return [vec for vec in veclist if vec[k] == 0] 


def vec_sum(veclist, D): 
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_sum([v1, v2, v3, v4], D) == Vec(D, {'b': 13, 'a': 11})
    True
    '''
    v0 = zero_vec(D)

    for vec in veclist:
        v0 += vec

    return v0


def vec_select_sum(veclist, k, D): 
    '''
    >>> D = {'a','b','c'}
    >>> v1 = Vec(D, {'a': 1})
    >>> v2 = Vec(D, {'a': 0, 'b': 1})
    >>> v3 = Vec(D, {        'b': 2})
    >>> v4 = Vec(D, {'a': 10, 'b': 10})
    >>> vec_select_sum([v1, v2, v3, v4], 'a', D) == Vec(D, {'b': 3})
    True
    '''

    l = vec_select(veclist, k)

    return vec_sum(l,D)



## Problem 2
def scale_vecs(vecdict):
    '''
    >>> v1 = Vec({1,2,3}, {2: 9})
    >>> v2 = Vec({1,2,4}, {1: 1, 2: 2, 4: 8})
    >>> scale_vecs({3: v1, 5: v2}) == [Vec({1,2,3},{2: 3.0}), Vec({1,2,4},{1: 0.2, 2: 0.4, 4: 1.6})]
    True
    '''
    return [1.0/k * vecdict[k] for k in vecdict.keys()]

"""
ungraded problem 2:

find the vectors that span the plane on the picture.

(0,0,0) (2,2,2) (2,2,0)

ans: v1 = (1,1,1) v2=(1,1,0)

must show any points (x,y,z) are in the plane (are linear combinations of v1, v2)

∀[x,y,z]=x[1,0,a]+y[0,1,b] , where z=ax+by

  [x,y,z] =x[1,1,1]+y[1,1,0], where z = ax+by

  you can't just pick any x,y,z.

  to test create a random linear combination of v1,v2

  test that that linear combination (x,y,z) satisfys z = ax +by

for example the point()



"""

## Problem 3
def GF2_span(D, L):
    '''
    >>> from GF2 import one
    >>> D = {'a', 'b', 'c'}
    >>> L = [Vec(D, {'a': one, 'c': one}), Vec(D, {'b': one})]
    >>> len(GF2_span(D, L))
    4
    >>> Vec(D, {}) in GF2_span(D, L)
    True
    >>> Vec(D, {'b': one}) in GF2_span(D, L)
    True
    >>> Vec(D, {'a':one, 'c':one}) in GF2_span(D, L)
    True
    >>> Vec(D, {x:one for x in D}) in GF2_span(D, L)
    True
    '''
    pass



## Problem 4
# Answer with a boolean, please.

is_it_a_vector_space_1 = "..."
is_it_a_vector_space_2 = "..."



## Problem 5
is_it_a_vector_space_3 = "..."
is_it_a_vector_space_4 = "..."


## Problem 6

is_it_a_vector_space_5 = "..."
is_it_a_vector_space_6 = "..."
