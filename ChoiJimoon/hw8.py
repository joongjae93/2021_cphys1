import random
import numpy as np
import matplotlib.pyplot as plt



#################3#Hypersphere#######################3
def circle_3d(n):
    count=0
    for i in range(n):
        x,y,z=random.random(), random.random(), random.random()
        if x*x+y*y+z*z<1:
            count+=1
    return 8*count/n

def circle_4d(n):
    count=0
    for i in range(n):
        x,y,z,a=random.random(), random.random(), random.random(), random.random()
        if x*x+y*y+z*z+a*a<1:
            count+=1
    return 16*count/n

def circle_5d(n):
    count=0
    for i in range(n):
        x,y,z,a,b=random.random(), random.random(), random.random(),random.random(),random.random()
        if x*x+y*y+z*z+a*a+b*b<1:
            count+=1
    return 32*count/n

#########################################
print(circle_3d(1000))
print(circle_4d(1000))
print(circle_5d(1000))



###############################

def aveE(b,n):
    states = np.ones(n)
    for t in range(n*100):
        i=random.randint(0,n-1)
        
        if random.random() <1/2:
            if states[i]==1:
                pass
            else:
                states[i]=(((states[i]**(1/2))-1)**2)
              
        else:            
            DE=2*(states[i]**1/2)+1
            if random.random() < np.exp(-b*DE):
                states[i]=(((states[i]**(1/2))+1)**2)
    return sum(states)
            
                    
                
                
              

        



def draw(n):
    temp=np.arange(1,20,1)
    y=[aveE(1/x,n) for x in temp ]
   
    plt.title('E=1/2*nkT')
    plt.xlabel('<T>')
    plt.ylabel('<E>')
    plt.plot(temp,y,'.')
    plt.plot(temp,0.5*n*temp)
    

    plt.show()

draw(1000)

    
# 입자박스(-6)


