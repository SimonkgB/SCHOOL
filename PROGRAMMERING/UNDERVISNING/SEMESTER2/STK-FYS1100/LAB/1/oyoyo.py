import matplotlib.pyplot as plt
import numpy as np


data = np.loadtxt("data.txt")
print(data)
"""
plt.figure(figsize=(10,7))
plt.hist(data,bins =len(set(data))+10,density = True, color="blue", label="")
plt.xlabel("svingetid(T)[s]")
plt.ylabel("frekvenstetthet")
plt.title("Svingetid for Foccault pendel")
plt.legend()
plt.show()
"""
std = np.std(data)
mean = np.mean(data)
print(mean)

u = np.sqrt((std**2)/45+0.01**2+ 0.1**2)
print(u)

print(((4*np.pi**2)*0.082511)/(7.538**2) - ((8*np.pi**2*14.33)/(7.538**3)*0.1024))
print((4*np.pi**2)*14.33/(7.538**2))


y = 14.33
x = 0.94

print(np.arcsin(x/y)*180/np.pi)

