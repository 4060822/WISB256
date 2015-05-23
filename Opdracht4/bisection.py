import math
def findRoot(f,a,b,epsilon):
    while float((b-a)/2)>float(epsilon):
        m=float((a+b)/2)
        if f(m)==0:
            return m
        elif f(a)*f(m)<=0:
            b=m
        else:
            a=m
    return m
def findAllRoots(f,a,b,epsilon):
    l=[]
    while float(b-a)>float(.1):
        if f(a)*f(a+.1)>0:
            a+=0.1
        else:
            l.append(findRoot(f,a,a+0.1,epsilon))
            a+=0.1
    return l