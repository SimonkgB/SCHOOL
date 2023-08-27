import sys # alt man skriver etter programnavnet legges i en liste med navn 

#print(sys.argv)
F= sys.argv[0]      #Må bruke inn i commando vinduet

F = float(F)

C = (F-32)*(5/9)
print(f"{F} blir {C}")