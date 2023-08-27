import numpy as np
import matplotlib.pyplot as plt

def roots(r, theta, n):
    for k in range(0,n-1):
        x = r**1/n * (np.cos((theta+2*np.pi*k)/(n)))
        y = r**1/n * (np.sin((theta+2*np.pi*k)/(n)))
        return x, y


x, y =roots(1E-4, 2*np.pi, 6)
plt.plot(x, y, "o", label="n =6")

x, y =roots(1E-4, 2*np.pi, 12)
plt.plot(x, y, "o", label="n =12")

x, y =roots(1E-4, 2*np.pi, 24)
plt.plot(x, y, "o", label="n =24")


plt.show()