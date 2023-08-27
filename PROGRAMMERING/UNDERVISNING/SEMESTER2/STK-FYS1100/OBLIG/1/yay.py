import urllib.request

# Last ned dataene fra nettsiden
url = "https://www.uio.no/studier/emner/matnat/math/STK1100/data/doedelighet.txt"
response = urllib.request.urlopen(url)
data = response.read().decode()

# Behandle dataene og lag en liste med dødsfall per alder
dodsfall_per_alder = []
for line in data.splitlines():
    if line:
        alder, antall_dodsfall = line.split()
        dodsfall_per_alder.append(int(antall_dodsfall))

# Beregn CDFen til X
n = sum(dodsfall_per_alder)
cdf = [0] * (len(dodsfall_per_alder) + 1)
for i in range(len(dodsfall_per_alder)):
    cdf[i+1] = cdf[i] + dodsfall_per_alder[i] / n

# Finn punktsannsynlighetene
px = [0] * (len(dodsfall_per_alder) + 1)
px[0] = cdf[0]
for i in range(1, len(px)):
    px[i] = cdf[i] - cdf[i-1]

# Skriv ut punktsannsynlighetene
for i in range(len(px)):
    print("P(X = {}) = {}")
