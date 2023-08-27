import numpy as np

# def extract_data(filename):
#     with open(filename, "r") as infile: # Åpner fila og leser dataen i den
#         vlist = [] # lager en "variabel" liste, (som jeg kaller det)
#         infile.readline()   # Hopper over den første linja 
#         for line in infile: 
#             word = line.split() # splitter alle linjene, dataen blir lagret i "word"
#             for n in range(len(word)):
#                 vlist.append(float(word[n])) # putter in verdiene lagret i "word" in i vlist
#         return vlist
# f1 = extract_data("temp_oct_1945.txt")  # putter in filen in i def'en over som lager en liste vi kaller f1
# f2 = extract_data("temp_oct_2014.txt")  # samme som linje 12 bare ny liste f2


# f1_mean = np.mean(f1)   # Regner ut gjennomsnittet og gir den et navn
# f1_min = np.min(f1)     # regner ut min "deviation" av lista 
# f1_max = np.max(f1)     # regner ut max "deviation" av lista

# f2_mean = np.mean(f2)   # samme som forklart over 
# f2_min = np.min(f2)
# f2_max = np.max(f2)


# print(f"Oct_1945: Mean = {f1_mean:.2f} ; Min = {f1_min} ; Max = {f1_max}")
# print(f"Oct_2014: Mean = {f2_mean:.2f} ; Min = {f2_min} ; Max = {f2_max}")

# # b)
# def write_formatting(filename, list1, list2):
#     with open(filename, "a") as outfile:  # skriver variabelen blir filen "filename". Man bruker heller a (append), fordi vi ikke skal skrive i dokumentet, men heller appende fra et annet
#         outfile.write("Oct_1945:  Oct_2014:" + "\n" + "\n")  # lager overskrift til tabellen
#         for i in range(len(f1)):  # Vis vi antar at lengdene i begge filene er like kan vi brue i til å "ta med" / "velge" alt innholdet vi vil ha fra txt
#             outfile.write(f"{list1[i]:4} {list2[i]:6}")  # skriver ut alle verdiene i txt fila
#             outfile.write("\n")  # velger ny linje. Så starter for loopen om igjen

# write_formatting("temp_formatted.txt", f1, f2)

# """
# Terminal> python.exe temp_read_write.py
# Oct_1945: Mean = 6.51 ; Min = 2.1 ; Max = 11.6
# Oct_2014: Mean = 8.85 ; Min = 2.3 ; Max = 13.6
# """











def extract_data(filename):
    with open(filename, "r") as infile: # Åpner fila og leser dataen i den
        vlist = []# lager en "variabel" liste, (som jeg kaller det)
        for line in infile:
            word = line.split() # splitter alle linjene, dataen blir lagret i "word"
            for x in range(0,4):
                q = (filename[x])
            infile.readline()   # Hopper over den første linja 
            for n in range(len(word)):
                vlist.append(float(word[n])) # putter in verdiene lagret i "word" in i vlist
        return vlist
f1 = extract_data("temp_oct_1945.txt")  # putter in filen in i def'en over som lager en liste vi kaller f1
f2 = extract_data("temp_oct_2014.txt")  # samme som linje 12 bare ny liste f2


f1_mean = np.mean(f1)   # Regner ut gjennomsnittet og gir den et navn
f1_min = np.min(f1)     # regner ut min "deviation" av lista 
f1_max = np.max(f1)     # regner ut max "deviation" av lista

f2_mean = np.mean(f2)   # samme som forklart over 
f2_min = np.min(f2)
f2_max = np.max(f2)


print(f"{q}: Mean = {f1_mean:.2f} ; Min = {f1_min} ; Max = {f1_max}")
print(f"Oct_2014: Mean = {f2_mean:.2f} ; Min = {f2_min} ; Max = {f2_max}")

# b)
def write_formatting(filename, list1, list2):
    with open(filename, "a") as outfile:  # skriver variabelen blir filen "filename". Man bruker heller a (append), fordi vi ikke skal skrive i dokumentet, men heller appende fra et annet
        outfile.write("Oct_1945:  Oct_2014:" + "\n" + "\n")  # lager overskrift til tabellen
        for i in range(len(f1)):  # Vis vi antar at lengdene i begge filene er like kan vi brue i til å "ta med" / "velge" alt innholdet vi vil ha fra txt
            outfile.write(f"{list1[i]:4} {list2[i]:6}")  # skriver ut alle verdiene i txt fila
            outfile.write("\n")  # velger ny linje. Så starter for loopen om igjen

write_formatting("temp_formatted.txt", f1, f2)

"""
Terminal> python.exe temp_read_write.py
Oct_1945: Mean = 6.51 ; Min = 2.1 ; Max = 11.6
Oct_2014: Mean = 8.85 ; Min = 2.3 ; Max = 13.6
"""






































