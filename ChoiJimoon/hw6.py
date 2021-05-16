import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import odeint

#######################################33
def f(state, t):
    x, w = state 
    return w, -1*(np.sin(x))

def f1(state, t):
    x, w = state 
    return w, -1*x

def f2(state, t):
    b=0.1
    x, w = state 
    return w, -b*w-np.sin(x)

def f3(state, t):
    A,b,v=1,0.1,0.5
    x, w = state 
    return w, A*np.cos(v*t)-b*w-np.sin(np.radians(x))

def f4(state, t):
    A,b,v=1,0.1,0.7
    x, w = state 
    return w, A*np.cos(v*t)-b*w-np.sin(np.radians(x))

def f5(state, t):
    A,b,v=1,0.1,1
    x, w = state 
    return w, A*np.cos(v*t)-b*w-np.sin(np.radians(x))
    


def draw(f,x0,w0,dt,l):
    state0=[x0,w0]
    t= np.arange(0,50,dt)
    states =odeint(f,state0,t)
    plt.plot(t,states[:,0],label=l)
    plt.legend()
    
    
def draw_Pendulum():
    draw(f,1,0,0.01,'Pendulum θ=1 w=0')
    draw(f1,1,0.1,0.01,'Pendulum_small oscillations θ=1 w=0.1')
    draw(f1,0.1,1,0.01,'Pendulum_small oscillations θ=0.1 w=1')
    draw(f1,0.1,0.1,0.01,'Pendulum_small oscillations θ=0.1 w=0.1')
    plt.xlabel('T')
    plt.ylabel('A')
    plt.title('Pendulum')
    plt.grid()
    plt.show()


def draw_Damped_Pendulum():
    draw(f2,1,0,0.01,'Damped Pendulum θ=1 w=0')
    plt.axhline(0, 0,1, color='red', linestyle='--', linewidth='2')
    plt.xlabel('T')
    plt.ylabel('A')
    plt.title('Damped_Pendulum')
    plt.grid()
    plt.show()

def draw_Forced_Pendulum():
    plt.figure(figsize=(15,4))
    plt.subplot(1,3,1)
    draw(f3,1,0,0.01,'Forced Pendulum θ=rad(1) w=0')
    plt.xlabel('T')
    plt.ylabel('A')
    plt.title('Forced Pendulum v=0.5')
    plt.grid()
  
    plt.subplot(1,3,2)
    draw(f4,1,0,0.01,'Forced Pendulum θ=rad(1) w=0')
    plt.xlabel('T')
    plt.ylabel('A')
    plt.title('Forced Pendulum v=0.7')
    plt.grid()
   
    plt.subplot(1,3,3)
    draw(f5,1,0,0.01,'Forced Pendulum θ=rad(1) w=0')
    plt.xlabel('T')
    plt.ylabel('A')
    plt.title('Forced Pendulum v=1')
    plt.grid()
    plt.show()
    
###########실행###############3

draw_Pendulum()
draw_Damped_Pendulum()
draw_Forced_Pendulum()

# 
-2

2번 문항에서 근사한 경우와 그렇지 않은 경우를 비교 시 조건을 같게 주어야 비교가 의미가 있을 것이고

4번 문항에서는 무엇을 말하고자 하는 건지 알기 어려움

그리고 1번 문항.. 감점 요소는 아니나 채점자가 알아보기 어려우면 이로 인해 불이익이 생길 수 있음