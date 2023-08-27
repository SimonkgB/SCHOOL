import math
# a)        #Alt for oppgava er beskrevet i forrige (3.7)
print ("time: population:")
def N(t):
    B = 50000
    N_0 = 5000
    C = (B/N_0)-1
    k = 0.2
    return B/(1 + C*math.exp(-k*t))
a_list = [N(t) for t in range(0,49,4)]
b_list = [*range(0,49,4)]
tN1 = [b_list, a_list]
for i in range(len(a_list)):
    print(f"{tN1[0][i]}     {tN1[1][i]:5.0f}")
    

#b)
print ("time: population:")
tN2=[]                              #Lager en tom liste
for i in range(len(a_list)):
    tN00 = [tN1[0][i], tN1[1][i]]   # lager en med annenhver t og N
    tN2.append(tN00)                #legger den forrige lista in i den fra tidligere

for i in range(0,len(a_list)):      # for antall i lista elges alle verdiene
    print(f"{int(tN2[i][0]):2}     {int(tN2[i][1]):5}") #printer det
    

"""
Terminal> py.exe population_table2.py
time: population:
0      5000
4      9913
8     17749
12     27526
16     36580
20     42924
24     46552
28     48390
32     49263
36     49666
40     49849
44     49932
48     49970
time: population:
 0      5000
 4      9912
 8     17748
12     27526
16     36580
20     42924
24     46551
28     48389
32     49263
36     49666
40     49849
44     49932
48     49969
"""