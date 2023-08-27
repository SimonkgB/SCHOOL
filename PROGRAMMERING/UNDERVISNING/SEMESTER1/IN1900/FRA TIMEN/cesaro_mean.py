import math

"""
to måter å løse oppgava på
"""

for n in range(0,10):    #Assuming 0 is the first number
    C = (math.factorial(2*n))/(math.factorial(n+1)*(math.factorial(n)))
    print(C)


def a(n):
    C = (math.factorial(2*n))/(math.factorial(n+1)*(math.factorial(n)))
    return C
r_number = float(input("what do you want as a cesaro's number?"))
print(a(r_number))
    