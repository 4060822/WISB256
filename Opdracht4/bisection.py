def findRoot(f,a,b,epsilon):
    while float((b-a)/2)>float(epsilon):
        m=float((a+b)/2)
        if f(m)==0:
            return m
        elif f(a)*f(m)<0:
            b=m
        else:
            a=m
    return m