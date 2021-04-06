import matplotlib.pyplot as plt
import numpy as np
from scipy import misc


#(Differentiation) Trigonometric Function

# Trigonometric Function ver.finite difference


a=np.arange(-7,7,0.001)
b=[]
c=[]

def dervif(x):
    return (np.sin(x+0.001)-np.sin(x))/0.001
def dervig(x):
    return (np.cos(x+0.001)-np.cos(x))/0.001    

for i in a:
    b.append(dervif(i))
for i in a:
    c.append(dervig(i))    
plt.plot(a,b,color="blue",label="sin funtion's derivative") 
plt.plot(a,c,color="red",label="cos funtion's derivative")
plt.legend(loc="upper right")
plt.title("Trigonometric Function ver.finite difference")
plt.show()        
    




















#Trigonometric Function ver. scipy.misc.derivative
a=np.arange(-7,7,0.001)
b=[]
for i in a:
    b.append(misc.derivative(np.sin,i,dx=0.001))

c=[]
for i in a:
    c.append(misc.derivative(np.cos,i,dx=0.001))

plt.plot(a,b,color="blue",label="sin funtion's derivative")
plt.plot(a,c,color="red",label="cos funtion's derivative")
plt.legend(loc="upper right")
plt.title("Trigonometric Function ver.scipy.misc.derivative")
plt.xlabel("x")
plt.show()




