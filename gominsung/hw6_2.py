from scipy.integrate import odeint as ode
import math
import numpy as np
import matplotlib.pyplot as plt


t=np.arange(0,50,0.01)


def f3(state,t):
    x,w=state
    return w,-1*0.1*w-math.sin(x)

def solf3(x0,w0):
    state0=[x0,w0]
    states=ode(f3, state0, t)   
    return states    

def f40(state,t):
    x,w=state
    return w,-1*1*w-math.sin(x)+math.cos(0.1*t)

def f41(state,t):
    x,w=state
    return w,-1*1*w-math.sin(x)+math.cos(0.5*t)    

def f42(state,t):
    x,w=state
    return w,-1*1*w-math.sin(x)+math.cos(2*t)    

def f43(state,t):
    x,w=state
    return w,-1*1*w-math.sin(x)+math.cos(3*t)

def solf40(x0,w0):
    state0=[x0,w0]
    states=ode(f40, state0, t)   
    return states

def solf41(x0,w0):
    state0=[x0,w0]
    states=ode(f41, state0, t)   
    return states

def solf42(x0,w0):
    state0=[x0,w0]
    states=ode(f42, state0, t)   
    return states

def solf43(x0,w0):
    state0=[x0,w0]
    states=ode(f43, state0, t)   
    return states    

# Damped Pendulum
plt.title("The movement of Damped Pendulum")
plt.plot(t,solf3(1,0)[:,0],label="The movement of Damped Pendulum at w0=0,$theta0=1$")
plt.xlabel("t")
plt.legend()
plt.show()

#Forced Pendulum
plt.subplot(411)
plt.title("The movement of Forced Pendulum at A=1,B=1,G=L,w0=0.1,$theta0=0.1$",fontsize="10")
plt.plot(t,solf40(0.1,0.1)[:,0],label="The movement of Forced Pendulumat V=0.1")
plt.xlabel("t")
plt.legend(loc="upper right",fontsize=7)

plt.subplot(412)
plt.plot(t,solf41(0.1,0.1)[:,0],label="The movement of Forced Pendulumat V=0.5")
plt.xlabel("t")
plt.legend(loc="upper right",fontsize=7)

plt.subplot(413)
plt.plot(t,solf42(0.1,0.1)[:,0],label="The movement of Forced Pendulumat V=2")
plt.xlabel("t")
plt.legend(loc="upper right",fontsize=7)

plt.subplot(414)
plt.plot(t,solf43(0.1,0.1)[:,0],label="The movement of Forced Pendulumat V=3")
plt.xlabel("t")
plt.legend(loc="upper right",fontsize=7)
plt.subplots_adjust(hspace=0.7)
plt.show()

# 외부에서 주어지는 힘의 진동수가 커지면 커질수록 진자는 감쇠진동의 추세가 사라지고 외부진동에 따른 운동을 하게 된다.

# -1  -  설명 틀림