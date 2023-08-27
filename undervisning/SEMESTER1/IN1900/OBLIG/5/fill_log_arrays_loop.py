import numpy as np

def f(x):               # lager en funksjon
    return np.log(x)    

[a,b] = [1,10]      # fra 1 tol 10
n = 101
interval = (b-a)/n  #lager et intervall med 101 punkter spredt mellom 1 og 10

x = np.zeros(n)       # lager en array med 101 nuller 
y = np.zeros(n)       # --------------"--------------
for i in range(n):
    x[i] = a + i * interval     # lager en array med ne verdier 
    y[i] = f(x[i])              # laer en array, der verdiene man får i x blir satt in i funksjonen
     
print(x,y)

"""
Terminal> python.exe fill_log_loop.py
[1.         1.08910891 1.17821782 1.26732673 1.35643564 1.44554455
 1.53465347 1.62376238 1.71287129 1.8019802  1.89108911 1.98019802
 2.06930693 2.15841584 2.24752475 2.33663366 2.42574257 2.51485149
 2.6039604  2.69306931 2.78217822 2.87128713 2.96039604 3.04950495
 3.13861386 3.22772277 3.31683168 3.40594059 3.4950495  3.58415842
 3.67326733 3.76237624 3.85148515 3.94059406 4.02970297 4.11881188
 4.20792079 4.2970297  4.38613861 4.47524752 4.56435644 4.65346535
 4.74257426 4.83168317 4.92079208 5.00990099 5.0990099  5.18811881
 5.27722772 5.36633663 5.45544554 5.54455446 5.63366337 5.72277228
 5.81188119 5.9009901  5.99009901 6.07920792 6.16831683 6.25742574
 6.34653465 6.43564356 6.52475248 6.61386139 6.7029703  6.79207921
 6.88118812 6.97029703 7.05940594 7.14851485 7.23762376 7.32673267
 7.41584158 7.5049505  7.59405941 7.68316832 7.77227723 7.86138614
 7.95049505 8.03960396 8.12871287 8.21782178 8.30693069 8.3960396
 8.48514851 8.57425743 8.66336634 8.75247525 8.84158416 8.93069307
 9.01980198 9.10891089 9.1980198  9.28712871 9.37623762 9.46534653
 9.55445545 9.64356436 9.73267327 9.82178218 9.91089109]
[0.         0.08535985 0.16400298 0.23690975 0.30486041 0.3684861
 0.4283046  0.48474591 0.53817108 0.58888617 0.63715291 0.68319685
 0.72721374 0.76937455 0.8098295  0.84871129 0.88613769 0.92221375
 0.95703352 0.99068155 1.02323415 1.05476041 1.08532306 1.11497927
 1.14378126 1.17177686 1.19901001 1.22552114 1.25134754 1.27652369
 1.30108155 1.32505074 1.34845883 1.37133149 1.39369267 1.41556474
 1.43696865 1.45792402 1.47844925 1.49856166 1.51827753 1.53761218
 1.55658008 1.57519489 1.59346951 1.61141615 1.62904638 1.64637117
 1.66340091 1.68014548 1.69661429 1.71281627 1.72875992 1.74445335
 1.7599043  1.77512015 1.79010794 1.80487441 1.819426   1.83376888
 1.84790894 1.86185185 1.87560302 1.88916766 1.90255076 1.91575711
 1.92879133 1.94165784 1.9543609  1.96690462 1.97929294 1.99152967
 2.00361847 2.01556287 2.02736628 2.039032   2.0505632  2.06196294
 2.0732342  2.08437982 2.09540259 2.10630518 2.11709019 2.12776012
 2.1383174  2.14876439 2.15910337 2.16933655 2.17946606 2.189494
 2.19942238 2.20925315 2.21898822 2.22862943 2.23817858 2.2476374
 2.25700758 2.26629079 2.2754886  2.28460259 2.29363426]
"""