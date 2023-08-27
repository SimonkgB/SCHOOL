import numpy as np
import matplotlib.pyplot as plt

n=21

x = np.zeros(n)
dx = np.zeros(n)
ddx = np.zeros(n)
dddx = np.zeros(n)
ddddx = np.zeros(n)

def f(x):
    return (x**3+5*x-1)     #NOTE: Sum_(n=0)(x**2+2*x+1) = Sum_(n=1)(x**2)

x[0] = f(0)
x[1] = f(1)
x[2] = f(2)
x[3] = f(3)


dx[0] = (x[1]-x[0])
dx[1] = (x[2]-x[1])
dx[2] = (x[3]-x[2])


ddx[0] = dx[1]-dx[0]
ddx[1] = dx[2]-dx[1]



if ddx[0] == ddx[1]:

    for i in range(n-1):
        dx[i+1] = dx[i] + ddx[0]
        x[i+1] = x[i] + dx[i]

else:
    x[4] = f(4)
    dx[3] = x[4]-x[3]
    ddx[2] = dx[3]-dx[2]
    dddx[0] = ddx[1]-ddx[0]
    dddx[1] = ddx[2]-ddx[1]
    
    if dddx[0] == dddx[1]:

        for i in range(n-1):
            ddx[i+1] = ddx[i] + dddx[0]
            dx[i+1] = dx[i] + ddx[i]
            x[i+1] = x[i] + dx[i]
    else:
        x[5] = f(5)
        dx[4] = x[5]-x[4]
        ddx[3] = dx[4]-dx[3]
        dddx[2] = ddx[3]-ddx[2]
        ddddx[0] = dddx[1]-dddx[0]
        ddddx[1] = dddx[2]-dddx[1]
        
        if ddddx[0] == ddddx[1]:

            for i in range(n-1):
                dddx[i+1] = dddx[i] + ddddx[0]
                ddx[i+1] = ddx[i] + dddx[i]
                dx[i+1] = dx[i] + ddx[i]
                x[i+1] = x[i] + dx[i]
        else:
            pass



print(x)
