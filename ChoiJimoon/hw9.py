import numpy as np
import matplotlib.pyplot as plt
import random


x=[0, 10, 9, 5, 10, 5, 4, 2, 8, 9]
y=[10, 0, 6, 8, 4, 3, 2, 7, 3, 2]



def dist(x,y):
    z=0
    for i in range(9):
        z+=np.sqrt((x[i+1]-x[i])**2+(y[i+1]-y[i])**2)
    return z

def de(i,j,x,y):
    nx, ny = x[:], y[:]
    nx[i], nx[j] = nx[j], nx[i]
    ny[i], ny[j] = ny[j], ny[i]
    return dist(nx,ny)-dist(x,y)


def swap(x,y,b):
    i=random.randint(0,9)
    j=random.randint(0,9)
    delta=de(i,j,x,y)
    if(delta<0):
        x[i], x[j] = x[j], x[i]
        y[i], y[j] = y[j], y[i]
    else:
        if(random.random()<np.exp(-b*delta)):
            x[i], x[j] = x[j], x[i]
            y[i], y[j] = y[j], y[i]
    return x,y

Tmax=20
tau=1000
for t in range(100000):
    T=Tmax*np.exp(-t/tau)
    b=1/T
    swap(x,y,b)

print(dist(x,y))    
plt.plot(x,y,'o')
plt.plot(x,y)
plt.show()

#거리가  25.54052797037772일떄 최소값이다.