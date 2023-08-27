import math
import sys

try:      # første arg går som filens navn så:
    a = float(sys.argv[1])  # henter 2. arg i komando linja
    b = float(sys.argv[2])  # henter 3.
    c = float(sys.argv[3])  # henter 4.
    
except IndexError:
    print("Du har glemt en verdi, skriv verdiene igjen for a, b og c i kommando feltet:")
    a = float(input("velg en verdi for a:"))    # input en verdi for a    
    b = float(input("velg en verdi for b:"))    # input en verdi for b
    c = float(input("velg en verdi for c:"))    # input en verdi for c

# For å gjøre koden enklere for maskinen og for å finne potensielle
# komplekse røtter finner vi alt under kvadratroten, slik:
y = b**2-4*a*c 

if y == 0:    # vis roten er 0 får man kun en løsning
    x = (-b+math.sqrt(b**2-4*a*c))/2*a
    print("liningen har kun en løsning:", x)
elif y < 0:       # vis roten blir <0 vil man få en kompleks likning
    print("likningen er kompleks") 

else:           # vis roten er 0< får man 2 løsninger
    x1 = (-b+math.sqrt(y))/2*a
    x2 = (-b-math.sqrt(y))/2*a
    print("likningen har løsningene:", x1, " and", x2)


"""
Terminal> python.exe quadratic_roots_error.py

"""