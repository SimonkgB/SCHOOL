import numpy as np
import matplotlib.pyplot as plt


class Differentiate:
    def __init__(self, h, x):
        self.h = h
        self.x = x

    def g(self):
        return ((f(self.x+self.h))-f(self.x))/self.h

    def g1(self):
        return (((f(self.x+self.h))-f(self.x-self.h))/(2*self.h))

    def g2(self):
        return (((-f(self.x+2*self.h)+8*f(self.x+self.h)-8*f(self.x-self.h)+f(self.x-2*self.h)))/(12*self.h))

def f(x):
    return np.sin(2*np.pi*x)

x = np.linspace(-1,1,100)

# exact:
plt.plot(x, 2*np.pi*np.cos(2*np.pi*x), color="k", label="exact sol")


h = [0.9, 0.6, 0.3, 0.1]
opac = 0.2
for i in h:
    opac += 0.2 
    p1 = Differentiate(i, x)
    plt.subplot(3,1,1)
    plt.plot(x,p1.g(), color="r", label="sin", alpha = opac)
    plt.subplot(3,1,2)
    plt.plot(x,p1.g1(), color="g", label="sin", alpha = opac)
    plt.subplot(3,1,3)
    plt.plot(x,p1.g2(), color="b", label="sin", alpha = opac)

plt.legend()
plt.show()



