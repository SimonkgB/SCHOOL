from cmath import sqrt
a = 6
b = -5
c = 1

x_1 = (-b + sqrt((b)**2 - 4 * a * c))/(2*a)
x_2 = (-b - sqrt((b)**2 - 4 * a * c))/(2*a)

print(f"Man får 2 røtter til x, de er {x_1:3.2f} og {x_2:3.2f}")