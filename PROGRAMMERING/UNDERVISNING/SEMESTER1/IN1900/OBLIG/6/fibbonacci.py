N = 15
F = [1, 1]
for k in range(N-2): # en range som går fra 0 til 13 ettersom de 2 første verdiene er 1 
    F.append(F[k]+F[k+1])   # adderer sammen sifere og appender de in i en liste
    
"""
Terminal> python.exe fibbonacci.py
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
"""