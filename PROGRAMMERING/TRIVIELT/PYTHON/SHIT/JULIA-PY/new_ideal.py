import julia

# Specify the Julia executable (adjust the path accordingly)
julia.install("C:/Users/simon/AppData/Local/Programs/Julia-1.9.2/bin/julia.exe")

# Start the Julia runtime
from julia import Julia
jl = Julia(runtime="C:/Users/simon/AppData/Local/Programs/Julia-1.9.2/bin/julia.exe")

# Load and execute the Julia script from a separate file
jl.include("new.jl")

# Call the Julia function from Python
result = jl.eval("julia_square(5)")
print("Result from Julia:", result)
