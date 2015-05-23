import math
def findRoot(f,a,b,epsilon):
    while float((b-a)/2)>float(epsilon):
        m=float((a+b)/2)
        if f(a)==0:
            return a
        if f(b)==0: 
            return b
        if f(m)==0:
            return m
        elif f(a)*f(m)<0:
            b=m
        else:
            a=m
    if math.fabs(f(m))<math.fabs(f(a)) and math.fabs(f(m))<math.fabs(f(a)):
        return m
    elif math.fabs(f(a))<math.fabs(f(b)):
        return b
    else:
        return a
def findAllRoots(f,a,b,epsilon):
    l=[]
    while float(b-a)>float(.1):
        if f(a)*f(a+.1)>0:
            a+=0.1
        else:
            l.append(findRoot(f,a,a+0.1,epsilon))
            a+=0.1
    return l