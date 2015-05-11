import random
import sys
import math

if len(sys.argv)<=2:
    print('Use:  estimate_pi.py N L')
if len(sys.argv)==3:
    if float(sys.argv[2])>1:
        print('AssertionError: L should be smaller than 1')