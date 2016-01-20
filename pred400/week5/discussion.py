
import numpy as np
import csv

data = []
with open('dan.csv', 'rb') as f:
	reader = csv.reader(f,delimiter=',')
	for row in reader:
		data.append(row)


lables = data.pop(0)

m = len(data)
print m
n = len(data[0])
idx = [int(i) for i in range(m)]

data = np.array(data)

idx = np.array(idx)
idx.shape = (m,1)

d = np.hstack([data,idx])
print d.shape



s = np.random.choice(d[:,29],9)
s = [int(i) for i in s]

print s
print data[s]

print sum(data[:,3])