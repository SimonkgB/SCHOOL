# Man vet i t=0 at e**(-k*t)=1 og ved å stokke om på formelen får vi:
# N = (B)/(1 + C) <=> C = ((B/N)-1) å man kan nå finne C

import math

# # Solve for C:
# B_0 = 50000
# N_0 = 5000

# C = (B_0/N_0)-1
# B = 50000
# k = 0.2
# t = 24

# N = B/(1 + C*(math.e**(-k*t)))
# print(f"{N:5.0f}")

def N(t):
    B = 50000
    N_0 = 5000
    C = (B/N_0)-1
    k = 0.2
    return B/(1 + C*math.e**(-k*t))
a_list = [N(t) for t in range(0,24+1)]
for x in range(len(a_list)):
    print(f"{a_list[x]:5.0f}")