


U=range(1,101)

A = set(U[0:62])
B = set(U[62:])
Ad = set([1])
Bd = set([62,63,64,65])

print len(A)
print len(B)

P=round(len(A&Ad)/float(len(Ad)),3)
print ('Conditional probability of A given Ad is %r') %P