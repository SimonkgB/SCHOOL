"""
from math import factorial
y = 0 # Skal holde approksimasjonen
m = 1 # Fortegn (enten -1 eller 1)

for i in range(1,9,2):
    y += m * x**i / factorial
    m += -m

#Dette er en dårlig metode istden for gjør det slik:

"""
def sin_taylor(x,n):
    s = [0]*(n+2)
    a = [0]*(n+2)
    a[0] = x
    for i in range(1,n+2):
        s[i] = s[i-1] + a[i-1]
        a[i] = -a[i-1] * x**2 / (2*1*(2*i+1))
    return s[n+1], abs(a[n+1])



def make_table(M,N):
    import numpy as np
    x = np.linspace(0.000001,1,M)
    n = np.arange(1,N+1)
    S= np.zeros((M,N))
    for i in range(M):
        for j in range(N):
            S[i,j] = sin_taylor(x[i], n[j])[0]
    return S, x, n

print(make_table(5,5))