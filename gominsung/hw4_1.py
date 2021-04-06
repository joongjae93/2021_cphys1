import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
import math as m

#Error Function
def exp1(t):
    a=-1*(t**2)
    b=np.exp(a)
    return b

def errf(x):
    a=integrate.quad(exp1,0,x)[0]
    return (2*a)/((np.pi)**0.5)    

def taylor(n,x):
    a=np.arange(0,n+1,1)
    f=0
    for i in a:
        an=(((-1)**i)*x**(2*i+1))/((2*i+1)*m.factorial(i))
        f=f+an
    return (2/np.pi**(1/2))*f    

x=np.arange(-2.5,2.5,0.01)
b=[]
c1=[]
c2=[]
c3=[]

for i in x:
    b.append(errf(i))

for i in x:
    c1.append(taylor(1,i))

for i in x:
    c2.append(taylor(5,i))

for i in x:
    c3.append(taylor(10,i))






plt.title("Taylor approximation of Error Function")
plt.plot(x,b,color="black",label="Error Function")
plt.plot(x,c1,color="red",label="Taylor approximation of Error Function at n=1")
plt.legend(loc="upper left",fontsize=7)



plt.plot(x,c2,color="blue",label="Taylor approximation of Error Function at n=5")
plt.legend(loc="upper left",fontsize=7)




plt.plot(x,c3,color="green",label="Taylor approximation of Error Function at n=10")
plt.legend(loc="upper left",fontsize=7)
plt.ylim(-1.5,1.5)
plt.xlabel("x")
plt.show()