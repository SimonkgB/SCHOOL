using DifferentialEquations
using Plots

function rocket(du, u, p, t)
    r, v = u
    f_t, μ_r, ϕ, G, μ_p = p
    du[1] = v
    du[2] = f_t / (μ_r - ϕ * t) - G * μ_p / r^2
end

p = [8690919.0 * 4, 5_000_000.0, 1.36584652e4, 6.674e-11, 1.03e25]
u_0 = [8150177.0, 0.0]
tspan = (0.0, 1000.0)

prob = ODEProblem(rocket, u_0, tspan, p)
sol = solve(prob, Rodas5(), abstol=1e-8, reltol=1e-8)

target_velocity = sqrt(2 * 6.674e-11 * 1.03e25 * 8150177)

plot(sol, vars=1, xlabel="Time (s)", ylabel="Height (m)", label="r(t)", title="Rocket Height")
plot!(sol, vars=2, xlabel="Time (s)", ylabel="Velocity (m/s)", label="v(t)", title="Rocket Velocity")
