import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import integrate
from scipy.misc import derivative


############Error_Function####################
def erf1(t) :
    return np.exp(-t**2)

def erf_taylor(x,n):
    f=0
    for i in range(n+1):
        f=f+(2/np.pi**(0.5))*(((-1)**i)*(x**(2*i+1)))/((2*i+1)*math.factorial(i))
    return f

def erf():
    x = np.arange(-4,4,0.01)
    z = []
    for i in x :
        F,err = integrate.quad(erf1,0,i)
        k = (2/np.pi**(1/2))*F
        z.append(k)
    plt.title("Error_Function")
    plt.plot(x,z,label='erf')
    plt.plot(x,erf_taylor(x,5),label='erf_taylor n=5')
    plt.plot(x,erf_taylor(x,10),label='erf_taylor n=10')
    plt.plot(x,erf_taylor(x,15),label='erf_taylor n=15')
    plt.grid()
    plt.legend()
    plt.axis([-4,4,-1.5,1.5])
    plt.show()
    
###############Trigonometric Function######################333

def sin(t):
    return np.sin(t)

def cos(t):
    return np.cos(t)
    

def sincos():
    x = np.arange(0,6,0.01)
    z,j = [],[]
    
    for i in x :
        F,err = integrate.quad(sin,0,i)
        r,t = integrate.quad(cos,0,i)
        z.append(F)
        j.append(r)
    plt.title("Integration")
    plt.plot(x,z,label='sin_Integration')
    plt.plot(x,j,label='cos_Integration')
   
    plt.grid()
    plt.legend()
   
    plt.show()

def qwe(f,x,dx):
    return (f(x+dx)+f(x))/2
    
def trapezoidal(dx):
    x = np.arange(0,6,dx)
    z,j = [],[]
    s,d=0,0
    for i in x:
        
        s += dx*qwe(sin,i,dx)
        d += dx*qwe(cos,i,dx)
        z.append(s)
        j.append(d)
       
        
    plt.plot(x,z,label='sin_trapezoidal')
    plt.plot(x,j,label='cos_trapezoidal')
    plt.legend()
    
    plt.grid()
    plt.show()
    


#############################Differentiation##############################

def sincos2():
    x = np.arange(-4,4,0.01)
    z,j = [],[]
    
    for i in x :
        F = derivative(sin,i,dx=0.01)
        r = derivative(cos,i,dx=0.01)
        z.append(F)
        j.append(r)
    plt.title("Differentiation")
    plt.plot(x,z,label='sin_Differentiation')
    plt.plot(x,j,label='cos_Differentiation')
   
    plt.grid()
    plt.legend()
    plt.axis([-4,4,-1.5,1.5])
    plt.show()

def for_difference(f,x,dx):
    return (f(x+dx)-f(x))/dx

def finite_difference():
    x = np.arange(-4,4,0.01)
    z,j = [],[]
    for i in x:
        z.append(for_difference(sin,i,0.01))
        j.append(for_difference(cos,i,0.01))
        
    plt.plot(x,z,label='sin_finite_difference')
    plt.plot(x,j,label='cos_finite_difference')
    plt.legend()
    plt.grid()
    plt.axis([-4,4,-1.5,1.5])
    plt.show()
    
    
    
##############실행###################

erf()


trapezoidal(0.01)
sincos()  


finite_difference()
sincos2()
