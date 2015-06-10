from numpy import *
from scipy.integrate import odeint
def func(I,t,S,R,B):
    xt=I[0]
    yt=I[1]
    zt=I[2]
    xdot=S*(yt-xt)
    ydot=xt*(R-zt)-yt
    zdot=xt*yt-B*zt
    return [xdot,ydot,zdot]
class Lorenz:
    def __init__(self,I,sigma=10,rho=28,beta=8/3):
        self._I=I
        self._S=sigma
        self._R=rho
        self._B=beta
        
    def solve(self,T,dt):
        t=arange(0,T+dt,dt)
        return odeint(func,self._I,t,(self._S,self._R,self._B))
        
