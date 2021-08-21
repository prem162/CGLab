from matplotlib import lines, markers
import matplotlib.pyplot as plt
import numpy as np
px,py=3,4
#plt.subplot(1,2,1)
plt.plot(px,py,marker='o',linestyle='none')
#plt.subplot(1,2,2)
lx = np.linspace(-5,5,10)
ly = px*lx+py
print(lx,ly)
plt.plot(lx, ly, '-r', label='y=2x+1')
plt.title('Graph of y=2x+1')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.legend(loc='upper left')
plt.grid()
plt.show()