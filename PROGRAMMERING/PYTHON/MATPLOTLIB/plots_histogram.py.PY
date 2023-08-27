import numpy as np
import matplotlib.pyplot as plt
import scienceplots #used in pyplot
plt.style.use(["science", "notebook", "grid"])

##########################
# plots
"""
x = np.linspace(0,15,100)
y = np.sin(x)+ 0.1*np.random.randn(len(x))

x2 = np.linspace(0,15,100)
y2 = np.sin(x)

plt.figure(figsize =(10,6))
plt.plot(x,y,"o", color="purple", lw=0.7, ms=4.6, label="component1")
plt.plot(x2,y2,"-", color="green", lw=0.7, ms=5, label="component2")
plt.xlabel("Time (s)")
plt.ylabel("voltage [V]")
plt.ylim(top =1.5,bottom=-0.5)
plt.legend(loc="upper right", fontsize=10, ncol=2)
plt.show()
"""
###############################
###############################
# histograms
res1 = np.random.randn(1000)*0.2+0.4
res2 = np.random.randn(1000)*0.2+0.4
plt.figure(figsize=(8,4))
plt.hist(res1, bins = 30,density=True, histtype="step")
plt.hist(res2, bins = 30,density=True, histtype="step")   #density gjør histogrammet om til et denisty plot
plt.show()

###############################