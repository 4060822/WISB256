import math
class Vector:
    def __init__(self,n=0,elements=0):
        self._n=n
        if type(elements)!= list:
            self._vector=[elements]*n
        else:
            self._vector=elements

    def __str__(self):
        for i in range(0,len(self._vector)):
            self._vector[i]=str(self._vector[i])
        delimiter='\n'
        return delimiter.join(self._vector)

    def __add__(self,other):
        return self.add(other)

    def add(self,other):
        outcome=[0]*len(self._vector)
        for i in range(0,len(self._vector)):
            outcome[i]=self._vector[i]+other._vector[i]
        return Vector(len(outcome),outcome)
        
    def lincomb(self,other,a,b):
        outcome=[0]*len(self._vector)
        for i in range(0,len(self._vector)):
            outcome[i]=a*self._vector[i]+b*other._vector[i]
        return Vector(len(outcome),outcome)
        
    def scalar(self,a):
        return self.lincomb(Vector(len(self._vector)),a,0)
    
    def inner(self,other):
        outcome=[]
        for i in range(0,len(self._vector)):
            outcome.append(str(self._vector[i]*other._vector[i]))
        return float(eval('+'.join(outcome)))
        
    def norm(self):
        return float(math.sqrt(self.inner(self)))
    
    def proj(self,other):
        w=self.inner(other)/(self.inner(self))
        return self.scalar(w)

def GrammSchmidt(V):
    W=[V[0]]
    for i in range(1,len(V)):
        SUM=V[i]
        for j in range(0,i):
            SUM=SUM+(W[j].proj(V[i])).scalar(-1)
        W.append(SUM)
    for i in range(0,len(W)):
        w=1/(W[i].norm())
        W[i]=W[i].scalar(w)
    return W