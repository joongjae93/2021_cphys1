import random 
import numpy as np
import matplotlib.pyplot as plt


def ptle(b,n):
    states=np.ones(n)
    for i in range(n*100):
        i=random.randint(0,n-1)
        trynum=random.random()
        if trynum<0.5:
            if states[i]==1:
                pass
            else:
                states[i]=states[i]-1
        else:
            DE=2*states[i]+1
            if random.random()<np.exp(-b*DE):
                states[i]=states[i]+1
            else:
                pass    
    return sum(states**2)



def vavg(n):
    temp=np.arange(1,100,1)
    E=[]
    Ethe=[]
    for t in temp:
        Ethe.append(t/2)
        E.append(ptle(1/t,n)/n)
    
    
    plt.xlabel('temperature')
    plt.ylabel('E')
    plt.plot(temp,E,'o',label="E")
    plt.plot(temp,Ethe,label="Theoretical E")
    plt.legend()
    plt.show()

vavg(1000)

# 입자 박스 (-6)