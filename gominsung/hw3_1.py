#Leibniz Pi formula
import numpy as np  
import matplotlib.pyplot as plt

def leibn(n):
   b_1=1
   x=1
   f_n=1
   while True:
        x= x+1
        if n==1:
            return 1
        if x%2==0:
            b_n=b_1+2
            a_n=1/b_n
            f_n=f_n-a_n
            b_1=b_n
        
            
        elif x%2==1:
            b_n=b_1+2
            a_n=1/b_n
            f_n=f_n+a_n
            b_1=b_n
        
        if x==n:
            return f_n
            break            

x=np.arange(1,100,1)
y=[]
z=[]
for i in x:
    y.append(leibn(i))

for i in x:
    z.append(np.pi/4)
plt.title("Leibniz Pi formula")    
plt.plot(x,y,color='skyblue',label="Leibniz Pi formula for π")
plt.plot(x,z,color="orange",label="π/4")
plt.xlabel("n")
plt.ylabel("$f_n$")
plt.legend()
plt.show()
