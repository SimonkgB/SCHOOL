
class F():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def __call__(self, x):
        return self.a*x**2 + self.b*x + self.c
    

f = F(1,2,0)
x = 2
print(f(x))