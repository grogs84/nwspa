from vec import Vec
from vecutil import zero_vec

def intersection(A,B):
    return set(A.f.keys()) | set(B.f.keys())

def getitem(M, k):
    "Returns the value of entry k in M.  The value of k should be a pair."
    assert k[0] in M.D[0] and k[1] in M.D[1]

    return M.f[k] if k in M.f else 0

def setitem(M, k, val):
    "Sets the element of v with label k to be val.  The value of k should be a pair"
    assert k[0] in M.D[0] and k[1] in M.D[1]
    M.f[k] = val

def add(A, B):
    "Returns the sum of A and B"
    assert A.D == B.D
    
    return Mat((A.D[0],A.D[1]), {r_c:A[r_c] + B[r_c] for r_c in intersection(A,B)})

def scalar_mul2(M, alpha):
    "Returns the product of scalar alpha with M" 
    return Mat((M.D[0], M.D[1]), {(r,c):M[(r,c)] * alpha for r in M.D[0] for c in M.D[1]})

def scalar_mul(M, alpha):
    "Returns the product of scalar alpha with M" 
    return Mat((M.D[0], M.D[1]), {r_c:M[r_c] * alpha for r_c in M.f.keys()})

def equal(A, B):
    "Returns true iff A is equal to B"
    assert A.D == B.D
    L = [A[(r,c)] == B[(r,c)] for r in A.D[0] for c in A.D[1]]

    if False in L:
        return False
    else:
        return True


def transpose(M):
    "Returns the transpose of M"
    return Mat((M.D[1], M.D[0]), {(r,c):M[(c,r)] for c in M.D[0] for r in M.D[1]})


def lin_comb_vec_mat_mult(v, M):
    "Returns the product of vector v and matrix M"
    assert M.D[0] == v.D

    rows = M.D[0]
    cols = M.D[1]

    vec = zero_vec(cols)

    for c in cols:
        for r in rows:
            vec[c] += v[c] * M[(r,c)]

    return vec

def vector_matrix_mul(v, M):
    "Returns the product of vector v and matrix M"
    assert M.D[0] == v.D

    vec = zero_vec(M.D[1])

    for mr,mc in M.f.keys():
        for vc in v.f.keys():
            if mr == vc:
                vec[mc] += v[vc] * M[(mr,mc)]
    return vec  


def matrix_vector_mul(M, v):
    "Returns the product of matrix M and vector v"
    assert M.D[1] == v.D

    rows = M.D[0]

    vec = zero_vec(rows)

    for vr in v.f.keys():
        for mr,mc in M.f.keys():
            if vr == mc:
                vec[mr] += v[vr] * M[(mr,mc)]

    return vec

def lin_comb_mat_vec_mult(M, v):
    "Returns the product of matrix M and vector v"
    assert M.D[1] == v.D

    rows = M.D[0]
    cols = M.D[1]

    vec = zero_vec(rows)

    for r in rows:
        for c in cols:
            vec[r] += M([r,c]) * v[r]

    return vec


def matrix_matrix_mul2(A, B):
    "Returns the product of A and B"
    assert A.D[1] == B.D[0]
    
    Arows = A.D[0]
    Bcols = B.D[1]
    Brows = B.D[0]

    mat = Mat((Arows, Bcols), {})

    for r in Arows:
        for c in Bcols:
            for k in Brows:
                mat[(r,c)] += A[(r,k)] * B[(k,c)]

    return mat


def matrix_matrix_mul(A, B):
    "Returns the product of A and B"
    assert A.D[1] == B.D[0]

    mat = Mat((A.D[0], B.D[1]), {})


    for brow, bcol in B.f.keys():
        for arow, acol in A.f.keys():
            if brow == acol:
                mat[(arow, bcol)] += B[(brow, bcol)] * A[(arow, acol)]
    return mat

################################################################################

class Mat:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function

    __getitem__ = getitem
    __setitem__ = setitem
    transpose = transpose

    def __neg__(self):
        return (-1)*self

    def __mul__(self,other):
        '''if Mat == type(other):'''
        if isinstance(other, Mat):
            return matrix_matrix_mul(self,other)
        '''elif Vec == type(other):'''
        if isinstance(other, Vec):
            return matrix_vector_mul(self,other)
        else:
            return scalar_mul(self,other)
            #this will only be used if other is scalar (or not-supported). mat and vec both have __mul__ implemented

    def __rmul__(self, other):
        """if Vec == type(other):"""
        if isinstance(other, Vec):
            return vector_matrix_mul(other, self)
        else:  # Assume scalar
            return scalar_mul(self, other)

    __add__ = add

    def __sub__(a,b):
        return a+(-b)

    __eq__ = equal

    def copy(self):
        return Mat(self.D, self.f.copy())

    def __str__(M, rows=None, cols=None):
        "string representation for print()"
        if rows == None:
            try:
                rows = sorted(M.D[0])
            except TypeError:
                rows = sorted(M.D[0], key=hash)
        if cols == None:
            try:
                cols = sorted(M.D[1])
            except TypeError:
                cols = sorted(M.D[1], key=hash)
        separator = ' | '
        numdec = 3
        pre = 1+max([len(str(r)) for r in rows])
        colw = {col:(1+max([len(str(col))] + [len('{0:.{1}G}'.format(M[row,col],numdec)) if isinstance(M[row,col], int) or isinstance(M[row,col], float) else len(str(M[row,col])) for row in rows])) for col in cols}
        s1 = ' '*(1+ pre + len(separator))
        s2 = ''.join(['{0:>{1}}'.format(c,colw[c]) for c in cols])
        s3 = ' '*(pre+len(separator)) + '-'*(sum(list(colw.values())) + 1)
        s4 = ''.join(['{0:>{1}} {2}'.format(r, pre,separator)+''.join(['{0:>{1}.{2}G}'.format(M[r,c],colw[c],numdec) if isinstance(M[r,c], int) or isinstance(M[r,c], float) else '{0:>{1}}'.format(M[r,c], colw[c]) for c in cols])+'\n' for r in rows])
        return '\n' + s1 + s2 + '\n' + s3 + '\n' + s4

    def pp(self, rows, cols):
        print(self.__str__(rows, cols))

    def __repr__(self):
        "evaluatable representation"
        return "Mat(" + str(self.D) +", " + str(self.f) + ")"
