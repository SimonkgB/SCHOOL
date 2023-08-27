"""
Lab (A)
"""

import numpy as np
import matplotlib.pyplot as plt
import scienceplots

with open("filename.txt","r") as infile:
    a=[]
    infile.readline()
    for line in infile:
        a.append(float(line))
    infile.close()
b = sorted(a, key = lambda x:float(x))
arr=np.array(b)

c = 2*np.pi*np.sqrt((0.6)/9.82)


def normal_dist(x, mean, std):
    return (1/(std*np.sqrt(2*np.pi))*np.exp(-0.5*((x-mean)/std)**2))

mean = np.mean(arr)
print(mean)
print(c)
std = np.std(arr)
p = std**2/104
print(np.sqrt(p**2+0.01**2))
pdf = normal_dist(arr, mean, std)

print(f"Integralet til tetthetsfunksjonen = {np.sum(pdf*(arr[103]-arr[0])/104)}")

plt.style.use(["notebook", "grid"])   #If you want cleaner looks install the package hidden in the start 


plt.figure(figsize=(10,7))
plt.hist(arr, bins =len(set(arr))+10,color="blue",label="", density = True)
plt.axvline(c,linestyle="dashed", label="teoretisk svingetid", color="green")
plt.plot(arr,pdf,label="Normal fordeling", color="red",linewidth=3)
plt.xlabel("svingetid(T)[s]")
plt.ylabel("frekvenstetthet")
plt.title("Svingetid for pendel")
plt.legend()
plt.show()
