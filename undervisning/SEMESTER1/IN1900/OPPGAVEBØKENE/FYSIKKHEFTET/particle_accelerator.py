# a)
"""
m_e =9.11e-31
q_e = -1.63e-19
E = 2e-2
    
v_0 = float(input("Venligst angi en verdi for v_0:"))
t = float(input("Venligst angi en positiv verdi for t:"))   

if t < 0:
    ValueError
x = v_0*t + 1/2*(q_e*E)/(m_e)*t
v = v_0 + (q_e*E)/(m_e) * t

print(f"Verdien i x er:{x}, mens verdien til v er {v}")

"""

# b)
import sys

E = 2e-2
try:
    v_0 = float(sys.argv[1])
    m = float(sys.argv[2])
    t = float(sys.argv[3])
    q = float(sys.argv[4])

except:
    print("Du har oppgitt for få variabler")
    v_0 = float(input("Venligst angi en verdi for v_0:"))
    t = float(input("Venligst angi en positiv verdi for t:"))
    m = float(input("Venligst angi en verdi for m:"))
    q= float(input("Venligst angi en verdi for q:"))

if t < 0:
    ValueError
    print("Du har angitt en negativ verdi for t som ikke er mulig")
elif t > 0:    
    x = v_0*t + 1/2*(q*E)/(m)*t
    v = v_0 + (q*E)/(m) * t

print(f"Verdien i x er:{x}, mens verdien til v er {v}")
