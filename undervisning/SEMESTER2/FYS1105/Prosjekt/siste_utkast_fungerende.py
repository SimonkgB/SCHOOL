import numpy as np
import numpy.linalg as lin
import matplotlib.pyplot as plt

m1= 1
m2= 1
l1= 1
l2= 1
g= 9.81

phi10= np.pi/2
phi20= -np.pi/2

dphi10= 0
dphi20= 0

ddphi10= 0
ddphi20= 0

dt= 0.01
tmax= 100
n = int(tmax/dt)
print(n)

t = np.zeros(n)

phi = np.zeros((n,2,1))
dphi = np.zeros((n,2,1))
ddphi = np.zeros((n,2,1))

phi[0] = np.array([[phi10], [phi20]])
dphi[0] = np.array([[dphi10],[dphi20]])
ddphi[0] = np.array([[ddphi10],[ddphi20]])
print(phi)
M = np.zeros((2,2))
a = np.zeros((2,1))


for i in range(n-1):
    phi1i = phi[i][0][0]
    phi2i = phi[i][1][0]
    dphi1i = dphi[i][0][0]
    dphi2i = dphi[i][1][0]
    M[0][0] = (m1+m2)*l1**2
    M[0][1] = m2*l1*l2*np.cos(phi1i-phi2i)
    M[1][0] = m2*l1*l2*np.cos(phi1i-phi2i)
    M[1][1] = m2*l1**2

    a[0][0] = m2*l1*l2*dphi2i*np.sin(phi1i-phi2i)*(dphi1i-dphi2i)-m2*l1*l2*dphi1i*dphi2i*np.sin(phi1i-phi2i)-(m1+m2)*g*l1*np.sin(phi1i)
    a[1][0] = m2*l1*l2*dphi1i*np.sin(phi1i-phi2i)*(dphi1i-dphi2i)+m2*l1*l2*dphi1i*dphi2i*np.sin(phi1i-phi2i)-m2*g*l2*np.sin(phi2i)
    ddphi[i] = np.linalg.pinv(M)@a
    
    dphi[i + 1] = dphi[i] + ddphi[i]*dt
    phi[i + 1] = phi[i] + dphi[i+1]*dt

    t[i + 1] = t[i] + dt

plt.subplot(3,1,1)
plt.plot(t,phi[:,0,0], "b", label="Angle of phi_1")
plt.plot(t,phi[:,1,0], "r", label="Angle of phi_2")
plt.xlabel("Time (s)")
plt.ylabel("Angle (rad)")
plt.legend()
plt.subplot(3,1,2)
plt.plot(t,dphi[:,0,0], "b", label="Angular velocity of phi_1")
plt.plot(t,dphi[:,1,0], "r", label="Angular velocity of phi_2")
plt.xlabel("Time (s)")
plt.ylabel("Angular velocity (rad/s)")
plt.legend()
plt.subplot(3,1,3)
plt.plot(t,ddphi[:,0,0], "b", label="Angular acceleration of phi_1")
plt.plot(t,ddphi[:,1,0], "r", label="Angular acceleration of phi_2")
plt.xlabel("Time (s)")
plt.ylabel("Angular acceleration  (rad/s^2)")

plt.legend()
plt.show()
