import numpy as np
import matplotlib.pyplot as plt


datam0 = np.loadtxt("datam0.txt")
datam1 = np.loadtxt("datam1.txt")
datam2 = np.loadtxt("datam2.txt")
datam3 = np.loadtxt("datam3.txt")
t0 = np.mean(datam0)
t1 = np.mean(datam1)
t2 = np.mean(datam2)
t3 = np.mean(datam3)

m0 = 2.2 #kg
m1 = 2.2 + 42.31/1000 
m2 = 2.2 + 90.38/1000
m3 = 2.2 + 133.01/1000

t = np.array([t0,t1,t2,t3])
m = np.array([m0,m1,m2,m3])

def f(m,t):
    return ((m*t**2)/(4*np.pi**2))

plt.plot(m, t)
plt.show()


"""
g = 9.82


with open("data2.txt","r") as infile:
    a=[]
    b=[]
    infile.readline()
    for line in infile:
        a4 , b4 = line.strip().split(",")
        a.append(float(a4))
        b.append(float(b4))
    infile.close()

a1 = sorted(a, key = lambda x:float(x))
b1 = sorted(b, key = lambda x:float(x))
arra=np.array(a)
arrb=np.array(b)


def f(m,x):
    k = m*g/x
    return k

plt.plot(arra, f(arra,arrb))
plt.show()

"""

