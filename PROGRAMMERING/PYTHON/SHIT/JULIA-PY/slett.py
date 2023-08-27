import julia

# Specify the Julia executable (adjust the path accordingly)
julia.install("C:/Users/simon/AppData/Local/Programs/Julia-1.9.2/bin/julia.exe")

# Start the Julia runtime
from julia import Julia
jl = Julia(runtime="C:/Users/simon/AppData/Local/Programs/Julia-1.9.2/bin/julia.exe")

# Load and execute the Julia script from a separate file
jl.include("slett.jl")
u0 = [1.0]         # Initial condition
tspan = (0.0, 2.0)  # Time span from t=0 to t=2
aa = 1.5     
# Call the Julia function from Python
result = jl.eval("solve_exponential_growth([1.0]  , (0.0, 2.0), 1.5  )")
print("Result from Julia:", result)
