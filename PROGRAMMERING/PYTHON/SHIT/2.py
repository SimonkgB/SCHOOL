from typing import Any
import numpy as np
import matplotlib.pyplot as plt



class Quadratic:
    def __init__(self,coff):
        self.coff = coff

    def __call__(self,x):
        res = 0
        for index, initial in enumerate(self.coff):
            power = len(self.coff)-index-1
            res += initial*(x**(power))
        return res
    def __str__(self):
        res = ""
        for index, initial in enumerate(self.coff):
            power = len(self.coff)-index-1
            if initial == 0:
                res += f""
            elif initial == 1:
                res += f"x^{power}+"
            elif power == 0:
                res += f"{initial}"
            elif power == 1:
                res += f"{initial}x+"
            else:
                res += f"{initial}x^{power}+"
        return res.rstrip(" + ")


class Cubic(Quadratic):
    def derivative(self,x):
        res = 0
        for index, initial in enumerate(self.coff):
            power = len(self.coff)-index-1
            if power>=1:
                res += (initial*power)*x**(power-1)
            elif power == 0:
                res += 0
        return res

coff = [1,3,2,4]
p1 = Quadratic(coff)
print(p1)
print(p1(2))

p2 = Cubic(coff)
print(p2(1))