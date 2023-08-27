import os
from julia import Julia

# Set the JULIA_HOME environment variable
julia_home = "C:/Users/simon/AppData/Local/Programs/Julia-1.8.5"
os.environ["JULIA_HOME"] = julia_home

# Initialize the Julia interpreter
jl = Julia()

# Include and execute a Julia script
jl.include("julia_test.jl")

# Access and call the Julia function
julia_factorial = jl.eval("calculate_square")
result = julia_factorial(5)
print(f"Factorial of 5 calculated in Julia: {result}")
