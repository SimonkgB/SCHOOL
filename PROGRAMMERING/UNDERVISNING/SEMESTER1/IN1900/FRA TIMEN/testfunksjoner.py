# def skriv_ut():
#     print("Hello world")

# skriv_ut()



# def skriv_ut(tekst):
#     print(tekst)

# skriv_ut("Hello world")



# def regn_ut(x):
#     y = x**2 + 2*x + 1
#     return y
# print(10)



# def f(x):
#      y = x**2 + 2*x +1
#      return x,y
# x0, y0 = f(10)
# print(y0)



# def f(x):
#     return x**2

# def g(x):
#     return f(x)**3

# print(g(2))



# def f(n):
#     v = 1
#     for i in range(2,n+1):
#         v = v*i
#     return v
# print(f(4))



# def f(x,y):     #inputs i en funksjonsdefinisjon kalles parametere
#     return x+y
# a=0
# b=1
# verdi = f(a,b)  #inputs i et funksjonskall kalles argumenter




# def f(x,y):
#     return x+y

# verdi= f(0)         #ikke lovlig
# verdi= f(0,1)       #lovlig
# verdi= f(0, 1, 2)   #ikke lovlig
# # Må ha like mange argumenter som parametere i funksjon

# def f(x,y,z=2):
#     return x+y
# verdi= f(0)         #ikke lovlig
# verdi= f(0,1)       #lovlig
# verdi= f(0, 1, 2)   #lovlig

# def f(x, y=0, z=0):     #Lovlig
#     print(x+y+z)

# def f(x, y=0, z):       #Ikke lovlig
#     print(x+y+z)        #Default parameterene må stå bakerst i lista

# def f(x=0, y, z):       #Ikke lovlig
#     print(x+y+z)        #Default parameterene må stå bakerst i lista


# def f ( x , y , z ):
#     return x + y + z



# verdi = f (x=0, y=1, z=2) # Lovlig
# verdi = f (0, y=1, z=2)   # Lovlig
# verdi = f (0, z=2, y=1)   # Lovlig
# verdi = f (z=2, 0, 1)     # Ikke lovlig



# def f(*args):       # * VIKTIG
#   # Nå er args et tuppel
#   for k in args:
#       print (k)
# f()    #Lovlig
# f(0)   #Lovlig
# f(0,1) #Lovlig





#Funksjon som skal finne produktet av alle
#verdiene i en liste
def prod(a):
    result = 1
    for e in a:
        result = result * e
    return result
# Vi lager en testfunksjon :


def test_prod():
    a = [3, 1, 5]
    computed = prod(a)                  # Eksempel på inputverdi for a
    expected = 15                       # Faktisk output fra prod
    success = (computed == expected)    # Forventet output fra prod
    message = "prod gir feil svar!"
    assert success, message
# Vi kaller på testfunksjonen :

test_prod()





# def prod(a):
#     result = 1
#     for e in a :
#         result = result * e
#     return result


# def test_prod():
#     inputs = [[3, 1, 5], [2, 4, 5], [1, 0]] #Gjennomfører flere tester
#     answers = [15 , 40 , 0 ]
#     for i in range(len(inputs)):
#       computed = prod(inputs[i])
#       expected = answers[i]
#       success = (computed == expected)  #kan fortasatt for data feil selv om riktig
#       message = "prod gir feil svar"
#       assert success, message
# # Vi kaller på testfunksjonen :
# test_prod()





# def test_prod():
#     inputs = [[3.1, 1.1, 5.2], [2.2, 4.0, 5.9]]
#     answers = [17.732, 51.92]
#     tolerance = 1e-10
#     for inp, expected in zip(inputs, answers):
#       computed = prod(inp)
#       success = abs(computed-expected) < tolerance
#       message = "prod gir feil svar"
#       assert success, message



