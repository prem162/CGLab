from collections import namedtuple
import random
import matplotlib.pyplot as plt  
import numpy as np
def slopeIntercept(x1,y1,x2,y2):
    m=(y2-y1)/(x2-x1)
    c=y1-m*x1
    return (m,-c)

lines=[(0,1),(2,4),(4,5),(6,2),(4,-1)]
linee=[(2,4),(4,5),(6,2)]
x1=[ls[0] for ls in lines]
y1=[ls[1] for ls in lines]
x2=[ls[0] for ls in lines[1:]]
y2=[ls[1] for ls in lines[1:]]
plt.subplot(1,2,1)
plt.plot(x1,y1,marker='o')
plt.grid()
points=[slopeIntercept(x1[i],y1[i],x2[i],y2[i]) for i in range(len(lines)-1)]
x=[p[0] for p in points]
y=[p[1] for p in points]
#print(points)
plt.subplot(1,2,2)

for i in range(len(x)):
    lx = np.linspace(0,6,5)
    ly = x[i]*lx-y[i]
    #print(lx,ly)
    plt.plot(lx, ly, '-r')
plt.plot(x1,y1,marker='o',color='b',)
plt.grid()
plt.show()