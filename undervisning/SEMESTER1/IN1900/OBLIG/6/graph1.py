import numpy as np
import matplotlib.pyplot as plt


# oppgave a)
def plot_line(p1,p2, p):    # variablene brukt, p er fo hvor i subplotet grafen skal befinne seg
    x = [p1[0], p2[0]]
    y = [p1[1], p2[1]]
    plt.subplot(3,1,p)  # sier igjen hvor det befinner seg 
    plt.plot(x, y)      # plotter ut for x og y verdier 

p1 = (0, 0)     # tilfeldige punkter bestemt
p2 = (2, 0)
p3 = (0, 0)
p4 = (0, 2)

plot_line(p1, p2, 1)
plot_line(p3, p4, 1)


# oppgave b)
def complete_graph(points, p):
    for x in range(0,len(points)):      # koden fungerer slik at den tar første punktet og lager en linje til alle andre punkter
        for i in range(1,len(points)):  # så tar den neste punkt og gjør det samme med den
            plot_line(points[x],points[i], p)   # bruker funksjonen laget tidligere til å plotte
            
a = (np.sqrt(2)/2)  # a verdien
f1 = [(0,0),(1,0),(0,1),(1,1)]  
f2 = [(1,0),(a,a),(0,1),(-a,a),(-1,0),(-a,-a),(0,-1),(a,-a)]    # punktene gitt
 
complete_graph(f1, 2)   # plotter punktene gitt in i funksjonen
complete_graph(f2, 3)

plt.show()      # viser grafen