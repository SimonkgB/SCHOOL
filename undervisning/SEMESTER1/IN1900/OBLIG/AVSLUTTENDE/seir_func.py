import numpy as np
import matplotlib.pyplot as plt

# NB! "Gidder ikke" å forklare alt som skjer. antar at det er greit

def SEIR(u,t):          # importer funksjonen fra oppgava
    beta=0.4; r_ia =0.1; r_e2=1.25; lmbda_1=0.33; lmbda_2=0.5; p_a=0.4; mu=0.2
    S, E1, E2, I, Ia, R = u
    N = sum(u)
    dS = -beta*S*I/N - r_ia*beta*S*Ia/N - r_e2*beta*S*E2/N
    dE1 = beta*S*I/N + r_ia*beta*S*Ia/N + r_e2*beta*S*E2/N - lmbda_1*E1
    dE2 = lmbda_1*(1-p_a)*E1 - lmbda_2*E2
    dI = lmbda_2*E2 - mu*I
    dIa = lmbda_1*p_a*E1 - mu*Ia
    dR = mu*(I + Ia)
    return [dS, dE1, dE2, dI, dIa, dR]


def test_SEIR():        # lager en test funskjon 
    tol = 1E-10
    success = True
    computed = SEIR([1, 1, 1, 1, 1, 1], 0)          # computed er hva koden får som "svar"
    expected = [-0.156666666666, -0.1733333333333, -0.302, 0.3, -0.068, 0.4]    # expected er verdiene jeg har fått oppgitt som svaret, eller har regnet ut selv
    for i in range(len(expected)):
        if abs(expected[i] - computed[i]) > tol:
            success = False     # abs(expec-comp) vil for hver enkel verdi i listene  sette success som false,  vis en av verdiene er større en toleransen
    msg = f"Her er det noe feil, expected {expected},\n computed: {computed}"
    assert success, msg

test_SEIR()

#b)
from ODESolver import RungeKutta4

def solve_SEIR(T, dt, S_0, E2_0):
    solver = RungeKutta4(SEIR)      # importerer Rungekutta4 fra ODESolver
    t = np.arange(0, T+dt, dt)
    solver.set_initial_condition([S_0, 0, E2_0, 0, 0, 0]) 
    return solver.solve(t)


#c)
def plot_SEIR(u, t):        # plotter funksjonen
    y, tid = solve_SEIR(t,1,u[0],u[2])  
    S = []; I = []; Ia = []; R =[]  # lager flere lister
    for i in y:     # for loopen henter ut alle verdiene fra y og under appender/ setter de inn i de nye listene
        S.append(i[0])
        I.append(i[3])
        Ia.append(i[4])
        R.append(i[5])

    plt.plot(tid,S,label="S")
    plt.plot(tid,I,label="I")
    plt.plot(tid,Ia,label="Ia")
    plt.plot(tid,R,label="R")
    plt.legend()
    plt.show()


plot_SEIR([5e6,0,100,0,0,0],150)        # plotter med variabler og tid


"""
Terminal> python.exe seir_func.py
# "Se plot"
"""