
using PyPlot

# Define a function to calculate the approximation of Euler's number
function approximate_euler(n)
    return (1+1/n)^n
end

# Define a function to calculate the approximation of Pi
function approximate_pi(n)
    s = 0.0
    for i in 0:n
        s += ((-1)^i)/(2*i+1)z
    end
    return 4s
end

# Define the range of values of n to use for approximation
n_range = 0:0.01:100

# Calculate the approximations for Euler's number and Pi
euler_approximations = approximate_euler.(n_range)
pi_approximations = approximate_pi.(n_range)

# Plot the approximations
plot(n_range, euler_approximations, label="Euler's number")
plot(n_range, pi_approximations, label="Pi")

# Add labels and title to the plot
xlabel("n")
ylabel("Approximation")
title("Approximating Euler's number and Pi")

print()