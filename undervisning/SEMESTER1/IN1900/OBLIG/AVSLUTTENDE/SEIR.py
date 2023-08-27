import numpy as np
import matplotlib.pyplot as plt
from ODESolver import RungeKutta4

# NB! "Gidder ikke" å forklare alt som skjer. antar at det er greit

#a)
class ProblemSEIR:
    def __init__(self, beta, r_ia = 0.1, r_e2=1.25, \
    lmbda_1=0.33, lmbda_2=0.5, p_a=0.4, mu=0.2):
        if isinstance(beta, (float, int)):
            self.beta = lambda t: beta
        elif callable(beta):
            self.beta = beta

        self.r_ia=r_ia; self.r_e2=r_e2; self.lambda_1 = lmbda_1; self.lmbda_2 = lmbda_2; self.p_a =p_a; self.mu = mu


    def set_initial_condition(self, S_0,E_2):       # setter initial betingelsene inn i en lista
        self.initial_condition = [S_0, 0, E_2, 0, 0, 0]
        return self.initial_condition
        

    def get_population(self):
        return self.initial_condition[0] + self.initial_condition[2]       # etter som kun den første verdien i lista og den tredje "eksisterer" kan man bare addere de

    
    def __call__(self, u, t):
        beta = self.beta(t); r_ia =0.1; r_e2=1.25; lmbda_1=0.33; lmbda_2=0.5; p_a=0.4; mu=0.2

        S, E1, E2, I, Ia, R = u
        N = sum(u)
        dS = -beta*S*I/N - r_ia*beta*S*Ia/N - r_e2*beta*S*E2/N
        dE1 = beta*S*I/N + r_ia*beta*S*Ia/N + r_e2*beta*S*E2/N - lmbda_1*E1
        dE2 = lmbda_1*(1-p_a)*E1 - lmbda_2*E2
        dI = lmbda_2*E2 - mu*I
        dIa = lmbda_1*p_a*E1 - mu*Ia
        dR = mu*(I + Ia)
        return [dS, dE1, dE2, dI, dIa, dR]


#b)
def test_ProblemSEIR():     
    u_list=[1, 1, 1, 1, 1, 1]   
    t = 0
    P1 = ProblemSEIR(0.4) 
    P1.set_initial_condition(5E6, 100)
    computed1 = P1.set_initial_condition(5E6, 100)      # computed er hva koden får som "svar"
    expected1 = [5E6, 0, 100, 0, 0, 0]             # expected er verdiene jeg har fått oppgitt som svaret, eller har regnet ut selv
    computed2 = P1.get_population()
    expected2 = 5000100
    computed3 = P1(u_list, t)
    expected3 = [-0.156666666666, -0.1733333333333, -0.302, 0.3, -0.068, 0.4]
    tol = 1E-5
    msg = "OOpsie.."

    expected_pop = abs(computed2-expected2) < tol
    success = expected_pop

    for i in range(len(u_list)):        # for loop, for å teste alle verdiene  i listene 
        if (abs(expected3[i] - computed3[i]) > tol):
            success = False         # abs(expec-comp) vil for hver enkel verdi i listene  sette success som false,  vis en av verdiene er større en toleransen

        if abs(computed1[i]- expected1[i]) > tol:
            success = False # se linje 60

    assert success, msg

#c)
class SolverSEIR:
    def __init__(self, P1, T, dt):          # konstruktør
        self.P1 = P1; self.T = T; self.dt = dt
    
    def solve(self, method = RungeKutta4):      # importerer rungeKutta4 fra ODESolver
        solve = method(self.P1)
        solve.set_initial_condition([5E6, 0, 100, 0, 0, 0]) # de bestemte initialverdiene 
        self.step_size = int(self.T / self.dt)
        t = np.linspace(0, self.T, self.step_size)
        u, t = solve.solve(t)
        return u, t
    
    def plot(self, states):         # plotter alle verdiene 
        u, t = SolverSEIR.solve(self)
        S = u[:,0]; I = u[:,3]; Ia = u[:,4]; R = u[:,5]
        if "S" in states:               # sjekker om "S/I osv." er i lista, og vis den er det plottes den 
            plt.plot(t, S, label="S")
        if "I" in states:
            plt.plot(t, I, label="I")
        if "Ia" in states:
            plt.plot(t, Ia, label="Ia")
        if "R" in states:
            plt.plot(t, R, label="R")
        plt.show()


if __name__ == "__main__":      # hvis programmet importes som en modul, vil ikke denne kjøres
    test_ProblemSEIR()
    
    S_0 = 5e6           
    E2_0 = 100
    problem = ProblemSEIR(beta=0.4)
    problem.set_initial_condition(S_0,E2_0)
    solver = SolverSEIR(problem,T=150,dt=1.0)
    solver.solve()
    solver.plot(["S","I","Ia","R"])



"""
Terminal> python.exe SEIR.py
# "Se plot"
"""