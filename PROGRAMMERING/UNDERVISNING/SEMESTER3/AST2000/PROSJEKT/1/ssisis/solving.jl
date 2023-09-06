using DifferentialEquations
using Plots

r_0 =8150177
v_0 =0

f_t =108636491
ϕ   =1.5e+04
μ_r =5_000_000
G   =6.674e-11
μ_p =1.03e25

function rocket(du, u, p, t)
    r, v = u
    f_t, μ_r, ϕ, G, μ_p =p
    du[1] =v
    du[2] =f_t/(μ_r-ϕ*t)-G*μ_p/r^2
end

p = [f_t, μ_r, ϕ, G, μ_p]
u_0 = [r_0, v_0]
tspan = (0.0, 1000.0)

prob = ODEProblem(rocket, u_0, tspan, p)
sol = solve(prob, Rodas5())

target_velocity = sqrt(2*6.674e-11*1.03e25*8150177)

plot(sol, vars=1, xlabel="Time (s)", ylabel="Height (m)", label="r(t)", title="Rocket Height")
#plot(sol, vars=2, xlabel="Time (s)", ylabel="Velocity (m/s)", label="v(t)", title="Rocket Velocity")