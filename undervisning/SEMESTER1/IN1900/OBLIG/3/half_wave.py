import math


def f(n):
    if math.sin(n)>0:   # Verdien må være mer enn null
        return math.sin(n)  # finner sin verdi av n
    else:
        return 0 # sier at vis verdien er negativ eller 0 vil den returneres som 0

def test_f():
    computed1 = f(3)    # vi setter n=3
    computed2 = f(6)    # n=6
    expected1 = 0.141120008 # Verdien til f(3)
    expected2 = 0           # siden den ikke er positiv setter vi den som null begrunnet i def over
    tolerance = 1.0*math.exp(-20)       # pga python vil ikke svarene alti være "riktige" derfor har men en toleranse 
    success1 = abs(computed1 - expected1) < tolerance
    success2 = abs(computed2 - expected2) < tolerance
    message = "ettersom f <=0 bli den fjernet"  #Feil melding vis expected ikke er riktig
    assert success1, message    # Vis Expected 1 er riktig eller ca riktig innenfor tolleransen er det en sukses vis ikke får vi tilbake en feilmelding 
    assert success2, message    # Samme som i linje 19, bare ang. success2
test_f()

"""
Terminal> py.exe half_wave.py

"""







