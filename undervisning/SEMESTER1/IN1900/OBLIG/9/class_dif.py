import numpy as np
import matplotlib.pyplot as plt

class Diff:     # lager en class med navn diff
    def __init__(self, f):  # lager en constructor (viktig ha med self i en class)
        self.f = f      
                                # de neste funskjonene er måter å approksimere den deriverte
    def der1(self, x, h):       # lager en funksjon i classen
        return (self.f(x+h)-self.f(x))/h    # funksjonen

    def der2(self, x, h):
        return (self.f(x+h)-self.f(x-h))/(2*h)

    def der3(self, x, h):
        return (-self.f(x+2*h)+8*self.f(x+h)-8*self.f(x-h) + self.f(x-2*h))/(12*h)


x = np.linspace(-1,1,500)   
h = (0.9, 0.6, 0.3, 0.1)        # 4 forskjellige unøyaktigheter (egntlig vil man ha den så liten som mulig)

f = Diff(lambda x:np.sin(2*np.pi*x))    # lambda er en måte man kan få en funksjon inn på en linje 
fdev = 2*np.pi*np.cos(2*np.pi*x)    # den faktiske verdien til funksjonen vår 

                                # for å plotte alt i forskjellige grafer
for i in range(len(h)):     
    plt.subplot(4,1,i+1)
    plt.plot(x,fdev, label="Eksakt")
    plt.plot(x,f.der1(x,h[i]), label="første funksjon") # ettersom jeg gir de en label kan de bli vanskelige å se med lav resulusjon
    plt.plot(x,f.der2(x,h[i]), label="andre funksjon")
    plt.plot(x,f.der3(x,h[i]), label="tredje funksjon")
    plt.legend()
plt.show()

"""
Terminal> python.exe class_dif.py
se plot
"""