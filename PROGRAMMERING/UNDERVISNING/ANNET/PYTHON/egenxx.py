import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**x

n=6

x = np.zeros(n)


x[0] = f(0)
x[1] = f(1)
x[2] = f(2)
x[3] = f(3)
x[4] = f(4)
x[5] = f(5)


plt.plot([0,1,2,3,4,5],x)
plt.show()

print(x)