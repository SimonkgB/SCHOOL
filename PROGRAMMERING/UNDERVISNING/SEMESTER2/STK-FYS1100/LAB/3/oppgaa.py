import numpy as np
import matplotlib.pyplot as plt
import scienceplots
import scipy.stats as stats
import math as mt
import scipy


with open("tester_med_litengreie.txt","r") as infile:
    a=[]
    infile.readline()
    for line in infile:
        a.append(float(line))
    infile.close()
b = sorted(a, key = lambda x:float(x))
arr=np.array(b)

def normal_dist(x, mean, std):
    return (1/(std*np.sqrt(2*np.pi))*np.exp(-0.5*((x-mean)/std)**2))

mean = np.mean(arr)
print(mean)
std = np.std(arr)
p = std**2/len(arr)
pdf = normal_dist(arr, mean, std)

def poisson(mean, n):
    y = ((mean**n)/(scipy.special.factorial(n)))*np.exp(-mean)
    return y

x = np.linspace(0,20,100)


print(mean, std**2)

#print(f"Integralet til tetthetsfunksjonen = {np.sum(poisson(mean,x)*(arr[len(arr)-1]-arr[0])/(len(arr)-1))}")

plt.style.use(["notebook", "grid"])

plt.figure(figsize=(10,7))
(n, bins, _) = plt.hist(arr, bins =13,range=(0,13),color="blue",label="", density = True)
plt.plot(x, poisson(mean,x),color="red")

#plt.axvline(c,linestyle="dashed", label="teoretisk svingetid", color="green")
#plt.plot(arr,pdf,label="Normal fordeling", color="red",linewidth=3)
plt.xlim(0,20)
plt.xlabel("Henfall/10sek")
plt.ylabel("Henfall/10sek tetthet")
plt.title("henfall per sek")
plt.legend()
plt.show()




df = 1

alpha = df/2

critical_value = stats.chi2.ppf(q=1-alpha, df=df)

observed_values = n
expected_values = poisson(mean,bins[:-1])
chi_square_statistic, p_value = stats.chisquare(observed_values, expected_values)

print(f"Degrees of freedom: {df}")
print(f"Significance level: {alpha}")
print(f"Critical value: {critical_value}")
print(f"Chi-square statistic: {chi_square_statistic}")
print(f"P-value: {p_value}")