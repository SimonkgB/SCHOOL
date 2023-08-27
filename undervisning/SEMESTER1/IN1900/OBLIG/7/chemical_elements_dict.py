
elements_10 = {     
    1:"-",
    2:"Helium",
    3:"Lithium",
    4:"Beryllium",
    5:"Boron",
    6:"Carbon",
    7:"Nitrogen",
    8:"-",
    9:"Fluoride",
    10:"Neon"
}       # skriver ned alt i oversiklig rekkefølge

elements_10[1] = "Hydrogen"
elements_10[8] = "Oxygen"


elements_10_copy = elements_10.copy()   # lager en kopi av elements_10 og kaller de nelements_10_copy
elements_10_copy.update({11: "Sodium"}) # oppdaterer "dic" med et nytt "argument?"
print(elements_10)

print("\n")

elements_11 = elements_10   # sier at e_11 er lik e_10 for å så bruke e_11 
elements_11.update({11: "Sodium"}) # oppdaterer "dic" med et nytt "argument?"
print(elements_10)
# De første printer bare ut det vi har fra før. Hadde det derrimot stått; Print(elements_10_copy) ville koden kjørt likt


"""
Terminal> python.exe atm_moon.py
{1: 'Hydrogen', 2: 'Helium', 3: 'Lithium', 4: 'Beryllium', 5: 'Boron', 6: 'Carbon', 7: 'Nitrogen', 8: 'Oxygen', 9: 'Fluoride', 10: 'Neon'}
"""