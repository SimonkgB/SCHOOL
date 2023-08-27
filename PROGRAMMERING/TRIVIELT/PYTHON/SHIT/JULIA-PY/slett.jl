using DifferentialEquations

function solve_exponential_growth(u0, tspan, aa)
    function exponential_growth(du, u, p, t)
        du[1] = p * u[1]
    end

    prob = ODEProblem(exponential_growth, u0, tspan, aa)
    sol = solve(prob)
    return sol
end