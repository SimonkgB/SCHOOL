using DifferentialEquations
using Plots

j = Array{100}

function g(x)
    tan(x^3 + pi/4)
end

plot(g, -1, 1)

function k(du, u, p, t)
    u = x, y

    du = 3*x^2 * (y^2 + 1)
    
end