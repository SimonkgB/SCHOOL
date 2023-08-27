using DifferentialEquations, Plots

# Define the ODE
f(u,p,x) = 3x^2 * (u^2 + 1)

# Initial conditions
u0_values = [0.0, 0.5, 1.0]

# Interval of integration (for example, from x = 0 to x = 2)
tspan = (-0.6, 0.6)

# Create a new plot
p = plot()

for u0 in u0_values
    # Define the problem with the current initial condition
    prob = ODEProblem(f, u0, tspan)

    # Solve the problem
    sol = solve(prob)

    # Add the solution to the plot
    plot!(sol)
end

title!(p, "Solution to the ODE")
xaxis!(p, "x")
yaxis!(p, "y(x)")

# Display the plot
display(p)

x = range(0, 3, 100)

h = \sec ^2\left(x^3+1\right)\cdot \:3x^2

plot(x, h)