
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

#  Trigonometric Function 

#Trigonometric Function ver.trapezoidal solution
def integf(x):
    if x>0 or x==0:
        a=np.arange(0,x,0.01)
        f=0
        for i in a:
            f=f+(np.cos(i+0.01)+np.cos(i))*((0.005))
        return f
    else :
        a=np.arange(x,0,0.01)
        f=0
        for i in a:
            f=f-(np.cos(i+0.01)+np.cos(i))*((0.005))
        return f


def integg(x):
    if x>0 or x==0:
        a=np.arange(0,x,0.01)
        g=0
        for i in a:
            g=g+(np.sin(i+0.01)+np.sin(i))*((0.005))
        return g
    else :
        a=np.arange(x,0,0.01)
        g=0
        for i in a:
            g=g-(np.sin(i+0.01)+np.sin(i))*((0.005))
        return g     

t=np.arange(-7,7,0.01)
b=[]
c=[]
for i in t:
    
    b.append(integf(i))
for i in t:
    
    c.append(integg(i)) 
plt.plot(t,b,color="blue",label="cos funtion's indefinite integral")  
plt.plot(t,c,color="red",label="sin funtion's indefinite integral") 
plt.legend(loc="upper right")
plt.title("Trigonometric Function ver.trapezoidal solution")
plt.show()        
             





# Trigonometric Function ver.scipy.integrate
def f(t):
    return np.sin(t)

def g(t):
    return np.cos(t)

def integf2(x):
    return float(integrate.quad(f,0,x)[0])

def integg2(x):
    return float(integrate.quad(g,0,x)[0])    


a=np.arange(-7,7,0.1)
b=[]
c=[]
for i in a:
    b.append(integf2(i))

for i in a:
    c.append(integg2(i))


plt.plot(a,b,color="red",label="sin funtion's indefinite integral")
plt.plot(a,c,color="blue",label="cos funtion's indefinite integral")
plt.legend(loc="upper right")
plt.title("Trigonometric Function ver.scipy.integrate")
plt.xlabel("x")
plt.show( )