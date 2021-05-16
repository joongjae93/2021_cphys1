from scipy.integrate import odeint as ode
import math
import numpy as np
import matplotlib.pyplot as plt


t=np.arange(0,50,0.01)

#1. Pendulum
def f1(state,t):
    x,w=state
    return [w,-1*(np.sin(x))]

def solf1(x0,w0):
    state0=[x0,w0]
    states=ode(f1, state0, t)   
    return states



#2. Pendulum (small oscillations)
def f2(state,t):
    x,w=state
    return [w,-x]
def solf2(x0,w0):
    state0=[x0,w0]
    states=ode(f2, state0, t)   
    return states


#The movement of Pendulum
plt.title("The movement of Pendulum")
plt.plot(t,solf1(0.5,0.5)[:,0],label="Pendulum at w0=0.5,$theta0=0.0.5$")
plt.xlabel("t")
plt.legend(loc="upper right")
plt.show()



#The monvement of Pendulum at Small Amplitude
plt.title("The movement of Pendulum at Small Amplitude")
plt.plot(t,solf2(0.1,1)[:,0],label="Pendulum(small oscillations) at w0=1,$theta0=0.1$")
plt.xlabel("t")
plt.legend(loc="upper right")
plt.show()











# Vibrations about Initial Condition at same Amplitude
plt.subplot(211)
plt.title("Vibrations about Initial Condition at same Amplitude")
plt.plot(t,solf1(0.1,1)[:,0],label="Pendulum at w0=1,$theta0=0.1$",)
plt.plot(t,solf2(0.1,1)[:,0],label="Pendulum(small oscillations) at w0=1,$theta0=0.1$")
plt.legend(loc="upper right",fontsize=7)
plt.xlabel("t")
plt.subplot(212)
plt.plot(t,solf1(1,0.1)[:,0],label="Pendulum at w0=0.1,$theta0=1$",)
plt.plot(t,solf2(1,0.1)[:,0],label="Pendulum(small oscillations) at w0=0.1,$theta0=1$")
plt.legend(loc="upper right",fontsize=7)
plt.xlabel("t")
plt.subplots_adjust(hspace=0.3)
plt.show()


#Vibrations about Initial Angular Velocity at same Initial Phase with Small Amplitude
plt.subplot(211)
plt.title("Vibrations about Initial Angular Velocity at same Initial Phase with Small Amplitude",fontsize="8")
plt.plot(t,solf1(0.1,0.1)[:,0],label="Pendulum at w0=0.1$theta0=0.1$",)
plt.plot(t,solf2(0.1,0.1)[:,0],label="Pendulum(small oscillations) at w0=0.1,$theta0=0.1$")
plt.legend(loc="upper right",fontsize=7)
plt.xlabel("t")
plt.subplot(212)
plt.plot(t,solf1(0.1,0.2)[:,0],label="Pendulum at w0=0.2,$theta0=0.1$",)
plt.plot(t,solf2(0.1,0.2)[:,0],label="Pendulum(small oscillations) at w0=0.2,$theta0=0.1$")
plt.legend(loc="upper right",fontsize=7)
plt.xlabel("t")
plt.subplots_adjust(hspace=0.3)
plt.show()

#Vibrations about Initial Phase at same Initial Angular Velocity with Large Amplitude
plt.subplot(211)
plt.title("Vibrations about Initial Phase at same Initial Angular Velocity with Large Amplitude",fontsize="8")
plt.plot(t,solf1(0.5,1)[:,0],label="Pendulum at w0=1,$theta0=0.5$",)
plt.plot(t,solf2(0.5,1)[:,0],label="Pendulum(small oscillations) at w0=1,$theta0=0.5$")
plt.legend(loc="upper right",fontsize=7)
plt.xlabel("t")
plt.subplot(212)
plt.plot(t,solf1(0.5,1.5)[:,0],label="Pendulum at w0=1.5,$theta0=0.5$",)
plt.plot(t,solf2(0.5,1.5)[:,0],label="Pendulum(small oscillations) at w0=1.5,$theta0=0.5$")
plt.legend(loc="upper right",fontsize=7)
plt.xlabel("t")
plt.subplots_adjust(hspace=0.3)
plt.show()

#Vibrations about Initial Phase  at same Angular Velocity with Small Amplitude
plt.subplot(211)
plt.title("Vibrations about Initial Phase  at same Angular Velocity with large Amplitude",fontsize="8")
plt.plot(t,solf1(0.1,0.1)[:,0],label="Pendulum at w0=0.1,$theta0=0.1$",)
plt.plot(t,solf2(0.1,0.1)[:,0],label="Pendulum(small oscillations) at w0=0.1,$theta0=0.1$")
plt.legend(loc="upper right",fontsize=7)
plt.xlabel("t")
plt.subplot(212)
plt.plot(t,solf1(0.5,0.1)[:,0],label="Pendulum at w0=0.1,$theta0=0.5$",)
plt.plot(t,solf2(0.5,0.1)[:,0],label="Pendulum(small oscillations) at w0=0.1,$theta0=0.5$")
plt.legend(loc="upper right",fontsize=7)
plt.xlabel("t")
plt.subplots_adjust(hspace=0.3)
plt.show()


#Vibrations about Initial Angular Velocity at same Initial Phase with Large Amplitude
plt.subplot(211)
plt.title("Vibrations about Initial Angular Velocity at same Initial Phase with Large Amplitude",fontsize="8")
plt.plot(t,solf1(0.5,1)[:,0],label="Pendulum at w0=1,$theta0=0.5$",)
plt.plot(t,solf2(0.5,1)[:,0],label="Pendulum(small oscillations) at w0=1,$theta0=0.5$")
plt.legend(loc="upper right",fontsize=7)
plt.xlabel("t")
plt.subplot(212)
plt.plot(t,solf1(1,1)[:,0],label="Pendulum at w0=1,$theta0=1$",)
plt.plot(t,solf2(1,1)[:,0],label="Pendulum(small oscillations) at w0=1,$theta0=1$")
plt.legend(loc="upper right",fontsize=7)
plt.xlabel("t")
plt.subplots_adjust(hspace=0.3)
plt.show()


