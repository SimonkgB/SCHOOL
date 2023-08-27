import numpy as np
x = np.linspace(1,10,101)
y = np.log(x)
print(x,y)

"""
Terminal> python.exe fill_log_vectroized.py
[ 1.    1.09  1.18  1.27  1.36  1.45  1.54  1.63  1.72  1.81  1.9   1.99
  2.08  2.17  2.26  2.35  2.44  2.53  2.62  2.71  2.8   2.89  2.98  3.07
  3.16  3.25  3.34  3.43  3.52  3.61  3.7   3.79  3.88  3.97  4.06  4.15
  4.24  4.33  4.42  4.51  4.6   4.69  4.78  4.87  4.96  5.05  5.14  5.23
  5.32  5.41  5.5   5.59  5.68  5.77  5.86  5.95  6.04  6.13  6.22  6.31
  6.4   6.49  6.58  6.67  6.76  6.85  6.94  7.03  7.12  7.21  7.3   7.39
  7.48  7.57  7.66  7.75  7.84  7.93  8.02  8.11  8.2   8.29  8.38  8.47
  8.56  8.65  8.74  8.83  8.92  9.01  9.1   9.19  9.28  9.37  9.46  9.55
  9.64  9.73  9.82  9.91 10.  ] [0.         0.0861777  0.16551444 0.2390169  0.3074847  0.37156356
 0.43178242 0.48858001 0.54232429 0.59332685 0.64185389 0.68813464
 0.73236789 0.77472717 0.81536481 0.85441533 0.89199804 0.9282193
 0.96317432 0.99694863 1.02961942 1.0612565  1.0919233  1.12167756
 1.15057203 1.178655   1.20597081 1.23256026 1.25846099 1.28370777
 1.30833282 1.33236602 1.35583515 1.37876609 1.40118297 1.42310833
 1.44456327 1.46556754 1.4861397  1.50629715 1.5260563  1.54543258
 1.56444055 1.58309394 1.60140574 1.61938824 1.63705308 1.65441128
 1.6714733  1.68824909 1.70474809 1.72097929 1.73695123 1.75267208
 1.7681496  1.78339122 1.79840401 1.81319475 1.82776991 1.84213568
 1.85629799 1.87026253 1.88403475 1.89761986 1.91102289 1.92424865
 1.93730177 1.95018671 1.96290773 1.97546895 1.98787435 2.00012773
 2.01223279 2.02419307 2.03601198 2.04769284 2.05923883 2.07065304
 2.08193842 2.09309787 2.10413415 2.11504997 2.12584791 2.13653051
 2.14710019 2.15755932 2.16791019 2.17815501 2.18829595 2.19833507
 2.20827441 2.21811594 2.22786155 2.2375131  2.24707238 2.25654115
 2.26592111 2.2752139  2.28442112 2.29354435 2.30258509]
"""