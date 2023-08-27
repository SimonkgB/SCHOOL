import numpy as np

x_test_values = [0.699, 0.703, 0.698, 0.688, 0.701]

#a)
def mean(x_list):
    s=0
    for i in range(len(x_list)):
        s += x_list[i]  
    mean = s / len(x_list)      # funksjonen
    return mean



#b)
def test_mean():                # tester hva vi fant i a
    computed = mean(x_test_values)
    expected = np.mean(x_test_values)
    tolerance = 1e-69
    success = abs(computed-expected) < tolerance  
    message = "wrong"
    assert success, message
test_mean()

#c)
def standard_deviation(x_list):
    s=0
    for i in range(len(x_list)):
        s += (x_list[i] - mean(x_test_values))**2   #finner verdien til delen etter summerings tegnet
    k = np.sqrt((1/len(x_list)) * s)       # bruker sqrt til numpty og legger til s til det som er før summerings tegnet
    return k

#d)
def test_standard_deviation():          #tester ha vi fant i c
    computed = standard_deviation()
    expected = 0.005192301994298872
    tolerance = -1e-69
    success =abs(computed - expected < tolerance)
    message = "wrong" 
    assert success, message
    
"""
Terminal> py.exe statistics.py
time: population:
0    5000
4    9913
8   17749
12   27526
16   36580
20   42924
24   46552
28   48390
32   49263
36   49666
40   49849
44   49932
48   49970
