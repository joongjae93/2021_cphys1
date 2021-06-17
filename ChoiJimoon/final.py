import random
import matplotlib.pyplot as plt
import numpy as np
from sympy import *
import sympy



# Random_Walk(100)
def RW(t):  
    z=0
    m,x=[0],[0]
    
    
    for i in range(1,t+1):
        
        x.append(i)
        if random.random() <1/2:
            z+=1
            m.append(z)
        else:
            z-=1
            m.append(z)
    return m , x , m[-1]
    

#4개의 Random Walk 위치 그래프
def Random_Walk(t):
    plt.plot(RW(100)[1],RW(100)[0],'r')
    plt.plot(RW(100)[1],RW(100)[0],'g')
    plt.plot(RW(100)[1],RW(100)[0],'b')
    plt.plot(RW(100)[1],RW(100)[0],'y')
    plt.title('4n Random Walk')
    plt.xlabel('time')
    plt.ylabel('step')
    plt.show()



#n개의 Random Walk 확률분포
def RW_hist(n,t):
    z=[]
    for i in range(n):
        z.append(RW(t)[2])
    plt.title('Probability distribution')
    plt.ylabel('Probability')
    plt.xlabel('step')    
    plt.hist(z,density=True,bins =100)
    plt.show()




Random_Walk(100)
RW_hist(10000,100)


## 2 Bifurcation  #######

#a) 이 방정식을 다음의 조건에서 풀고 궤적을 그려라. (미분방정식)

t,X = symbols('t,X')
x = Function('x')



def Bifurcation(f,q,s):
    
    F=dsolve(f,ics={x(0):q}).rhs
    print(s,'초기조건x(0)=',q, '일떄의 미분방정식을 풀면', F)
    plot(F,(t,0,10),title='%s'%(F))
    


Bifurcation(Eq(x(t).diff(t),-x(t)-(x(t)**2)),2,'-x(t)-(x(t)**2')
Bifurcation(Eq(x(t).diff(t),-x(t)-(x(t)**2)),-2,'-x(t)-(x(t)**2')
Bifurcation(Eq(x(t).diff(t),x(t)-(x(t)**2)),2,'x(t)-(x(t)**2')
Bifurcation(Eq(x(t).diff(t),x(t)-(x(t)**2)),-2,'x(t)-(x(t)**2')




#b)정상상태(dx/dt=0)에서 가능한 해를 구하여라. (방정식)

print('x(r-x)')
print('r=-1일떄',solve(-X-(X**2)))
print('r=1일떄',solve(X-(X**2)))


