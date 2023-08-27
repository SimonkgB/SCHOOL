from math import sqrt

class Coords:               # lager en class med navn Coords
    def __init__(self, x, y, z):    # setter variabler som x,y,z
        self.x = x
        self.y = y
        self.z = z
                                        # vidre bruker vi mange spesielle metoder
    def __str__(self):      # brukes for string
        return f"({self.x:3.2f}, {self.y:3.2f}, {self.z:4.2f})"
    
    def __len__(self):  # her skal koden finne lengden på close som er 3, men jeg får ikke gjort dette "rikig" så jeg hard-coder 3 
        return 3

    def __abs__(self):  # bruker for absoluttverdi
        return sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __add__(self, other):       # brukes for addisjon
        return Coords(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):       # brukes for å subtraktere
        return Coords(self.x - other.x, self.y - other.y, self.z - other.z)


sqrt3 = sqrt(3)     # bare en variabel
close = Coords(1/sqrt3, 1/sqrt3, 1/sqrt3)       #kordinater med x, y, z som man setter in i classen
far = Coords(3/sqrt3, 15/sqrt3, 21/sqrt3)       # ------""---------

print(close)
print(far)

print(f"The class represents coordinates in {len(close)} dimensions")
print(f"The distance from the centre to the point close is {abs(close)}")
print(f"The distance from the centre to the point far is {abs(far)}")


further = close + far
print(f"The coordinates further are at {further}")
distance = abs(far - close)
print(f"The distance from far to close is {distance}")
centre = further - further
print(f"The coordinates at the centre are {centre}")


"""
Terminal> python.exe coords.py
(0.58, 0.58, 0.58)
(1.73, 8.66, 12.12)
The class represents coordinates in 3 dimensions
The distance from the centre to the point close is 1.0
The distance from the centre to the point far is 15.000000000000002
The coordinates further are at (2.31, 9.24, 12.70)
The distance from far to close is 14.142135623730953
The coordinates at the centre are (0.00, 0.00, 0.00)
"""