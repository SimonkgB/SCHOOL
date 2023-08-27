import math

print ("time: population:")
def population(t, k=0.2, B=50000, C=9): #lager funksjon popu...
    y = B/(1 + C*math.exp(-k*t))        # Funksjonen
    return y

a_list = [population(t) for t in range(0,49,4)]      # Lager listene 
b_list = [*range(0,49,4)]
tN1 = [b_list, a_list]                 # Samler listene
for i in range(len(a_list)):            # finner antall verdier i lista for å laget alt oversiktlig
    print(f"{tN1[0][i]}   {tN1[1][i]:5.0f}")    # printer alt ut med f-strings


"""
Terminal> py.exe pop_func.py
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