import numpy as np
import matplotlib.pyplot as plt
import scienceplots

with open("filename.txt","r") as infile:
    a=[]
    infile.readline()
    for line in infile:
        a.append(float(line))
    infile.close()

arr=np.array(a)
print(arr)

plt.style.use(["notebook", "grid"])

plt.figure(figsize=(10,5))
plt.hist(arr, bins = 10,color="blue",label="density function")  #density gjør histogrammet om til et denisty plot
plt.xlabel("ulike siffere")
plt.ylabel("antall")
plt.title("RNG between (0,9)")
plt.legend()
plt.show()