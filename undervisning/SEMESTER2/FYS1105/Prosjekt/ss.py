import numpy as np
import matplotlib.pylab as plt

# Define your matrix and initial conditions
A = np.array([[1, 2], [3, 4]])
x0 = np.array([1, 1])

# Define the time step dt
dt = 0.01

# Define a function that computes the derivative of the matrix at a given time step
def deriv(A, x):
    return np.dot(A, x)

# Use a loop to iterate through each time step and update the matrix using the Euler-Chromer method
t = np.arange(0, 1, dt)
x = np.zeros((len(t), len(x0)))
x[0, :] = x0

for i in range(1, len(t)):
    x[i, :] = x[i-1, :] + dt * deriv(A, x[i-1, :])
    A = A + dt * np.outer(x[i, :], x[i-1, :])

# Store the results in an array
results = np.hstack((t[:, np.newaxis], x))
print(results)

plt.plot(results[0],t)
plt.show()