import math

print ("time: population:")
def N(t):               # Definerer N og bruker t som en variabel
    B = 50000           # konstantente brukt i formel
    N_0 = 5000
    C = (B/N_0)-1
    k = 0.2
    return B/(1 + C*math.exp(-k*t))
a_list = [N(t) for t in range(0,49,4)]      # Lager listene 
b_list = [*range(0,49,4)]
tN1 = [b_list, a_list]                 # Samler listene som gjort i neste
for i in range(len(a_list)):            # oppgave for å laget alt oversiktlig
    print(f"{tN1[0][i]}   {tN1[1][i]:5.0f}")    # printer alt ut med f-strings
 

"""
Terminal> py.exe Sum_for.py
time: population:
0    5000
4    9913
8   17749
12   27526
16   36580
20   42924
24   46552
28   48390
32   49263
36   49666
40   49849
44   49932
48   49970
"""

# Bruker samme format som i 3.8 a