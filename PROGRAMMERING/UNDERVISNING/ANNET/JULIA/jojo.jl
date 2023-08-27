
x0 = 1.0   # initial displacement
v0 = 0.0   # initial velocity
m = 1.0    # mass
k = 1.0    # spring constant
dt = 0.01  # time step
tmax = 10.0  # maximum time

function acceleration(x)
    return -k/m * x
end

n= Int(round(tmax/dt))+1
x = zeros(n)
v = zeros(n)
x[1] = x0
v[1] = v0

for i in 1:n-1
    v[i+1] = v[i] + dt * acceleration(x[i])
    x[i+1] = x[i] + dt * v[i+1]
end


using Plots
plot(0:dt:tmax, x, xlabel="Time", ylabel="Position", legend=true)
