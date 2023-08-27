def extract_data(filename):
    infile = open("Oxygen.txt", "r") # open file
    infile.readline()
    Isotope = []
    Weight = []
    Natural_abundance = []
    for line in infile:
        word = line.split()
        Isotope.append(word[0])
        Weight.append(float(word[1]))
        Natural_abundance.append(float(word[2]))
    infile.close()
    m = 0
    for i in range(len(Isotope)):
        mi = Weight[i]
        wi = Natural_abundance[i]
        m += mi*wi
    return m

data = extract_data("Oxygen.txt")

print(f"{data:2.4f}")





"""
Terminal> python.exe read_file_isotopes.py
15.9994
"""