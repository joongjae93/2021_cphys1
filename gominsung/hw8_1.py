import random
import numpy as np


#Hypersphere
def hyper3d(n):
    count=0
    for i in range(n):
        x,y,z =random.random(),random.random(),random.random()
        if x*x+y*y+z*z<1:
            count+=1
    return  8*count/n 


def hyper4d(n):
    count=0
    for i in range(n):
        x,y,z,t =random.random(),random.random(),random.random(),random.random()
        if x*x+y*y+z*z+t*t<1:
            count+=1
    return  16*count/n  


def hyper5d(n):
    count=0
    for i in range(n):
        x,y,z,t,a =random.random(),random.random(),random.random(),random.random(),random.random()
        if x*x+y*y+z*z+t*t+a*a<1:
            count+=1
    return  32*count/n                 
C3=hyper3d(10000000)
C4=hyper4d(10000000)
C5=hyper5d(10000000)
print(C3)
print(C4)
print(C5)
