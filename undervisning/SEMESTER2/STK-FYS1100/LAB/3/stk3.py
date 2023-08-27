import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2
import scienceplots
import scipy.stats as stats

with open("filename.txt","r") as infile:
    a=[]
    b =[]
    infile.readline()
    for line in infile:
        row = line.strip().split(',')
        a.append(float(row[0]))
        b.append(float(row[1]))
    infile.close()
arrayA=np.array(a)
arrayB=np.array(b)


slope, intercept, r_value, p_value, std_err = stats.linregress(arrayA, arrayB)

# Skriv ut resultatene
print("slope:", slope)
print("intercept:", intercept)
print("r-squared:", r_value**2)
res = stats.linregress(arrayA, arrayB)
plt.plot(arrayA, res.intercept + res.slope*arrayA, 'r', label='fitted line')
plt.show()


"""


plt.style.use(["notebook", "grid"])

plt.figure(figsize=(10,5))
plt.hist(arrayA, bins = 10,color="blue",label="density function")  #density gjør histogrammet om til et denisty plot
plt.xlabel("ulike siffere")
plt.ylabel("antall")
plt.title("RNG between (0,9)")
plt.legend()
plt.show()

"""

df = 1

alpha = 0.05

critical_value = stats.chi2.ppf(q=1-alpha, df=df)

observed_values = arrayA
expected_values = [10, 20, 20, 20, 20]
chi_square_statistic, p_value = stats.chisquare(observed_values, expected_values)

print(f"Degrees of freedom: {df}")
print(f"Significance level: {alpha}")
print(f"Critical value: {critical_value}")
print(f"Chi-square statistic: {chi_square_statistic}")
print(f"P-value: {p_value}")
