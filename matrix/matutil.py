from vec import Vec
from mat import Mat
from vecutil import list2vec

def identity(D, one):
  """Given a set D and the field's one, returns the DxD identity matrix
  e.g.:
  
  >>> identity({0,1,2}, 1)
  Mat(({0, 1, 2}, {0, 1, 2}), {(0, 0): 1, (1, 1): 1, (2, 2): 1})
  """
  return Mat((D,D), {(d,d):1 for d in D})

def keys(d):
  """Given a dict, returns something that generates the keys; given a list,
     returns something that generates the indices.  Intended for coldict2mat and rowdict2mat.
  """
  return d.keys() if isinstance(d, dict) else range(len(d))

def value(d):
  """Given either a dict or a list, returns one of the values.
     Intended for coldict2mat and rowdict2mat.
  """
  return next(iter(d.values())) if isinstance(d, dict) else d[0]

def mat2rowdict(A):
  """Given a matrix, return a dictionary mapping row labels of A to rows of A
	 e.g.:
	 
     >>> M = Mat(({0, 1, 2}, {0, 1}), {(0, 1): 1, (2, 0): 8, (1, 0): 4, (0, 0): 3, (2, 1): -2})
	 >>> mat2rowdict(M)
	 {0: Vec({0, 1},{0: 3, 1: 1}), 1: Vec({0, 1},{0: 4, 1: 0}), 2: Vec({0, 1},{0: 8, 1: -2})}
	 >>> mat2rowdict(Mat(({0,1},{0,1}),{}))
	 {0: Vec({0, 1},{0: 0, 1: 0}), 1: Vec({0, 1},{0: 0, 1: 0})}
	 """
  return {row:Vec(A.D[1], {col:A[row,col] for col in A.D[1]}) for row in A.D[0]}

def mat2coldict(A):
  """Given a matrix, return a dictionary mapping column labels of A to columns of A
	 e.g.:
	 >>> M = Mat(({0, 1, 2}, {0, 1}), {(0, 1): 1, (2, 0): 8, (1, 0): 4, (0, 0): 3, (2, 1): -2})
	 >>> mat2coldict(M)
	 {0: Vec({0, 1, 2},{0: 3, 1: 4, 2: 8}), 1: Vec({0, 1, 2},{0: 1, 1: 0, 2: -2})}
	 >>> mat2coldict(Mat(({0,1},{0,1}),{}))
	 {0: Vec({0, 1},{0: 0, 1: 0}), 1: Vec({0, 1},{0: 0, 1: 0})}
  """
  return {col:Vec(A.D[0], {row:A[row,col] for row in A.D[0]}) for col in A.D[1]}

def coldict2mat(coldict):
    """
    Given a dictionary or list whose values are Vecs, returns the Mat having these
    Vecs as its columns.  This is the inverse of mat2coldict.
    Assumes all the Vecs have the same label-set.
    Assumes coldict is nonempty.
    If coldict is a dictionary then its keys will be the column-labels of the Mat.
    If coldict is a list then {0...len(coldict)-1} will be the column-labels of the Mat.
    e.g.:
    
    >>> A = {0:Vec({0,1},{0:1,1:2}),1:Vec({0,1},{0:3,1:4})}
    >>> B = [Vec({0,1},{0:1,1:2}),Vec({0,1},{0:3,1:4})]
    >>> mat2coldict(coldict2mat(A)) == A
    True
    >>> coldict2mat(A)
    Mat(({0, 1}, {0, 1}), {(0, 1): 3, (1, 0): 2, (0, 0): 1, (1, 1): 4})
    >>> coldict2mat(A) == coldict2mat(B)
    True
    """
    row_labels = value(coldict).D
    return Mat((row_labels, set(keys(coldict))), {(r,c):coldict[c][r] for c in keys(coldict) for r in row_labels})

def rowdict2mat(rowdict):
    """
    Given a dictionary or list whose values are Vecs, returns the Mat having these
    Vecs as its rows.  This is the inverse of mat2rowdict.
    Assumes all the Vecs have the same label-set.
    Assumes row_dict is nonempty.
    If rowdict is a dictionary then its keys will be the row-labels of the Mat.
    If rowdict is a list then {0...len(rowdict)-1} will be the row-labels of the Mat.
    e.g.:
    
    >>> A = {0:Vec({0,1},{0:1,1:2}),1:Vec({0,1},{0:3,1:4})}
    >>> B = [Vec({0,1},{0:1,1:2}),Vec({0,1},{0:3,1:4})]
    >>> mat2rowdict(rowdict2mat(A)) == A
    True
    >>> rowdict2mat(A)
    Mat(({0, 1}, {0, 1}), {(0, 1): 2, (1, 0): 3, (0, 0): 1, (1, 1): 4})
    >>> rowdict2mat(A) == rowdict2mat(B)
    True
    """
    col_labels = value(rowdict).D
    return Mat((set(keys(rowdict)), col_labels), {(r,c):rowdict[r][c] for r in keys(rowdict) for c in col_labels})

def listlist2mat(L):
  """Given a list of lists of field elements, return a matrix whose ith row consists
  of the elements of the ith list.  The row-labels are {0...len(L)}, and the
  column-labels are {0...len(L[0])}
  >>> A=listlist2mat([[10,20,30,40],[50,60,70,80]])
  >>> print(A)
  <BLANKLINE>
          0  1  2  3
       -------------
   0  |  10 20 30 40
   1  |  50 60 70 80
  <BLANKLINE>
"""
  m,n = len(L), len(L[0])
  return Mat((set(range(m)),set(range(n))), {(r,c):L[r][c] for r in range(m) for c in range(n)})

def rowlist2echelon(rowlist):
  """converts a lsit of vecs to echelon form"""
  col_labels_list = sorted(rowlist[0].D, key=hash)
  new_row_list = []
  rows_left = set(range(len(rowlist)))

  for c in col_labels_list:
    rows_with_nonzero = [r for r in rows_left if rowlist[r][c] !=0]
    if rows_with_nonzero != []:
      pivot = rows_with_nonzero[0]
      new_row_list.append(rowlist[pivot])
      rows_left.remove(pivot)
      for v in new_row_list:
        print v
      print "************"

  return list2mat(new_row_list)





def test_rowlist2echelon():
  v1 = list2vec([0,2,3,4,5])
  v2 = list2vec([0,0,0,0,5])
  v3 = list2vec([1,2,3,4,5])
  v4 = list2vec([0,0,0,4,5])

  rowlist = [v1,v2,v3,v4]

  A = rowlist2echelon(rowlist)
  print(A)


def root_method(N):
  from math import floor, sqrt

  a = N + 1
  while isinstance(sqrt((a*a) - N), int) != True:
    a += 1

  b = sqrt((a*a) - N)

  return a-b


