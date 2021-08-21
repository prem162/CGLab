
import matplotlib.pyplot as plt
import numpy as np
x=[3,2,5,8,1,5]
y=[2,9,3,6,8,3]
plt.subplot(1,2,1)
plt.plot(x,y,marker='o',linestyle='none')
plt.subplot(1,2,2)
for i in range(6):
    lx = np.linspace(-5,5,10)
    ly = x[i]*lx+y[i]
    print(lx,ly)
    plt.plot(lx, ly, '-r', label='y=2x+1')
plt.title('Graph of y=2x+1')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.legend(loc='upper left')
plt.grid()
plt.show()