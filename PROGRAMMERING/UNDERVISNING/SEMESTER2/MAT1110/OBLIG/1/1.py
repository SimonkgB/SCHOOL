import numpy as np

#a)
v_1 = np.array([1, 1, 1])
v_2 = np.array([1, 1, -2])
v_3 = np.array([1, -1, 0])

if np.dot(v_1, v_2) & np.dot(v_1,v_3) & np.dot(v_2,v_3) ==0:
    print("Alle vinkelene er vinkelrette på hvrandre")

"""
Terminal> Python.exe> 1.py
Alle vinkelene er vinkelrette på hvrandre
"""

#c)
A = np.transpose(np.array([v_1,v_2,v_3]))
B = np.linalg.inv(A)

print(np.dot(B,v_1))
print(np.dot(B,v_2))
print(np.dot(B,v_3))

"""
Terminal> Python.exe> 1.py
[1. 0. 0.]
[1.11022302e-16 1.00000000e+00 0.00000000e+00]
[0. 0. 1.]
"""