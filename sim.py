import math
import sympy
import numpy as np
import matplotlib.pyplot as plt

# x = math.sqrt(24)
y = sympy.sqrt(24)

# print(x)
# print(y)

a, b = sympy.symbols('a b')
e = 2*a + 4*a*b + 6*b**2
print(e)
print(e-a)
#
# d = sympy.symbols('d')
# solution1 = sympy.solve(d**2 + 6*d + 9)
# print(solution1)
#
# solution2 = sympy.solve(2*d**2 - 6*d + 9)
# print(solution2)

def graph(formula, data_range):
    x = np.array(data_range)
    y = eval(formula)
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))
    plt.plot(x, y)
    plt.show()

graph('2*x**2 - 6*x + 9', range(-20,20))
