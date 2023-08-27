import math
class Quadratic():      # lager en class med navn Quadratic
    def __init__(self, coefficients):       # lager en constuktør
        self.coeff = coefficients

    def __call__(self, x):      # bruker den spesielle metoden "call" som vi kan bruke til funksjoner
        s=0
        for i in range(len(self.coeff)):    # en for loop som går igjennom lengden til coeff/coeficients
            s += self.coeff[i]*x**i     # legger sammen alle verdiene, der x verdiene blir samtidig opphøyd for hvor de er i loopen 
        return s

    def __str__(self):      # en spesiell metode man bruker når man skal skrive noe i en string
        s = ""  # lager en string uten noe informasjon
        for i in range(0, len(self.coeff)):     # det videre er veldig likt hva som skjer i "call" funksjonen
            if self.coeff[i] != 0:
                s += f" + {self.coeff[i]:g}*x**{i:g}"  # i stringen laget tidligere legger vi til funskjonen laget de to tidligere linjene 
                                    # de neste linjene er bare en måte å gjøre tekst stringen ryddig og fjerner unødvendige "ting"
        s = s.replace("+ -", "- ")      
        s = s.replace(" 1*", " ")
        s = s.replace("x**0", "1")
        s = s.replace("x**1 ", "x ")
        if s[0:3] == " + ":
            s = s[3:]
        if s[0:3] == " - ":
            s = "-" + s[3:]
        return s

P1 = [2, 3, 1]          # lager en liste med variablene vi vil bruke
Polynomial = Quadratic(P1)  # setter lista inn i classen og gir den et navn
print(Polynomial)   
print(Polynomial(1))    # printer ut lista med x verdi = 1
print(Polynomial(2))


class Cubic(Quadratic):             # en sub class der vi utregener den deriverte
    def differentiate(self):
        for i in range(1, len(self.coeff)):     
            self.coeff[i-1] = i*self.coeff[i]       # ettersom cubic er en "fortsettelse" fra Quadratic har den samme variabler og vi emdre bare de 
        del self.coeff[-1]      # fjerner siste verdi
        return self.coeff

P2 = [2, 3, 1, 4]       # samme som på lije 28 bare for Cubic istedet
Poly = Cubic(P2)
print(Poly)
print(Poly(1))
print(Poly(2))
Poly.differentiate()
print(Poly)


"""
Terminal> python.exe polynomial.py
2*1 + 3*x + x**2
6
12
2*1 + 3*x + x**2 + 4*x**3
10
44
3*1 + 2*x + 12*x**2
"""