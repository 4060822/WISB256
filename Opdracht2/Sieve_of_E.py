import time
import sys
print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

prime= open('prime.dat','w')
N=int(input('N='))
t=[x for x in range(2,N)]
priemen=[]
def P(a):
    for y in t:
        if y!=0:
            veelv=range(y,N,y)
            for f in veelv[1:N]:
                if t[f-2]!=0:
                    t[f-2]=0
    for z in t:
        if z!=0:
            priemen.append(z)
T1=time.perf_counter()
P(N)
T2=time.perf_counter()
Time=str(T2-T1)
print(str(len(priemen)), ' Prime numbers smaller than ', str(N), ' in ', Time, ' sec.')
prime.write('\n'.join(map(str, priemen)))