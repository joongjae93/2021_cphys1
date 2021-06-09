import numpy as np
import sympy
from sympy import Symbol
from sympy import *

x= sympy.symbols("x")
a= sympy.symbols("a")

print(sympy.integrate(sympy.exp(-a*x**2),(x,-sympy.oo,sympy.oo)))
print(sympy.integrate(x*sympy.exp(-a*x**2),(x,-sympy.oo,sympy.oo)))
print(sympy.integrate(x**2*sympy.exp(-a*x**2),(x,-sympy.oo,sympy.oo)))
print(sympy.integrate(x**4*sympy.exp(-a*x**2),(x,-sympy.oo,sympy.oo)))


t = symbols('t')
x = Function('x') 
print(dsolve(Eq(x(t).diff(t),-a*x(t))))

# 상수 결정 x(-1.5)