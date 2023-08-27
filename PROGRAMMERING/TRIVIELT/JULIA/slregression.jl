using CSV, GLM, Plots, TypedTables
#=
data = CSV. File("housingdata.csv")

X = data.size
Y = round.(Int, data.price / 1000)

t = Table(X=X,Y=Y)

gr(size = (600,600))

p_scatter = scatter(X,Y,
    xlims = (0, 5000),
    ylims = (0,800),
    xlabel = "Size (sqft)",
    ylabel = "Price (in thouands of dollars)",
    title = "housing Prices in Portland",
    legend = false,
    color = :red
)

#using glm t ofind a linear regressoon

ols = lm(@formula(Y ~ X), t)

plot!(X, predict(ols), color=:green, linewidth = 3)

newX = Table(X = [1250])

predict(ols, newX)
=#
###########################
# machine learning approch
###########################

epochs = 0

gr(size = (600,600))

p_scatter = scatter(X,Y,
    xlims = (0, 5000),
    ylims = (0,800),
    xlabel = "Size (sqft)",
    ylabel = "Price (in thouands of dollars)",
    title = "housing Prices in Portland (epochs= $epochs)",
    legend = false,
    color = :red
)

theta_0 = 0.0
theta_1 = 0.0

h(x)= theta_0 .+ theta_1 * x

plot!(X, h(X), color = :blue, linewidth = 3)

# cost function

m = length(X)
y_hat = h(X)
function cost(X,Y)
    (1/(2*m))*sum((y_hat-Y).^2)
end

J = cost(X, Y)

J_history = []
push!(J_history, J)


function pd_theta_0(X,Y)
    (1/m)*sum((y_hat - Y))
end

function pd_theta_1(X,Y)
    (1/m)*sum((y_hat - Y).*X)
end

alpha_0 = 0.09
alpha_1 = 0.00000008

theta_0_temp = pd_theta_0(X,Y)
theta_1_temp = pd_theta_1(X,Y)

theta_0 -= alpha_0 * theta_0_temp

theta_1 -= alpha_1 * theta_1_temp

y_hat = h(X)
J = cost(X,Y)
push!(J_history,J)

epochs +=1
plot!(X, y_hat, color =:blue, 
    alpha = 0.5,
    linewidth = 3,
    title = "housing prices in portland (epochs = $epochs)"
)
