N = 15
F = [1, 1]
for k in range(N-2):
    F.append(F[k]+F[k+1])
print(F)

"""
Terminal> python.exe fibbonacci.py