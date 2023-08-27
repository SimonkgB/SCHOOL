


class RandomGenerator:
    def __init__(self, seed, m, a, b):
        self.seed = seed
        self.m = m
        self.a = a
        self.b = b

    def __call__(self, n):
        res = []
        x = self.seed
        for i in range(n):
            x = (self.a * x + self.b) % self.m
            res.append(x/(self.m-1))
        return res
    
    def __str__(self):
        return f"seed{self.seed} m={self.m} a={self.a} b={self.b}"

rand = RandomGenerator(0.01,2**16+1, 75, 74)
x = rand(50)
print(x)