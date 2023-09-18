using DifferentialEquations, Plots

g = 4 * pi^2

function n_body!(du, u, p, t)
    n = length(p)
    for i in 1:n
        du[2*i-1] = u[2*n + 2*i-1]  # dx/dt = vx
        du[2*i]   = u[2*n + 2*i]    # dy/dt = vy
        ax, ay = 0.0, 0.0
        xi, yi = u[2*i-1], u[2*i]
        for j in 1:n
            if i != j
                xj, yj = u[2*j-1], u[2*j]
                r = sqrt((xi - xj)^2 + (yi - yj)^2)
                ax -= g * p[j] * (xi - xj) / r^3
                ay -= g * p[j] * (yi - yj) / r^3
            end
        end
        du[2*n + 2*i-1] = ax  # dvx/dt = ax
        du[2*n + 2*i]   = ay  # dvy/dt = ay
    end
end

# Initial conditions
# The Sun is the first body with a very large mass and zero initial velocity.
x_init  = [0.0, 1.0, 2.0]
y_init  = [0.0, 0.0, 0.0]
vx_init = [0.0, 0.0, 0.5]
vy_init = [0.0, 1.0, 0.5]
masses  = [1e6, 1.0, 1.0]  # Sun's mass is much larger

u0 = vcat(x_init, y_init, vx_init, vy_init)
tspan = (0.0, 10.0)

prob = ODEProblem(n_body!, u0, tspan, masses)
sol = solve(prob, Tsit5(), reltol=1e-4, abstol=1e-4)

# Plotting
plot(title="N-Body Problem", xlabel="x", ylabel="y", aspect_ratio=:equal)
for i in 1:length(masses)
    plot!(sol, vars=(2*i-1, 2*i), linewidth=2, label="Body $i")
end
display(plot)



#=
n = 3
u0 = [
0, 1.35897907, 1.35467118, -2.40141679,# -4.89723538, -3.37087, 0.04797701, 11.21620265    # x positions
0, 0.0, -1.23582801, -1.18833107,# -5.33049507, -1.9138109, -0.28910667, 5.77199413        # y positions
0, 0.0, 3.72165837, 1.97490595,# 1.91789032, 2.26974996, 13.62231746, -1.02070427  #vx velocities
0, 6.37508296, 4.0989842, -4.13351378 #-1.96199243, -3.06010066, 2.23993763, 1.84629397    #vy velocities
]


# Make sure to add 7 initial vx and 7 initial vy to u0 to make its length 4 * n = 28

masses = [1.4293965883833313, 9.86448020e-06, 2.32372811e-06, 8.23504061e-08, #1.36108732e-02, 2.88206510e-07, 4.37226345e-08, 2.69142194e-08]
]
tspan = (0.0, 1.28394067*109000)
=#