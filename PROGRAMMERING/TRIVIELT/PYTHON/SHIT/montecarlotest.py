import random as rd
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sc

def f(x):
    return np.cos(x)

def g(x):
    return x

def monte_carlo_area(a, b, n):
    count = 0

    for _ in range(n):
        x = rd.uniform(a, b)
        ymin = min(f(a), f(b))
        ymax = max(f(a), f(b))
        y = rd.uniform(min(-1, ymin), ymax)

        if g(x) <= y <= f(x):
            count += 1
            plt.scatter(x, y)

    area = (count / n) * (b - a) * max(f(a), f(b))
    return area


# Example usage:
lower_limit = 0
upper_limit = 0.739085
num_points = 2000

estimated_area = monte_carlo_area(lower_limit, upper_limit, num_points)
print("Estimated area under the curve:", estimated_area)

p = (np.abs(lower_limit) + np.abs(upper_limit))*(np.abs(f(lower_limit))+np.abs(f(upper_limit)))
print(estimated_area/p)


yy = np.linspace(lower_limit,upper_limit,100)
plt.plot(yy, f(yy))
plt.plot(yy,g(yy))
plt.show()