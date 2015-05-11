import random
import sys
import math
def drop_needle(L):
    x=random.random()
    a=random.vonmisesvariate(0,0)
    if L<=1:
        if x+L*math.cos(a)<=0 or x+L*math.cos(a)>=1 or x==0 or x==1:
            z=True
        else:
            z=False
    return z
def recurse(N):
    if N>0:
        y=drop_needle(L)
        if y==True:
            t.append(y)
        x=random.random()
        a=random.vonmisesvariate(0,0)
        recurse(N-1)
        return t
L=float(sys.argv[2])
N=int(sys.argv[1])
t=[]
if len(sys.argv)<=2:
    print('Use:  estimate_pi.py N L')
if len(sys.argv)==3:
    if float(sys.argv[2])>1:
        print('AssertionError: L should be smaller than 1')
    if float(sys.argv[2])<=1:
        recurse(N)
        h=len(t)
        Pi= (2*L*N)/h
        print(str(h), ' hits in ' , sys.argv[1], ' tries ')
        print('Pi = ', str(Pi))

        