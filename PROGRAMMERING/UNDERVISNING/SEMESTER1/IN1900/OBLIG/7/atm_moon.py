def extract_data(filename):
    with open(filename,"r") as infile:
        infile.readline()   # hopper over den første linja
        dic = {} # lager en dictionary og kaller den dic
        particle = []   # lager en liste kalt particle
        density = []
        for line in infile:
            words = line.split(";")      # splitter alt ved ; og lagrer det i words
            for i in range(len(words)):
                particle = words[i].split("-")[0]   # splitter ved "-" og bruker den første "verdien og setter den inn som particles
                density = words[i].split("-")[1]    # gjør det samme som den over bare for en annen verdi
                particle = particle.strip()         # fjerner tegn i particles 
                density = density.strip()           # samme som over
                density = density.replace(",", "")  # bytter "," med " "
                dic.update({particle:density})      #Setter inn key og value
            
        infile.close()      # lukker filen
    return dic
      
    
print(extract_data("atm_moon.txt"))

"""
Terminal> python.exe atm_moon.py
{'Helium 4': '40000', 'Neon 20': '40000', 'Hydrogen': '35000',
 'Argon 40': '30000', 'Neon 22': '5000', 'Argon 36': '2000',
  'Methane': '1000', 'Ammonia': '1000', 'Carbon Dioxide': '1000'}
"""

