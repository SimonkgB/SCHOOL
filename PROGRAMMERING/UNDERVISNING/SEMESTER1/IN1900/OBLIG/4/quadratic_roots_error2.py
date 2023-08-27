# alt skal våre likt som jeg gjorde i 5.1 
import math

a = float(input("a verdi:"))    # ber "deg" sete inn en verdi for a i commando vinduet
b = float(input("b verdi:"))    # for b
c = float(input("c verdi:"))    # for c


# For å gjøre koden enklere for maskinen og for å finne potensielle
# komplekse røtter finner vi alt under kvadratroten, slik:
y = b**2-4*a*c 

if y == 0:    # vis roten er 0 får man kun en løsning
    x = (-b+math.sqrt(b**2-4*a*c))/2*a
    print("liningen har kun en lÃ¸sning:", x)
elif y < 0:       # vis roten blir <0 vil man få en kompleks likning
    raise ValueError
else:           # vis roten er 0< får man 2 løsninger
    x1 = (-b+math.sqrt(y))/2*a
    x2 = (-b-math.sqrt(y))/2*a
    print("likningen har løsningene:", x1, " og", x2)


"""
Terminal> python.exe quadratic_roots.py

raise ValueError
    ValueError

likningen har løsningene: 1.0  og -1.0
"""