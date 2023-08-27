# import math
# import numpy as np

#ikke vektorisert:
# # bruk av lister
# from math import sin
# x = [k/10 for k in range(0,11)]
# y = [sin(e) for e in x]

# # bruk av numpy

# from math import sin
# import numpy as np
# x = np.linspace(0,1,11)
# y = np.zeros(11)
# for k in range(11):
#     y[k] = sin(x[k])

# vektorisert og numpy
import numpy as np
x = np.linspace(0,1,11)
y = np.sin(x)


#fra liste til array
x = [1,2,3]
a = np.array(x)

#fra array til liste
a = np.linspace(0,5,100)
x = list(a)







