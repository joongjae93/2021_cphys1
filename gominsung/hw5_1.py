import numpy as np
import matplotlib.pyplot as plt
import math

#  Vibration in a one-dimensional system

k=1
m=1
c=1
b1=np.zeros((40,1))
b1[0][0]=c
b2=np.zeros((40,1))
b2[0][0]=c
b2[39][0]=c

def f(w):
    d=2*k-m*(w**2)
    a=np.zeros([40,40])
    b=range(40)
    for i in b:
        if i==0:
            a[i][i]=d-k
            a[i][i+1]=-k
        elif i==39:
            a[39][38]=-k
            a[39][39]=d-k
        else :
            a[i][i-1]=-k
            a[i][i]=d
            a[i][i+1]=-k
    return a
def homework1():
        y1=np.linalg.solve(f(1),b1)
        y2=np.linalg.solve(f(2),b1)
        y3=np.linalg.solve(f(3),b1)

        y11=[]
        y12=[]
        y13=[]
        for i in range(40):
            y11.append(y1[i][0])
            y12.append(y2[i][0])
            y13.append(y3[i][0])
        x=np.arange(0,40)
        plt.plot(x,y11,label="w=1")
        plt.plot(x,y12,label="w=2")
        plt.plot(x,y13,label="w=3")    
        plt.legend(loc="upper right")
        plt.xlabel("i")
        plt.ylabel("a_i")
        plt.title("Vibration of a one-dimensional system with force applied to one end")
        plt.xlim(0,40)
        plt.show()
    
def homework2():
        y1=np.linalg.solve(f(1),b2)
        y2=np.linalg.solve(f(2),b2)
        y3=np.linalg.solve(f(3),b2)

        y11=[]
        y12=[]
        y13=[]
        for i in range(40):
            y11.append(y1[i][0])
            y12.append(y2[i][0])
            y13.append(y3[i][0])
        x=np.arange(0,40)
        plt.plot(x,y11,label="w=1")
        plt.plot(x,y12,label="w=2")
        plt.plot(x,y13,label="w=3")    
        plt.legend(loc="upper right")
        plt.xlabel("i")
        plt.ylabel("a_i")
        plt.title("Vibration of a one-dimensional system with force applied to both ends")
        plt.xlim(0,40)
        plt.show()        
homework1()
homework2()

# w=1 일경우
# 한쪽 끝에서만 힘을 가할 경우 (3n+2) 번쨰 물체들은 진동하지 않고 (0,1),(6,7),(12,13),....번째 물체들과 
# (3,4),(9,10),(15,16),...번째 물체들은 진폭은 서로 같으나 방향이 서로 다른 진동을 한다.
# 양쪽 끝에서만 힘을 가할경우 3n번 째 물체들은 진동하지 않고 1,2,7,8,13,14,..번 째 물체들과 
#4,5,10,11,16,17,....번 째 물체들은 진폭은 서로 같으나 방향이 서로 다른 진동을 한다.
# w= 2일경우
# 한쪽 끝에서만 힘을 가할경우 힘을 가하는 원천에서 멀어지면 멀어질수록 진폭이 감소한다.
# 양 끝에서 힘을 가할경우 중앙에서 진동이 상쇄되어 중앙의 진폭은 0이고 중앙에서 멀어질수록 상쇄되는 양이 줄어들어 진폭이 커진다.

#=3일경우
# 한 쪽 끝에서만 힘을 가할경우 n=0과 n=1번째 물체만 진동하고 나머지 물체는 진동하지 않는다.
# 양 쪽 끝에서 힘을 가할경우 n=0 n=1 n=38 n=39 번째 물체만 진동하고 나머지 물체는 진동하지 않는다.

# 상쇄되지 않는 경우는 어떻게 설명할 수 있나요?(-1.5)