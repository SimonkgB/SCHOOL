#a)
def read_person_data(filename):     # lager en funksjon 
    with open(filename,"r") as infile:
        main_dict = {}      #lager en dic med navn main_dict
        secc_dict = {}      #-----""---------------
        for line in infile:
            # man kan også lage en ny for-loop for det under men jeg bruker de tfor å forstå alt bedre
            name = line.split(",")[0].strip()       # splitter ved "," og tar første verdi og kaller den name 
            age = line.split(",")[1].strip()        # --------------""---------
            gender = line.split(",")[2].strip()     # --------------""----------
            secc_dict.update({"age":age,"gender":gender})   #oppdaterer dict med nye [keys] og verdier
            main_dict.update({name:secc_dict})      # Opdaterer maindict med navn som key og verdiene er fra secc_dict
        print(main_dict)
        infile.close()      # lukker filen
            
a = read_person_data("readperson.txt")

#b)
main_dict = read_person_data("readperson.txt")  # lager en funskjon
def write_person_data(data_dict, filename):  
    outfile = open(filename, "w")   # åpner en fil og bruker w for "write"
    #Lage en for loop som grå gjennom dic-en
    # eks for data in main_dict:  da kan man bruke dict[data] fra en n ested list  så kan man dra ut dict[data][age]
    for i in range(data_dict):
        data = str(data_dict)
        outfile.write(f"{data} \n")     # i fila skriver data som jeg ikke har laga enda og hopper til neste linje 
write_person_data(main_dict, "person_data.txt")

write_person_data(a, "readperson.txt")