import time
import sys

prime= open(str(sys.argv[2]),'w')
N=int(sys.argv[1])
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
print('Found ', str(len(priemen)), ' Prime numbers smaller than ', str(N), ' in ', Time, ' sec.')
print(priemen)
print(N)
prime.write('\n'.join(map(str, priemen)))