M = 3
s = 0
k = 1

for k in range(k,M+1):
    s += 1/(2*k)**2
print(s)

    
############
# FEIL funnet:
# k var ikke deffinert
# parantes i brøken manglet
# manglet +1 i rangen





# Det følgende er bare en sjekk for riktig svar
# print((1/(2*1)**2) + (1/(2*2)**2) + (1/(2*3)**2 )) 

"""
Terminal> py.exe Sum_for.py
0.3402777777777778
"""

