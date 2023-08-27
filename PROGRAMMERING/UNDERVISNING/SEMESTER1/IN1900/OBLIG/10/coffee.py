import numpy as np
import matplotlib.pyplot as plt
from ODESolver import ForwardEuler

def estimate_h(t1, Ts, T0, T1):
    return (T1 - T0)/(t1*(Ts - T0))

class Cooling:              #
    def __init__(self, h, T_s):
        self.h = h
        self.T_s = T_s

    def __call__(self, T, t):
        return -self.h * (T-self.T_s)



# b)

if __name__ == "__main__":

    def test_Cooling():             # lager en test funksjon...
        T_s = 20
        h = estimate_h(60, T_s, 90, 80)
        problem = Cooling(h, T_s)
        computed = problem(60, 100)
        expected = -0.0952380952
        tol = 1E-5
        success = abs(computed - expected) < tol
        msg = f"Oppsie..."
        assert success, msg
    
test_Cooling()


#c)
time_points = np.linspace(0, 2000, 1000)
T_s_list = [20, 25]

for i in range(len(T_s_list)):
    h = estimate_h(15, T_s_list[i], 95, 92)
    f = Cooling(h, T_s_list[i])
    P1 = ForwardEuler(f)
    P1.set_initial_condition(U0 = 95)
    u, t = P1.solve(time_points)
    plt.plot(t, u, label=f"T_S = {T_s_list[i]}")

plt.legend()
plt.show()

"""
Terminal> python.exe coffeee.py
# "Se plot"
"""