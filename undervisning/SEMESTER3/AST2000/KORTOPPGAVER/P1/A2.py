import numpy as np
import matplotlib.pyplot as plt

#a) b)
with open("fileA2.txt", "r") as infile:
    year = []
    month = []
    infile.readline()
    infile.readline()
    for line in infile:
        columns = line.strip().split() 
        year.append(int(columns[0]))
        month.append(float(columns[6]))



plt.figure(figsize=(10,7))
plt.hist(month, bins = 20,color="blue",label="", density = True)
plt.show()


#c)

bi = (max(month)-min(month))/20 + 0.1 

antall = [[] for _ in range(20)]
for i in month:
    for k in range(20):
        if i>min(month)+(k)*bi and i<min(month)+(k+1)*bi:
            antall[k].append(i)

count_antall = [len(a) for a in antall]


#d)
probability=[]
for k in count_antall:
    probability.append(k/sum(count_antall))

#e)
bins = []
for k in range(20):
    bins.append(f"{min(month)+(bi*k):.1f}")

plt.bar(bins,probability)
plt.xlabel("(mm)")
plt.show()

#f)
# No the rainfall is not distrubited as a Gaussian, rather Poisson
#g)
# Yes the similar pattern occur when tring diffrent months