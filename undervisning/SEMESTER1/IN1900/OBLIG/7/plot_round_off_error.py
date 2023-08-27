# This program is needed in Problem 7.5 Interpret output from a program.

from math import sin, cos, pi

def f(x):
	return sin(x)

def df_approx(f, x, delta_x):
	print(delta_x, f(x+delta_x)- f(x))
	return (f(x+delta_x)-f(x))/delta_x
    #return (f(x+delta_x)-f(x-delta_x))/(2*delta_x)



x = pi/3
for n in range(1, 20):
    delta_x = 10**(-n)
    calculated = df_approx(f, x, delta_x)
    exact = cos(x)
    rel_err = abs(calculated - exact)/abs(exact)
    abs_err = abs(calculated - exact)

#     print("delta_x: %e, df_approx: %13.10e, df_exact: %13.10e, abs_error: %e, \
# 		   rel_error: %e, n=%d" % (delta_x, calculated, exact, abs_err, rel_err, n))




import numpy as np
a_deltax = np.array(delta_x)
a_calculated = np.array(calculated)
a_exact = np.array(exact)
a_abserr = np.array(abs_err)
a_relerr = np.array(rel_err)
a_n = np.array(n)

#np.savetxt("arrayss.txt",a_n)

# with open("arrayss.txt", "x") as infile:
#     infile.write(str(n))
                 