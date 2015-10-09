import matplotlib.pyplot as plt
import numpy as np

# min 3x + 4y
# st
#  x + 3y >= 6
# 2x +  y >= 3

x = np.arange(-2,10,0.1)
y = np.arange(-2,10,0.1)

# y1 = -0.33*x + 2
# y2 = -2.0*x + 3

d1 = -3.0*x + 2
d2 = -0.5*x + (3.0/2)

y3= 10+0.0*x

z = -10+0.0*x

# y4=[0]*len(x)
# for k in range(0,len(x)):
#     if y1[k] >= y2[k]:
#         y4[k]=y1[k]
#     if y2[k] > y1[k]:
#         y4[k]=y2[k]


y6=[0]*len(x)
for k in range(0,len(x)):
    if d1[k] >= d2[k]:
        y6[k]= d2[k]
    if d2[k] > d1[k]:
        y6[k]= d1[k]





y5 = (5.4/2.0) - 3.0*x/2.0

z1 = (5.4/3) - 6.0*x/3.0

plt.xlim(-2,10)
plt.ylim(-2,10)
plt.hlines(0,-2,10,color='k')
plt.vlines(0,-2,10,color='k')
plt.grid(True)

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('The shaded area is the feasible region for the maximization problem.')

# plt.plot(x, y1, color='b')
# plt.plot(x, y2, color='b')

plt.plot(x, d1, color='g')
plt.plot(x, d2, color='g')

plt.plot(x,z1,'k--')

# plt.scatter(.6, 1.8, c='red', s=40)
plt.scatter(.2, 1.4, c='red', s=40)

# plt.legend(['x+3y >= 6','2x+y >= 3', '5.4 = 3x+2y'], 'best')
plt.legend(['x+2y <= 3','3x+y <= 2', '5.4 = 6x+3y'], 'best')

# plt.fill_between(x,y3,y4, color='grey',alpha=0.2)
plt.fill_between(x,z,y6, color='yellow',alpha=0.2)

plt.show()