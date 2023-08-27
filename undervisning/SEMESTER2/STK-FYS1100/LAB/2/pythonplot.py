import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

data = np.loadtxt("data.txt", delimiter=",")
print(data)


x = data[:,0]
y = data[:,1]

print(x,y)


slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

n = len(x)
t_value = stats.t.ppf(0.975, n-2)
x_mean = np.mean(x)
x_std = np.std(x, ddof=1)
y_pred = slope*x + intercept
y_err = y - y_pred
s_err = np.sqrt(np.sum(y_err**2) / (n-2))
pred_int = t_value * s_err * np.sqrt(1/n + (x_mean - x)**2 / ((n-1)*x_std**2))
print(pred_int)

plt.scatter(x, y_err)
plt.axhline(y=0, color="r", linestyle="-")
plt.xlabel("x")
plt.ylabel("Residualer")
plt.show()
