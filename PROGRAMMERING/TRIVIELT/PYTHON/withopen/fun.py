import numpy as np
import os
import time
import random


filename = input("he: ")

if os.path.isfile(filename) == True:         #hele if statementen sjekker om første som står i file er time, vis det er det
    with open (f"{filename}", "r") as infile:     # appender vi med "a"
        a=[]                                        # vis ikke så writer vi nytt med "w"
        for line in infile:
            a.append(line.split(","))
        if a[0][0]=="time":
            mode = "a"
        else:
            mode = "w"

else:                   # vis fila ikke eksisterer lager vi en ny en med "x"
    mode = "x"


with open (f"{filename}", mode) as infile:
    infile.write("posision\n")
    for i in range(20):
        infile.write(f"{random.randint(0,9)}\n")
    infile.close()