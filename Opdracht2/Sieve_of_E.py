import time
import sys

N=int(input('N='))
t=[x for x in range(3,N,2)]
priemen=[2]
if N>=7907:
    v=[x for x in range(7907,N,2)]
elif N<7907:
    v=[]
prime=open('prime.dat', 'w')
def Priem1(a):
    for y in t:
        if y%a==0:
            t.remove(y)
        if y==a:
            priemen.append(y)
    for y in v:
        if y%a==0:
            v.remove(y)
    if len(priemen)<999 and len(t)>0:
        Priem1(t[0])
def Priem2(a):
    for y in v:
        if y%a==0:
            v.remove(y)
        if y==a:
            priemen.append(y)
    if len(v)>0:
        Priem2(v[0])
T1 = time.perf_counter()
Priem1(3)
if v!=[]:
    Priem2(v[0])
T2 = time.perf_counter()
Time ='Time required '+ str(T2-T1)+ ' sec.'
print('$ python3 Sieve_of_E.py ', str(int(N)), ' prime.dat Found ', str(len(priemen)), ' Prime numbers smaller than ', str(int(N)), ' in '+ str(Time)+ ' sec.') 
prime.write('\n'.join(map(str, priemen)))
prime.close()