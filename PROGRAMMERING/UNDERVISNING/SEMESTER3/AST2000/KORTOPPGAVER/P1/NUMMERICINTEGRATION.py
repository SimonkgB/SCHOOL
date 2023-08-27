#####################
# METHOD1       RASKE
#####################
import numpy as np

a = 0
b = 1

x = np.linspace(a, b, 100)
y = x**2

trapz = np.trapz(y, x)

print("Trapz:", trapz)

#####################
# METHOD2       NØYAKTIG
#####################
from scipy.integrate import quad

def integrand(x):
    return x**2

result, error = quad(integrand, 0, 1)
print("Result:", result)
print("Error:", error)
