import numpy as np

r = float(input("Radius:"))

def f(r):
    return np.pi*r**2

print(f"Du valgte r = {r}\nArealet er da = {f(r):3.5}")