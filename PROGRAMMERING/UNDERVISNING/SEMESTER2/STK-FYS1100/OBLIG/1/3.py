import matplotlib as plt
import numpy as np
import matplotlib.pyplot as plt

infile = open("doedelighet.txt", "r")
infile.readline()
alder = []
menn = []
kvinner = []
for line in infile:  
    words=line.split()
    alder.append(int(words[0]))
    menn.append(float(words[1])/1000)
    kvinner.append(float(words[2])/1000)

###############################

#c)

P = lambda list, qm: list[qm] * (1 - np.array(list[:qm])).prod()

punkt_mann = []
punkt_kvinne = []
for i in range(len(alder)):
    punkt_mann.append(P(menn, i))
    punkt_kvinne.append(P(kvinner, i))


plt.subplot(2,1,1)
plt.bar(alder, punkt_mann, 1, edgecolor="black")
plt.title("menn")
plt.xlabel("alder")
plt.ylabel("punktsannsynelighet")

plt.subplot(2,1,2)
plt.bar(alder, punkt_kvinne, 1, edgecolor="black")
plt.title("kvinner")
plt.xlabel("alder")
plt.ylabel("punktsannsynelighet")

plt.show()




###############################

#d) vis X<a har man allerede overlevd år X så man kan ikke dø
# vis X>=a er sansyneligheten for at man overlever til år X der X-a sier hvor mange år frem i tid det er 

###############################

#e) og f)

h = lambda a, x: 0 if x < a else x - a
    
E = lambda list, a: sum(h(a, i) * list[i] for i in range(len(list)))

gjennstående_m = []
gjennstående_k = []
for k in range(len(alder)):
   gjennstående_m.append(E(punkt_mann,k))
   gjennstående_k.append(E(punkt_kvinne,k))

j = [30,50,80,0]
for u in j:
    print(f"Antat gjenstående levetid for en mann {u} er {gjennstående_m[u]:.2f} år")
for u in j:
    print(f"Antat gjenstående levetid for en kvinne {u} er {gjennstående_k[u]:.2f} år")

# svar for e) Man ser at med alder vil man på basis ha kortere å leve enn tidligere
# e)
"""
Terminal> Python.exe> 3.py
Antat gjenstående levetid for en mann 30 er 50.88 år
Antat gjenstående levetid for en mann 50 er 31.26 år
Antat gjenstående levetid for en mann 80 er 5.24 år
Antat gjenstående levetid for en mann 0 er 80.73 år
"""

# svar for f) Det er tydlig at kvinner gjennomsnittlig lever lengere enn menn.
# f)
"""
Antat gjenstående levetid for en kvinne 30 er 54.21 år
Antat gjenstående levetid for en kvinne 50 er 34.43 år
Antat gjenstående levetid for en kvinne 80 er 7.14 år
Antat gjenstående levetid for en kvinne 0 er 84.11 år
"""
#####################
#g)

plt.plot(alder, gjennstående_m, "b", label="mann")
plt.plot(alder, gjennstående_k, "r", label="kvinne")
plt.xlabel("Alder")
plt.ylabel("Sansynlig gjenstående levetid")
plt.legend()
plt.show()

