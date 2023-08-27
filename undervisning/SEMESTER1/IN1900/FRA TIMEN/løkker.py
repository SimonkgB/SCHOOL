# høyde = 180
# vekt = 75.5
# adresse = "Andeby"
# # print("Høyden er %d centimeter" %høyde)
# # print("vekten er %f kilo" % vekt)
# # print("vekten er %5.2 kilo" % vekt)
# #%5.2 betyr 5 plasser og 2 er desimaller

# #Bedre måte å gjøre det på ved bruk av f-strings
# #f sier at stringen innholder en placeholder bruk {feks}

# print(f"Høyden er {høyde} centimeter")
# print(f"vekten er {vekt:5.2f} kilo")
# print(f"Hun bor i {adresse}")
# print(f"Hun bor i {adresse:>10s}")
# print(f"Hun bor i {adresse:<10s}")

# a=2
# while a < 50:
#     print(a)
#     a = a*2


C= -20

while C <= 40:
    F = 9/5 * C + 32
    print(f"{C:3.1f} {F:3.1f}")
    C = C + 5

# x = 0
# y = 0
# while x < 3 and y < 3:
#     print(f"x+y = {x+y:d}")
#     x = x + 1
#     y = 2*y + x
    
# x = 0
# y = 0
# while x <= 2 or y < 2:
#     print(f"x+y = {x+y:d}")
#     x = x + 1
#     y = 2*x + 2
    
# The use of and will always give false if true and false 
# The use of or will always give true if true or false 

# for use of multiple variables use [feks, feks1, "feks2", -2.34, "pi"]

# a = [3.14, 3.1415926, 999999]
# print(len(a))     #says number of elements in list
# print(a[0])       #Use iduvidual elements in the list  NB! starts at 0
# print(a[1])
# print(a[2])

# a.append(99)   #add another element to the list
# print(a)

# a = a + [100, 200]    #merge a from previous string and add 100 and 200 to the end
# print(a)

# a.insert(2, -99)    #place -99 in the number 2 slot 
# print(a)

# del a[2]      #delete number element 2 in list
# print(a)


# a = [-10, -5, 0, 5 , 10]
# print (a.index(10))          #Says where in the list number 10 first comes up

# b = [1, 2, 1]
# print(b.index(1))
# print(b.count(1))

# k1 = b.index(1)
# k2 = b.index(1, k1+1)    #tell where the string start searchs for the next 1
# print(k1, k2)

# a = [-10, -5, 0, 5, 10]     #Doesnt work
# print(a[-10])
# print(a[-5])


# g = [-20, -15, -10, 5, 0]
# for C in g:
#     F = (9.0/5) * C + 32
#     print(f"{C:3.1f} {F:3.1f}")

# The next 2 strings does the same task

# minliste = [0, 2, 4]
# for x in minliste:
#     print(x**2)

# k = 0
# while k < len(minliste):
#     x = minliste[k]
#     print(x**2)
#     k += 1







