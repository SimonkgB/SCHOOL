"""
class K:
    def __init__(self, a ,b):
        self.a = a
        self.b = b

p = K(2, 6)     # setter inn data
print(p.a)      # henter ut data
print(p.b)

class K:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def verdi(self, x):
        return self.a * x + self.b

p1 = K(0,1)
p2 = K(6,8)
print(p1.verdi(1))
print(p2.verdi(1))



class K:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        s = f"objekt med verdi {self.value}"
        return s


u = K(3.14)
print(u)


class K:
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, b):
        value1 = self.value
        value2 = b.value
         for i in range(len(value1)):
            if value1[i] !=value2[i]:
                return false
        return true

u = K((0,1,2,3))
v = K((0,1,2,4))
print(u==v)


x = complex(1,2)
y = complex(0,1)

print(x)

z = x + y 

print(z)

# kan skrive

class Complex:
    def __init__(self,real, imag):
        self.real = real
        self.imag = imag
    def __str__(self):
        return f"{self.real} + {self.imag}"
    def __add__(self):
        real = self.real + y.real
        imag = self.imag + y.imag
        result = Complex(real, imag)
        return results
"""

print(complex(1,2))