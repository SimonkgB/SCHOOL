import numpy as np
from numpy import sin, cos, pi, exp, log
import matplotlib.pyplot as plt

end_t = 3

if 1: # a)
  f = lambda x : 2*sin(pi*x)
  g = lambda x : -sin(2*pi*x)
  analytic = lambda x,t : 2*sin(pi*x)*cos(pi*t)-1/(2*pi)*sin(2*pi*x)*sin(2*pi*t)
else: # b)
  f = lambda x : x*(1-x)
  g = lambda x : 0
  def analytic(x, t):
    r = 0
    for k in range(1,201):
      r += 8/(pi**3*(2*k-1)**3) * sin((2*k-1)*pi*x) * cos((2*k-1)*pi*t)
    return r


def shift(x, k):
  # return [(x[i+k] if 0 <= i+k < len(x) else 0) for i in range(len(x))] #Equivalent but slower
  r = np.zeros(len(x))
  if k > 0: r[:-k] = x[k:]
  else: r[-k:] = x[:k]
  return r


r = 1

n_list = [10,20,50,100,200]
errs = []
for n in n_list:
  dx = 1/(n+1)
  x = np.linspace(dx,1-dx,n)
  dt = dx*r

# Make sure end_t is a grid point
  steps = int(end_t/dt+1)
  dt = end_t / steps

  v0 = f(x)
  v1 = v0 + dt*g(x) + 2*dt**2/dx**2 * (shift(v0,-1)-2*v0+shift(v0,1))
  v = [v0, v1]

  for i in range(steps-1):
    new_v = 2*v[-1] + dt**2/dx**2 * (shift(v[-1],-1)-2*v[-1]+shift(v[-1],1)) - v[-2]
    v.append(new_v)

  errs.append(np.max(np.abs(v[-1]-analytic(x,end_t))))
  if n == 100:
    plt.plot(x, v[-1], label='Numeric')
    plt.plot(x, analytic(x, end_t), label='Analytic')
    plt.legend()
    plt.show()

plt.loglog(n_list, errs, label='numeric')
plt.loglog(n_list, 1/np.array(n_list)**2, label='rate 2')
plt.loglog(n_list, 1/np.array(n_list)**3, label='rate 3')
plt.legend()
plt.show()