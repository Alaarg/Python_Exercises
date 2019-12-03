# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 09:50:26 2019

@author: Ahmad ALaarg
"""
"""

import sympy as sym
x = sym.symbols('x')
expr = x + 1
print ( expr.subs(x, 2) )


from sympy import * 
x = symbols('x')
init_printing()
expr= Integral(sqrt(1/x),x)
print(expr)

"""
"""
import sympy as sym
x = sym.Symbol('x')
y, i ,n, a, b = sym.symbols('y i n a b')
f = x**2 + 1
print( f.subs(x, 2))
print(  sym.expand( (x + y) ** 3 )   )
"""

from sympy import symbols
from sympy.plotting import plot
x = symbols('x')
plot(x**2, (x, -5, 5))


from sympy.plotting import plot3d
x, y = symbols('x y')
f=x**2*y**2
plot3d(f, (x, -5, 5), (y, -5, 5))


x, y = symbols('x y')
f=cos(x)+sin(y)
plot3d(f, (x, -10, 10), (y, -10, 10))

from sympy import symbols, cos, sin
from sympy.plotting import plot3d_parametric_line
u, v = symbols('u v')
plot3d_parametric_line(cos(u), sin(u), u, (u, -5, 5))


from sympy.plotting import plot3d_parametric_surface
u, v = symbols('u v')
plot3d_parametric_surface(cos(u + v), sin(u -v), u -v, (u, -5, 5), (v, -5, 5))

