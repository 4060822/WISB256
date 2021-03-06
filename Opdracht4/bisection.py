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
    if math.fabs(f(m))<math.fabs(f(a)) and math.fabs(f(m))<math.fabs(f(b)):
        return m
    if math.fabs(f(a))<math.fabs(f(m)):
        return a
    else:
        return b
def findAllRoots(f,a,b,epsilon):
    l=[]
    while float(b-a)>float(.1):
        if f(a)*f(a+.1)>0:
            a+=0.1
        else:
            l.append(findRoot(f,a,a+0.1,epsilon))
            a+=0.1
    return l