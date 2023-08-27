import numpy as np
# x = np.linspace(0,2,20)
# y= x*(2-x)
# import matplotlib.pyplot as plt
# plt.plot(x,y)
# plt.show()

# forbedret og med 1000 punkter
x = np.linspace(0,2,1000)
y = np.cos(18*np.pi * x)
import matplotlib.pyplot as plt
plt.plot(x,y)
plt.show()