# alt skal v�re likt som jeg gjorde i 5.1 
import math

a = float(input("a verdi:"))    # ber "deg" sete inn en verdi for a i commando vinduet
b = float(input("b verdi:"))    # for b
c = float(input("c verdi:"))    # for c


# For � gj�re koden enklere for maskinen og for � finne potensielle
# komplekse r�tter finner vi alt under kvadratroten, slik:
y = b**2-4*a*c 

if y == 0:    # vis roten er 0 f�r man kun en l�sning
    x = (-b+math.sqrt(b**2-4*a*c))/2*a
    print("liningen har kun en løsning:", x)
elif y < 0:       # vis roten blir <0 vil man f� en kompleks likning
    raise ValueError
else:           # vis roten er 0< f�r man 2 l�sninger
    x1 = (-b+math.sqrt(y))/2*a
    x2 = (-b-math.sqrt(y))/2*a
    print("likningen har l�sningene:", x1, " og", x2)


"""
Terminal> python.exe quadratic_roots.py

raise ValueError
    ValueError

likningen har l�sningene: 1.0  og -1.0
"""