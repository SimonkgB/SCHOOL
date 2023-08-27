import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

m1 = 1
m2=1
l1=1
l2 = 1
g=9.81

phi10 = np.pi/2
phi20 = np.pi/2
dphi10 = 0
dphi20 = 0
ddphi10 = 1
ddphi20 = 1

dt = 0.01
tmax = 10
n = int(tmax/dt)



ddphi1 = np.zeros(n)
ddphi2 = np.zeros(n)
ddphi = np.array([ddphi1, ddphi2])

dphi1 = np.zeros(n)
dphi2 = np.zeros(n)
dphi = np.array([dphi1,dphi2])

phi1 = np.zeros(n)
phi2 = np.zeros(n)
phi = np.array([phi1,phi2])

list = []
arrayz = np.zeros((2, 2))
a=np.ones(10)
for k in range(10):
    i = a[k]*arrayz
    list.append(i)
M = np.array(list)

a = np.zeros(n)
t = np.zeros(n)


phi[0] = np.array(phi10,phi20)
dphi[0] = np.array(dphi10,phi20)
ddphi[0] = np.array(ddphi10,ddphi20)







ddphi[0]=np.array([[-m2*l1*l2*dphi[1][0]*np.sin(phi[0][0]-phi[1][0])*(dphi[0][0]-dphi[1][0])-m2*l1*l2*dphi[0][0]*dphi[1][0]*np.sin(phi[0][0]-phi[1][0])-(m1+m2)*g*l1*np.sin(phi[0][0])],[m2*l1*l2*dphi[0][0]*np.sin(phi[0][0]-phi[1][0])*(dphi[0][0]-dphi[1][0])+m2*l1*l2*dphi[0][0]*dphi[1][0]*np.sin(phi[0][0]-phi[1][0])-m2*g*l2*np.sin(phi[1][0])]])



i = 0
while i < n-1:
    M[i] = np.array([[(m1+m2)*l1**2, m2*l1*l2*np.cos(phi[0][i]-phi[1][i])], [m2*l1*l2*np.cos(phi[0][i]-phi[1][i]), m2*l1**2]])
    a[i] = np.array([[-m2*l1*l2*dphi[1][i]*np.sin(phi[0][i]-phi[1][i])*(dphi[0][i]-dphi[1][i])-m2*l1*l2*dphi[0][i]*dphi[1][i]*np.sin(phi[0][i]-phi[1][i])-(m1+m2)*g*l1*np.sin(phi[0][i])],[m2*l1*l2*dphi[0][i]*np.sin(phi[0][i]-phi[1][i])*(dphi[0][i]-dphi[1][i])+m2*l1*l2*dphi[0][i]*dphi[1][i]*np.sin(phi[0][i]-phi[1][i])-m2*g*l2*np.sin(phi[1][i])]])
    ddphi[i] = np.linalg.pinv(M[i])@ a[i]
    dphi[i + 1] = dphi[i] + ddphi[i]*dt
    phi[i + 1] = phi[i] + dphi[i+1]*dt
    t[i + 1] = t[i] + dt
    i = i + 1
print(ddphi,dphi,phi)




plt.plot(t,phi, "b", label="position")
plt.subplot(3,1,1)
plt.plot(t,dphi, "y", label="velocity")
plt.subplot(3,1,2)
plt.plot(t,ddphi, "r", label="acceleration")
plt.subplot(3,1,3)

plt.legend()
plt.show()