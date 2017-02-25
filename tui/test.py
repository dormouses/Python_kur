

#from sympy import Symbol, solve, lambdify
#x = Symbol("x", positive=True)
#z = Symbol("z")
#eq = x**2 - z**2*x
#res = solve(eq, x)
#
#f = lambdify( z, res[0])
#
#print(f(2))
#
#from sympy import solve_poly_system
#from sympy.abc import x, y
#eq1 = x*y - 2*y
#eq2 = 2*y**2 - x**2
#print(solve_poly_system([eq1, eq2], x, y))

#from sympy import Symbol, solve, lambdify, Matrix
#k1 = Symbol("k1")
#k2 = Symbol("k2")
#k3 = Symbol("k3")
#km1 = Symbol("km1")
#km2 = Symbol("km2")
#x = Symbol("x")
#y = Symbol("y")
#eq1 = k1*(1 - x - y) - km1*x - k3*x*y
#eq2 = k2*(1 - x - y)**2 - km2*y**2 - k3*x*y
#
#res = solve([eq1, eq2], x, k2)
#
#A = Matrix([eq1, eq2])
#var_vector = Matrix([x, y])
#jacA = A.jacobian(var_vector)
#
##print(jacA)
#
#det_jacA = jacA.det()
#
##print(det_jacA)
#
#trace_jacA = jacA.trace()
#
##print(trace_jacA)
#
#trace_func = lambdify( (x, y, k1, k2, k3, km1, km2) , trace_jacA)
#
#print(k1.subs(k1, 0))

#from sympy import symbols, cos
#x, y, z = symbols("x y z")
#expr1 = cos(x) + 1
#expr2 = expr1.subs(x, y*z)
#
#expr3 = x**y
#expr3 = expr3.subs(y, x**y)
#print(expr3)
#expr3 = expr3.subs(y, x**x)
#print(expr3)

#from sympy import symbols, cos, sin, expand_trig
#x, y, z = symbols("x y z")
#expr = sin(2*x) + cos(2*y)
#expr2 = expand_trig(expr)
#print(expr2)
#expr3 = expr.subs(sin(2*x), 2*sin(x)*cos(x))
#print(expr3)
#expr2 = x**2 + y**2 - z**2
#print(expr2.subs([(x, 1), (y, 3), (z, 2)]))
#
#expr3 = x**4 - 4*x**3 + 4*x**2 - 2*x + 3
#replacements = [(x**i, y**i) for i in range(5) if i % 2 == 0]
#print(expr3.subs(replacements))

#from sympy import *
#str_expr = "x**2 + 3*x - 1/2"
#expr = sympify(str_expr)
#print(expr)
#print(expr.subs(x, 2))
#print(expr.evalf(subs={x: 2}))
#
#from sympy import *
#expr1 = sqrt(8)
#print(expr1.evalf())
#print(expr1.evalf(3))
#expr2 = cos(1)**2 + sin(1)**2
#expr3 = (expr2 - 1).evalf()
#print(expr3)
#expr3 = (expr2 - 1).evalf(chop=True)
#print(expr3)

#from sympy import lambdify, Symbol
#import numpy as np
#x = Symbol("x")
#a = np.linspace(0, np.pi, 3)
#expr = sin(x)
#f = lambdify(x, expr, "numpy")
#print(f(a))
#
#def new_sin(x):
#    return x
#f = lambdify(x, expr, {"sin":new_sin})
#print(f(a))
#print(f(0.1))

#import math
#a = math.sqrt(9)
#print(a)
#b = math.sqrt(8)
#print(b)
#c = math.sqrt(2)
#print(c)
#d = b*c
#print(d)
#
#import sympy
#a = sympy.sqrt(9)
#print(a)
#b = sympy.sqrt(8)
#print(b)
#c = sympy.sqrt(2)
#print(c)
#d = b*c
#print(d)

#from sympy import symbols, expand, factor
#x, y = symbols("x y")
#expr = x + 2*y
#print(expr)
#expr2 = expr - x
#print(expr2)
#expr3 = x*expr
#print(expr3)
#expr4 = expand(expr3)
#print(expr4)
#expr5 = factor(expr4)
#print(expr5)

#from sympy import *
#x, y, z = symbols("x y z")
#expr = x*cos(x)
#d_expr = diff(expr, x)
#print(d_expr)
#
#expr2 = x**4
#d3_expr2 = diff(expr2, x, x, x)
#print(d3_expr2)
#d3_expr2 = diff(expr2, x, 3)
#print(d3_expr2)

#from sympy import *
#x = symbols("x")
#expr = -x*sin(x) + cos(x)
#i_expr = integrate(expr, x)
#print(i_expr)
#
#expr2 = integrate(exp(-x), (x, 0, oo))
#print(expr2)
#
#expr3 = limit(sin(x)/x, x, 0)
#print(expr3)

#from sympy import *
#y = symbols("y", cls=Function)
#print(f(x)) # f(x) - unknown fuction
#ode = Eq(y(x).diff(x, 2) - 2*y(x).diff(x) + y(x)- sin(x), y(x))
#print(ode)
#res = dsolve(ode, y(x))
#print(res)


import numpy as np
import scipy as sp
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def g(y, x):
    y1 = y[0]
    y2 = y[1]
    y3 = y[2]
    f1 = -0.04 * y1 + 10e+4*y2*y3
    f2 = 0.04*y1 - 10e+4*y2*y3 - 3 * 10e+7*y2*y2
    f3 = 3 * 10e+7*y2*y2
    return [f1, f2, f3]



init = 1.0, 0.0, 0
# First integrate from 0 to 2
x = np.linspace(0,3,300)
sol=odeint(g, init, x)

plt.figure(1)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y1')
plt.plot(x, sol[:,0], color='b')


#plt.figure(2)
#plt.grid(True)
#plt.xlabel('x')
#plt.ylabel('y2')
#plt.plot(x, sol[:,1], color='b')
#
#plt.figure(3)
#plt.grid(True)
#plt.xlabel('x')
#plt.ylabel('y3')
#plt.plot(x, sol[:,1], color='b')

plt.show()










