"""
import numpy as np
from math import pi
class F:
    def __init__(self,a,w):
        self.a = a
        self.w = w

    def value(self,x):
        return np.exp(-self.a*x)*np.sin(self.w*x)


f = F(a=1.0, w=0.1)
print(f.value(x=pi))
f.a = 2
print(f.value(pi))
"""
import math

class Barometric:
    def __init__(self, T):
        self.T = T #K
        self.g = 9.81 #m/(s*s)
        self.R = 8.314 #J/(K*mol)
        self.M = 0.02896 #kg/mol
        self.p0 = 100.0 #kPa

    def __call__(self, h):
        return self.p0 * math.exp(-self.M*self.g*h/(self.R*self.T))

baro = Barometric(245)
p = baro(2346) #same as p = baro.__call__(2346)