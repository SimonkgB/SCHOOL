using DifferentialEquations
function rober!(du,u,p,t)
    y_1,y_2,y_3 = u
    k_1,k_2,k_3 = pdu
    du[1] = -k_1*y_1+k_3*y_2*y_3
    du[2] = k_1*y_1-k_2*y_2^2-k_3*y_2*y_3
    du[3] = k_2*y_2^2
    nothing
end

u_0 = [1.0,0.0,0.0]
tspan = (0.0,1e5)
params = [0.04,3e7,1e4]

ode_prob = ODEProblem(rober!, u_0, tspan, params)

ode_sol = solve(ode_prob)
print(ode_sol)
using Plots
Plots.plot(ode_sol, tspan = (1e-6,1e5) xscale =:log10, layout=(3,1)) 