import random
import matplotlib.pyplot as plt
import numpy as np
from sympy import *

# 1. Random Walks

def Rwalks(t):
    x=0
    t0=0
    while t0 < t:
        if random.random()<1/2:
            x=x+1
        else:
            x=x-1
        t0=t0+1
        if t0==t:
            return x

data=[]
for i in range(100000):
    data.append(Rwalks(100))
plt.hist(data, bins=100,density = True, alpha=0.4, histtype='stepfilled',color = 'red')
plt.hist(data, bins=100,density = True, alpha=1, histtype='step',color="black")
plt.show()    

# 2. Bifurcation

def sol(r,x0):
    t=symbols('t')
    x=Function('x')
    a=dsolve(Eq(x(t).diff(t),(r*x(t))-(x(t)**2)), ics={x(0): x0})
    plot( a.rhs, (t,0,10))  
    print("r=%s x0=%s 일 때 미분방정식의 해 x(t)는 %s 이다." %(r, x0, a.rhs))


sol(-1,2)
sol(-1,-2)
sol(1,2)
sol(1,-2)


def solution(r):
    x=symbols('x')
    a=solve(r*x-x**2)
    print("r=%s일 때 정상상태의 해 x(t)는 %s 이다." %(r,a))

solution(1)
solution(-1)
