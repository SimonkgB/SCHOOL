using Plots

# Define constants
g = 9.81  # Acceleration due to gravity (m/s^2)
L1 = 1.0  # Length of first rod (m)
L2 = 1.0  # Length of second rod (m)
m1 = 1.0  # Mass of first bob (kg)
m2 = 1.0  # Mass of second bob (kg)

# Define initial conditions
θ1₀ = π/2   # Initial angle of first rod (rad)
θ2₀ = π/2   # Initial angle of second rod (rad)
ω1₀ = 0.0   # Initial angular velocity of first rod (rad/s)
ω2₀ = 0.0   # Initial angular velocity of second rod (rad/s)

# Define simulation time and time step
t = 0:0.01:10
Δt = t[2] - t[1]

# Define function to calculate derivatives of state variables
function derivatives(θ1, θ2, ω1, ω2)
    dθ1 = ω1
    dθ2 = ω2
    dω1 = (m2*L1*ω1^2*sin(θ1-θ2)*cos(θ1-θ2) +
           m2*g*sin(θ2)*cos(θ1-θ2) +
           m2*L2*ω2^2*sin(θ1-θ2) -
           (m1 + m2)*g*sin(θ1)) /
          (L1*(m1 + m2*sin(θ1-θ2)^2))
    dω2 = (-m2*L2*ω2^2*sin(θ1-θ2)*cos(θ1-θ2) +
            (m1 + m2)*(g*sin(θ1)*cos(θ1-θ2) -
            L1*ω1^2*sin(θ1-θ2) -
            g*sin(θ2))) /
          (L2*(m1 + m2*sin(θ1-θ2)^2))
    return [dθ1, dθ2, dω1, dω2]
end

# Define function to solve double pendulum using Runge-Kutta method
function solve_double_pendulum(θ1₀, θ2₀, ω1₀, ω2₀, t)
    θ1_values = [θ1₀]
    θ2_values = [θ2₀]
    ω1 = ω1₀
    ω2 = ω2₀
    for i in 2:length(t)
        k1 = Δt*derivatives(θ1_values[i-1], θ2_values[i-1], ω1, ω2)
        k2 = Δt*derivatives(θ1_values[i-1]+k1[1]/2, θ2_values[i-1]+k1[2]/2, ω1+k1[3]/2, ω2+k1[4]/2)
        k3 = Δt*derivatives(θ1_values[i-1]+k2[1]/2, θ2_values[i-1]+k2[2]/2, ω1+k2[3]/2, ω2+k2[4]/2)
        k4 = Δt*derivatives(θ1_values[i-1]+k2[1]/2, θ2_values[i-1]+k3[2]/2, ω1+k3[3]/2, ω2+k3[4]/2)
        θ1_new = θ1_values[i-1] + (k1[1] + 2*k2[1] + 2*k3[1] + k4[1])/6
        θ2_new = θ2_values[i-1] + (k1[2] + 2*k2[2] + 2*k3[2] + k4[2])/6
        ω1 += (k1[3] + 2*k2[3] + 2*k3[3] + k4[3])/6
        ω2 += (k1[4] + 2*k2[4] + 2*k3[4] + k4[4])/6
        push!(θ1_values, θ1_new)
        push!(θ2_values, θ2_new)
    end
    return θ1_values, θ2_values
end

# Solve double pendulum
θ1_values, θ2_values = solve_double_pendulum(θ1₀, θ2₀, ω1₀, ω2₀, t)

# Convert polar coordinates to Cartesian coordinates
x1 = L1*sin.(θ1_values)
y1 = -L1*cos.(θ1_values)
x2 = x1 + L2*sin.(θ2_values)
y2 = y1 - L2*cos.(θ2_values)

# Plot double pendulum motion
plot(x1, y1, color=:blue, aspect_ratio=:equal, xlims=(-2,2), ylims=(-2,2), label="First Pendulum")
plot!(x2, y2, color=:red, label="Second Pendulum")
