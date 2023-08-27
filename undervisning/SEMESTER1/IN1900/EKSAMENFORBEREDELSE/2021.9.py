from math import factorial, asin
def arcsin_approx(x, N):
    s= 0
    for n in range(N+1):
        s += (factorial(2*n)/(2**(2*n)*factorial(n)**2))*((x**(2*n+1))/(2*n+1))
    return s

alist = []
x=0.5


for i in range(1,20+1):
    print(f"{i}  {arcsin_approx(x,i)}  {abs(asin(0.5)-(arcsin_approx(x,i)))}")







    """
for i in range(1,20+1):
    alist.append(arcsin_approx(x,i))

for k in range(0,20,3):
    if k<len(alist)-2:
        print(f"{alist[k]}, {alist[k+1]}, {alist[k+2]}\n")
    elif k > len(alist)-3:
        print(f"{alist[18]}, {alist[19]}")
    else:
        break

"""