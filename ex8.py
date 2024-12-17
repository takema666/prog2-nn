import numpy as np
import matplotlib.pyplot as plt

#xs = np.array([-5,-4,-3,-2,-1,0,1,2,3,4,5])
#ys = np.array([66,45,28,15,6,1,0,3,10,21,36])
xs = np.array(np.linspace(-5,5,num=11))
ys = 2**xs - 3*xs +1

plt.plot(xs,ys)
plt.show