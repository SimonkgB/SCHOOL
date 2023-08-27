import numpy as np
import matplotlib.pyplot as plt

# Vi valgte følgende variabler for oppgava
x0 = 0 # Vi setter start posisjon x0 lik 0m
v0 = 5 # vi velger start farten v0 som 5 m/s
t = 0 # vi setter tiden lik 0s

g = 9.81 # vi setter tyngde aksellerasjonen lik 9.81 m/s**2
m = 1.0 #Vi setter massen lik 1 kg.
my = 0.2 #Vi velger friksjonskoeffesienten lik 0.2
a = my*g


dt = 0.01 # opptaterings tiden til programmet
tmax = v0/a #Fordi akselerasjonen er konstant kan vi bruke formelen  (v(t_max)=v0 + a*tmax = 0, og løse for t_max)
n = int(tmax/dt)

v = v0
x = x0



x = np.zeros(n) # lager en array: x = [0,0,0,0,0,0,0...0]
v = np.zeros(n) # lager en array: v = [0,0,0,0,0,0,0...0]
a = np.zeros(n) # lager en array: a = [0,0,0,0,0,0,0...0]
t = np.zeros(n) # lager en array: t = [0,0,0,0,0,0,0...0]

i = 0

v[0] = v0   # Gjør så vi får en startfart på v0 og ikke 0
a[0] = g*(-my)

while i < n-1: #I denne while-løkken bytter vi ut i-ende indeks i arrayene ovenfor med de faktiske verdiene.
    a[i + 1] = g*(-my)
    v[i+1] = v[i] + a[i]*dt
    x[i + 1] = x[i] + v[i+1]*dt     # Euler-Cromer
    t[i + 1] = t[i] + dt
    i += 1

plt.subplot(3,1,1)
plt.plot(t,x, "b", label="position")    # setter aksene i grafen og gir dem navn
plt.subplot(3,1,2)
plt.plot(t,v, "y", label="velocity")
plt.subplot(3,1,3)
plt.plot(t,a, "r", label="acceleration")


plt.legend()    # gjør det mulig å se label i grafen
plt.show()  # viser grafen
