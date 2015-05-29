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
        return eval('+'.join(outcome))
        
    def norm(self):
        return math.sqrt(self.inner(self))
    
def GrammSchmidt(V):
    W=[V[0].scalar(1/(V[0].norm()))]
    if len(V)>1:
        for i in range(1,len(V)):
            SUM=V[i]
            for j in range(0,i-1):
                SUM=SUM+W[j].scalar(V[i].inner(W[j])/W[j].norm())
            W.append(SUM.scalar(1/(SUM.norm())))
    return W