# midterm question 6

import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0,26,1)

### equation 1 red line ####
y1 = -2*x +20

### equation 2 blue line ####
y2 = -1.0*x +15

### corners ###
xx = [5, 0, 0, 25, 25, 15]
yy = [10,20,25,25, 0,  0]

##### set plot attributes #####
plt.xlim(0,25)
plt.ylim(0,25)
plt.xlabel('x-axis')
plt.ylabel('y-axis')



plt.plot(x,y1,c='red')
plt.plot(x,y2,c='blue')
plt.fill(xx,yy, color='grey',alpha=0.5)
plt.legend(['2*x + y >= 20','x + y >= 15'],loc='best')


plt.show()