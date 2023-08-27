using DifferentialEquations, Plots,ImageMagick, PlutoUI;plotly()

function double_pendulum(du, u, p, t)
	theta1, theta2, omega1, omega2 = u
	m1, m2, L1, L2, g = p
	c = cos(theta1 - theta2)
	s = sin(theta1 - theta2)

	du[1] = omega1
	du[2] = omega2
	du[3] = (-g * (2 * m1 + m2) * sin(theta1) -
		m2 * g * sin(theta1 - 2 * theta2) -
		2 * s * m2 * (omega2^2 * L2 + omega1^2 * L1 * c)) /
		(L1 * (2 * m1 + m2 - m2 * cos(2 * theta1 - 2 * theta2)))
	du[4] = (2 * s * (omega1^2 * L1 * (m1 + m2) +
		g * (m1 + m2) * cos(theta1) +
		omega2^2 * L2 * m2 * c)) /
		(L2 * (2 * m1 + m2 - m2 * cos(2 * theta1 - 2 * theta2)))
	
end

t_span=(0.0, 10.0)

theta1 = 90
theta2 = 90
theta1 = deg2rad(theta1)
theta2 = deg2rad(theta2)
u_0 = [theta1, theta2, 0, 0]

m1 = 1
m2 = 2
L1 = 1
L2 = 1
p = [m1, m2, L1, L2, 9.81]

prob = ODEProblem(double_pendulum, u_0, t_span, p)
sol = solve(prob)

plot(sol,
	linewidth = 1.5
)

function polar2cart(sol; vars = (1, 2))

	idx = sol.t[1]:0.01:sol.t[end]

	p1 = map(x -> x[vars[1]], sol.(idx))
	p2 = map(y -> y[vars[2]], sol.(idx))

	x1 = L1 * sin.(p1)
	y1 = -L1 * cos.(p1)

	x2 = L2 * sin.(p2)
	y2 = -L2 * cos.(p2)

	((x1, y1), (x1 + x2, y1 + y2))
	
end

pendulum1, pendulum2 = polar2cart(sol)

x1 = pendulum1[1][end]
y1 = pendulum1[2][end]
x2 = pendulum2[1][end]
y2 = pendulum2[2][end]

phase_x1y1 = plot(pendulum1,
	legend = false,
	title = "Double Pendulum Phase Space x1 y1",
	xaxis = "x",
	yaxis = "y",
	formatter = :plain,
	widen = true,
	xlims = (-4, 4),
	ylims = (-4, 4),
	aspect_ratio = 1.1
);


phase_x2y2 = plot(pendulum2,
	legend = false,
	title = "Double Pendulum Phase Space x2 y2",
	xaxis = "x",
	yaxis = "y",
	formatter = :plain,
	widen = true,
	xlims = (-4, 4),
	ylims = (-4, 4),
	aspect_ratio = 1.1
);


begin
	plot!(phase_x2y2,
		([0, x1, x2], [0, y1, y2]),
		color = :black,
		linewidth = 2
	);
	scatter!(phase_x2y2,
		([0, x1, x2], [0, y1, y2]),
		color = [:black, :green, :red],
		markersize = 4
	)
end