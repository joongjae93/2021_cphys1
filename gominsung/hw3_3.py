import numpy as np
import matplotlib.pyplot as plt
import math as m

# sinc funtion graph
def sincan(x,n):

    a_n1=((-1)**n)*(x**(2*n))   #분자
    a_n2= m.factorial((2*n)+1)  
    a_n=a_n1/a_n2
    return a_n
def sincsum(x,n):
    f_0=0
    b=np.arange(0,n+1,1)
    for i in b:
        f_0=f_0+sincan(x,i)
    return f_0   

def draw(n):
    x=np.arange(-20,20,0.2)
    y1=[]
    plt.subplot(411)
    plt.title("Taylor approximation of sinc function")
    for i in x:
        y1.append(sincsum(i,n))
    plt.plot(x,y1,color="skyblue",label="Talor expension n=%i" %n)
    plt.xlabel("x")
    plt.legend(loc="upper right",fontsize=8)
    z1=[]
    for i in x:
        a=(m.sin(i))/i
        z1.append(a)
    plt.plot(x,z1,color="red",label="Sinc funtion")  
    plt.legend(loc="upper right",fontsize=8)
    plt.ylim(-0.25,1)

    y2=[]
    plt.subplot(412)
    for i in x:
        y2.append(sincsum(i,n+5))
    plt.plot(x,y2,color="skyblue",label="Talor expension n=%i" %(n+5))
    plt.xlabel("x")
    plt.legend(loc="upper right",fontsize=8)
    z2=[]
    for i in x:
        a=(m.sin(i))/i
        z2.append(a)
    plt.plot(x,z2,color="red",label="Sinc funtion")  
    plt.legend(loc="upper right",fontsize=8)
    plt.ylim(-0.25,1)


    y3=[]
    plt.subplot(413)
    for i in x:
        y3.append(sincsum(i,n+10))
    plt.plot(x,y3,color="skyblue",label="Talor expension n=%i" %(n+10))
    plt.xlabel("x")
    plt.legend(loc="upper right",fontsize=8)
    z3=[]
    for i in x:
        a=(m.sin(i))/i
        z3.append(a)
    plt.plot(x,z3,color="red",label="Sinc funtion")  
    plt.legend(loc="upper right",fontsize=8)
    plt.ylim(-0.25,1)
    
    y4=[]
    plt.subplot(414)
    for i in x:
        y4.append(sincsum(i,n+15))
    plt.plot(x,y4,color="skyblue",label="Talor expension n=%i" %(n+15))
    plt.xlabel("x")
    plt.legend(loc="upper right",fontsize=8)
    z4=[]
    for i in x:
        a=(m.sin(i))/i
        z4.append(a)
    plt.plot(x,z4,color="red",label="Sinc funtion")  
    plt.legend(loc="upper right",fontsize=8)
    plt.ylim(-0.25,1)
    plt.subplots_adjust(hspace=0.3)
    plt.show()
       

draw(1)