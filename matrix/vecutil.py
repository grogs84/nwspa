from vec import Vec

def list2vec(L):
    """Given a list L of field elements, return a Vec with domain {0...len(L)-1}
    whose entry i is L[i]

    >>> list2vec([10, 20, 30])
    Vec({0, 1, 2},{0: 10, 1: 20, 2: 30})
    """
    return Vec(set(range(len(L))), {k:L[k] for k in range(len(L))})

def zero_vec(D):
    """Returns a zero vector with the given domain
    """
    return Vec(D, {})


def list2vec2(L, D=[]):
    """Given a list L of field elements, return a Vec with domain {0...len(L)-1}
       whose entry i is L[i]    

       >>> list2vec([10, 20, 30], D)    
       Vec({0, 1, 2},{0: 10, 1: 20, 2: 30})    
    """    
    assert isinstance(D, list)
    if not D: D = range(len(L))    

    return Vec(set(D), {k:L[i] for i,k in enumerate(D)})

def vec2list(v):
    l = [i for i in v.D]
    l.sort
    return [v.f[i] for i in l]

def vec2tuple(v):
    return tuple(vec2list(v))

