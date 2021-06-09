import numpy as np
import sympy
from sympy import Symbol
from sympy import *


########################33
x,y,z,a = symbols("x,y,z,a")



print(sympy.integrate(sympy.exp(-a*(x**2)),(x,-oo,oo)))
print(sympy.integrate(x*sympy.exp(-a*(x**2)),(x,-oo,oo)))
print(sympy.integrate((x**2)*sympy.exp(-a*(x**2)),(x,-oo,oo)))
print(sympy.integrate((x**3)*sympy.exp(-a*(x**2)),(x,-oo,oo)))
print(sympy.integrate((x**4)*sympy.exp(-a*(x**2)),(x,-oo,oo)))


##############################
t = symbols('t')
x = Function('x') 
print(dsolve(Eq(x(t).diff(t),-a*x(t)),ics={x(0):1}))