import sys
import numpy

try:
    sys.argv[1]
    if sys.argv[1] == int(sys.argv[1]):
        print("int")
    elif sys.argv[1] != int(sys.argv[1]):
        print("str")
    else:
        print("L")


except:
    print("dne")