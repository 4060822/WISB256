import random
import sys
import math
def drop_needle(L,M):
    x=t[M]
    a=s[M]
    if x+L*math.cos(a)<=0:
        z=True
    elif x+L*math.cos(a)>=1:
        z=True
    elif x==0:
        z=True
    elif x==1:
        z=True
    else:
        z=False
    return z
def recurse(N):
    if N>0:
        y=drop_needle(L,N-1)
        if y==True:
            f.append(y)
        recurse(N-1)
        return f
f=[]
if len(sys.argv)<=2:
    print('Use: ',sys.argv[0],' N L')
if len(sys.argv)==3:
    L=float(sys.argv[2])
    N=int(sys.argv[1])
    if float(sys.argv[2])>1:
        t=[x for x in range(0,N)]
        s=[x for x in range(0,N)]
        for i in range(0,N):
            t[i]=random.random()
            s[i]=random.vonmisesvariate(0,0)
        recurse(N)
        h=len(f)
        Pi= (2*L-2*(math.sqrt((L**2)-1)+math.asin(1/L)))/((h/N)-1)
        print(str(h), ' hits in ' , sys.argv[1], ' tries ')
        print('Pi = ', str(Pi))
    if float(sys.argv[2])<=1:
        t=[x for x in range(0,N)]
        s=[x for x in range(0,N)]
        for i in range(0,N):
            t[i]=random.random()
            s[i]=random.vonmisesvariate(0,0)
        recurse(N)
        h=len(f)
        Pi= (2*L*N)/h
        print(str(h), ' hits in ' , sys.argv[1], ' tries ')
        print('Pi = ', str(Pi))
if len(sys.argv)==4:
    L=float(sys.argv[2])
    N=int(sys.argv[1])
    if float(sys.argv[2])>1:
        seed=int(sys.argv[3])
        random.seed(seed)
        t=[x for x in range(0,N)]
        s=[x for x in range(0,N)]
        for i in range(0,N):
            t[i]=random.random()
            s[i]=random.vonmisesvariate(0,0)
        recurse(N)
        h=len(f)
        Pi= (2*L-2*(math.sqrt((L**2)-1)+math.asin(1/L)))/((h/N)-1)
        print(str(h), ' hits in ' , sys.argv[1], ' tries ')
        print('Pi = ', str(Pi))
    if float(sys.argv[2])<=1:
        seed=int(sys.argv[3])
        random.seed(seed)
        t=[x for x in range(0,N)]
        s=[x for x in range(0,N)]
        for i in range(0,N):
            t[i]=random.random()
            s[i]=random.vonmisesvariate(0,0)
        recurse(N)
        h=len(f)
        Pi= (2*L*N)/h
        print(str(h), ' hits in ' , sys.argv[1], ' tries ')
        print('Pi = ', str(Pi))