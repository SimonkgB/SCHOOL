k = 1
S = 0
M = 3

while k <= M:
    S += 1/((2*k)**2)
    k += 1
print(S)

# Begge loopsa får samme svar.

############
# Det følgende er bare en sjekk for riktig svar
# print((1/(2*1)**2) + (1/(2*2)**2) + (1/(2*3)**2 )) 


"""
Terminal> py.exe Sum_for.py
0.3402777777777778
"""