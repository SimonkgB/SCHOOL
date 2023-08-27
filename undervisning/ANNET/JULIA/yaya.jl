using PyCall
np = pyimport("numpy")
np.linal = pyimport("numpy.linalg")
plt = pyimport("matplotlib.pyplot")


m1= 1
m2= 1
l1= 1
l2= 1
g= 9.81

phi10= π/2
phi20= -π/2

dphi10= 0
dphi20= 0

ddphi10= 0
ddphi20= 0

dt= 0.1
tmax= 10
n = trunc(Int,tmax/dt)

t = np.zeros(n)


phi1 = np.zeros((n,1))
dphi1 = np.zeros((n,1))
ddphi1 = np.zeros((n,1))
phi2 = np.zeros((n,1))
dphi2 = np.zeros((n,1))
ddphi2 = np.zeros((n,1))


phi1[1] = phi10
phi2[1] = phi20
dphi1[1] = dphi10
dphi2[1] = dphi20
ddphi1[1] = ddphi10
ddphi2[1] = ddphi20



M = np.zeros((2,2))
a = np.zeros((2,1))


for i in 1:n-1
    phi1i = phi1[i,1]
    phi2i = phi2[i,1]
    dphi1i = dphi1[i,1]
    dphi2i = dphi2[i,1]
    M[1,1] = (m1+m2)*l1^2
    M[1,2] = m2*l1*l2*cos(phi1i-phi2i)
    M[2,1] = m2*l1*l2*cos(phi1i-phi2i)
    M[2,2] = m2*l1^2


    a[1,1] = m2*l1*l2*dphi2i*sin(phi1i-phi2i)*(dphi1i-dphi2i)-m2*l1*l2*dphi1i*dphi2i*sin(phi1i-phi2i)-(m1+m2)*g*l1*sin(phi1i)
    a[2,1] = m2*l1*l2*dphi1i*sin(phi1i-phi2i)*(dphi1i-dphi2i)+m2*l1*l2*dphi1i*dphi2i*sin(phi1i-phi2i)-m2*g*l2*sin(phi2i)
    ddphi[i] = *(np.linalg.pinv(M),a)
end   
#=
    dphi[i + 1] = dphi[i] + ddphi[i]*dt
    phi[i + 1] = phi[i] + dphi[i+1]*dt

    t[i + 1] = t[i] + dt
end

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
=#