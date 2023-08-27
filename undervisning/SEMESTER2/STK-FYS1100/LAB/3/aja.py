import numpy as np
import matplotlib.pyplot as plt

x = np.array([596,340,207,128,79])
y = np.array([5.12,10.26,15.29,20.55,25.73])

def f(x,y):
    return -np.log(x/1000)/y

m = np.mean(f(x,y))
print(m)
i = np.linspace(0,60,300)

def g(x):
    return 1000*np.exp(-m*x)

plt.plot(i,g(i))
plt.scatter(y,x)
plt.yscale("log")
plt.show()

print(f(x,y))
plt.plot(y,f(x,y))
plt.show()

# blytykkelse på 22.8mm for 90% av gammakvanter blokka av blyet
# blytykkelse på 45.6mm for 99% av gammakvanter blokka av blyet