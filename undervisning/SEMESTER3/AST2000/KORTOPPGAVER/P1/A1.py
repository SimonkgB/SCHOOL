import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
#1)

a1 = 30
a2 = 70

sigma = 2
mu = 29

x1 = np.linspace(a1, a2, 1000)

trapz1 = np.trapz(norm.pdf(x1, mu, sigma), x1)

print("Trapz:", trapz1)




#3)
sevendays = trapz1**7
print(f"the probability for the temprature being over 30 degrees for 7 is: {sevendays}")
#4)

from math import factorial

b1 = 0
b2 = 30

x2 = np.linspace(b1, b2, 1000)

trapz2 = np.trapz(norm.pdf(x2, mu, sigma), x2)

svar = (factorial(7)/(factorial(4)*factorial(4)))*(trapz1**4)*(trapz2**3)
print(f"Det er: {svar}")