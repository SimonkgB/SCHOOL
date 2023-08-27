import julia

# Specify the Julia executable (adjust the path accordingly)
julia.install("C:/Users/simon/AppData/Local/Programs/Julia-1.8.5/bin/julia.exe")

jl = julia.Julia(runtime="C:/Users/simon/AppData/Local/Programs/Julia-1.8.5/bin/julia.exe")

# Transfer data from Python to Julia
data = [1.0, 2.0, 3.0]
jl.data = data


# Continue from the previous Python code

# Include the Julia script
jl.include("C:/Users/simon/Dokumenter/PROGRAMMERING/PYTHON/SHIT/JULIA-PY/diffsol.jl")

# Import the results from Julia
results = jl.sol

# Print the results
print("Results from Julia:", results)
