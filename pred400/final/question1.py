
import numpy as np
import matplotlib.pyplot as plt

# 120x + 30y >= 240 (0,8), (2,0)
# x    + y   >= 5   (0,5), (5,0)
# 15x  + 40y >= 120 (0,3), (8,0)

# .1x + .2y

A = np.array([[120,1,15],
	          [30,1,40]]).transpose()

b = np.array([240,5,120])
zs = np.array([.1, .2])

# 120x + 30y >= 240
l1 = {'m':-120./30, 'b':240.0/30}
# x    + y   >= 5
l2 = {'m':-1, 'b':5}
# 15x  + 40y >= 120
l3 = {'m':-15./40, 'b':120./40}

lines = [l1,l2,l3]

def get_points(line):
	p1 = (0, line['b'])
	p2 = (float(-line['b'])/line['m'], 0)
	return p1, p2
	

def intersection(line1, line2):
	# lines must be in form y=mx +b
	# line is a dict line[m] =know line[b] = know
	# line1[m] -= line2[m]
	# line1 = line2 where
	m1 = line1['m']
	m2 = line2['m']
	b1 = line1['b']
	b2 = line2['b']

	m1 -= m2
	b2 -= b1

	x = float(b2)/m1

	y = line1['m']*x + line1['b']
	# round to the nearest int
	return x,y
	# return np.round(x),np.round(y)


def is_feasable(A, x, b):
	A = np.array(A)
	x = np.array(x)
	b = np.array(b)

	return np.all(A.dot(x)>=b)




corner_points = []

for line in lines[:-1]:
	for line2 in lines[1:]:
		if line != line2:
			point = intersection(line, line2)
			# our point point needs to made of integers
			# search the int points around this for feasable solutions.
			xs = [np.floor(point[0]), np.ceil(point[0])]
			ys = [np.floor(point[1]), np.ceil(point[1])]

			for x in xs:
				for y in ys:
					if is_feasable(A,np.array([x,y]), b):
						corner_points.append((x,y))

			# corner_points.append(intersection(line,line2))



for l in lines:
	p1, p2 = get_points(l)
	corner_points.append(p1)
	corner_points.append(p2)




_min = 10000
solution = {}
print '\n'


for point in corner_points:
	x = np.array(point)
	if is_feasable(A, x, b):
		amounts = A.dot(x)
		temp_min = zs.dot(x)
		print 'point: {}'.format(point)
		print 'for amounts: {}'.format(amounts)
		print 'for a total cost of: {}'.format(temp_min)
		print '\n'
		if temp_min < _min:
			_min = temp_min
			solution['cost'] = temp_min
			solution['points'] = point
			solution['surplus'] = b-amounts


print solution






x = np.linspace(0,10,100)

vitamin_a = (-120./30)*x + (240./30)
vitamin_b = -x + 5
vitamin_c = (-15./40)*x + (120./40)

z1 = (-.1/.2)*x + 3.5

plt.xlim(0,8)
plt.ylim(0,8)

plt.plot(x,vitamin_a)
plt.plot(x,vitamin_b)
plt.plot(x,vitamin_c)
# plt.plot(x,z)
plt.plot(x,z1)

for i in range(9):
	for j in range(9):
		if (j < (-120./30)*i + (240./30)) or (j < -i + 5) or (j < (-15./40)*i + (120./40)):
			plt.scatter(i,j,c='r')
		else:
			plt.scatter(i,j,c='g')



plt.show()