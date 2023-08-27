M_C = 12.011
M_H = 1.0079
l = 9

print("Molekyl:  Mm:")
for n in range(2, l+1):
    m = 2*n+2
    molar_mass = n*M_C+m*M_H
    print(f"M(C{n}H{m}) = {molar_mass:6.3f} g/mol") 


"""
Terminal> py.exe alkane.py
Molekyl:  Mm:
M(C2H6) = 26.069 g/mol
M(C3H8) = 38.096 g/mol
M(C4H10) = 50.123 g/mol
M(C5H12) = 62.150 g/mol
M(C6H14) = 74.177 g/mol
M(C7H16) = 86.203 g/mol
M(C8H18) = 98.230 g/mol
M(C9H20) = 110.257 g/mol
"""