import numpy as np
import matplotlib.pyplot as plt

# Logistic Map Graph

def logis(r,f_0,n):               
    a=0
    c=f_0
    if n==0:
        return f_0
    else : 
        for i in range(1,n+1):
            a=a+1
            f=r*f_0*(1-f_0)
            f_0=f
        return f
def draw(r,f_0):
    x=np.arange(1,100,1)
    y=[]
    for i in x:
        y.append(logis(r,f_0,i))
    plt.plot(x,y,color="skyblue",label="Logistic Map")
    plt.xlabel("n")
    plt.ylabel("$f_n$")
    plt.legend(loc="upper right")
    plt.title("Logistic Map Graph")
    plt.show()
draw(0.5,0.5)    
draw(0.95,0.5)
draw(2,0.5)
draw(3.2,0.5)
draw(3.8,0.5)
draw(3.8,0.501)