import matplotlib.pyplot as plt
import numpy as np
class RightTriangle:
    def __init__(self,x1,y1):
        self.x = x1
        self.y = y1
        if x1<0 or y1<0:
            raise ValueError
        self.z = np.sqrt(x1**2 + y1**2)

    def plot_triangle(self):
        x = [0, self.x, 0, 0, self.x, 0]
        y = [0, 0, 0, self.y, 0, self.y]
        plt.plot(x,y)
        plt.axis("equal")
        plt.show()

T1 = RightTriangle(1,2)
T2 = RightTriangle(2,4)

T2.plot_triangle()

print(T1.z)
print(T2.z)


"""
Terminal> python.exe right_triangle.py
plot
"""