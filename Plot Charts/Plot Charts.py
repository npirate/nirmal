##import matplotlib.pyplot as plt
##from matplotlib import interactive
##interactive(True)
##X = 5
##y = 2
##plt.plot(X,y)
###plt.show()

import numpy as np

import matplotlib.pyplot as plt
from matplotlib import interactive
interactive(True)

x1 = 5 * np.random.rand(50)

x2 = 5 * np.random.rand(50) + 25

x3 = 30 * np.random.rand(25)

x = np.concatenate((x1, x2, x3))

y1 = 5 * np.random.rand(50)

y2 = 5 * np.random.rand(50) + 25

y3 = 30 * np.random.rand(25)

y = np.concatenate((y1, y2, y3))

color_array = ['b'] * 50 + ['g'] * 50 + ['r'] * 25

plt.scatter(x, y, s=[50], marker='D', c=color_array)

#plt.show()
