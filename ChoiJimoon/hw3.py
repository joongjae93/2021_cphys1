import numpy as np
import matplotlib.pyplot as plt
import math

#############Leibniz Pi formula###################3

def Leibniz_Pi_formula(n):
    x,y=[],[]
    f=0
    l=[i for i in range(1,n+1) if i % 2 == 1]
    for i in range(0,len(l)):
        if i % 2 ==0:
            f+=1/l[i] 
            y.append(f)
            x.append(l[i])
        elif i % 2 ==1: 
            f+=1/-l[i]
            y.append(f)
            x.append(l[i])
        
    
    plt.plot(x,y,'-b',label='Leibniz formula for pi')
    plt.hlines(math.pi/4,0,100,color='r',label='pi/4')
    plt.legend()
    plt.show()
    



###################logistic_map#######################


def logistic_map(r,f,n):
    k=f
    y=[]
    x=[]
    for i in range(1,n+1):
        f=r*f*(1-f)
        y.append(f)
        x.append(i)  
    plt.plot(x,y,'-b',label='logistic_map r=%s, f=%s' %(r,k))  
    plt.legend()
    plt.show()  

    

######################sinc function#################################


def sinc_taylor(x,n):
    f=0
    for i in range(n+1):
        f=f+((-1)**i)*(x**(2*i))/math.factorial((2*i)+1)
    return f
        
def sinc_function(n):
    x=np.arange(-10,10,0.2)
    y=[]
    for i in x:
        s= math.sin(i)/i
        y.append(s)    
    plt.plot(x,y,'-b',label='sinc_function')
    plt.plot(x,sinc_taylor(x,n),'-g',label='sinc_function_tile n= %d' %n)
    plt.axhline(0,color='r')
    plt.axis([-10,10,-1,1])
    plt.legend()
    plt.show()
    
################실행######################3    


Leibniz_Pi_formula(100)

logistic_map(0.5,0.5,100) 
logistic_map(0.95,0.5,100)
logistic_map(2,0.5,100)
logistic_map(3.2,0.5,100)
logistic_map(3.8,0.5,100)
logistic_map(3.8,0.501,100)
 
sinc_function(1)  
sinc_function(5)
sinc_function(10)
sinc_function(15)

