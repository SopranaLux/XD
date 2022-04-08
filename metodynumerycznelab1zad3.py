import numpy as np
import matplotlib.pyplot as plt
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('png', 'pdf')

def df(f, x,  h = 10**(-7)):
    return (f(x + h) - f(x)) / h
def f2(x):
    return ((x - 2)**2) -1
def newton(f, x0, eps = 10**-4, max_iter=100):
    x1 = x0
    for n in range(0, max_iter):
        fxn = f(x1)
        if abs(fxn) < eps:
            return x1
        dfxn = df(f, x1)
        if dfxn == 0:
            x1 = None
            return x1
        x1 = x1 - fxn/dfxn
    x1 = None
    return x1
print(newton(f2, 4))

def newton_vis(f, x0, eps = 10**-4, max_iter=100):
    x = np.arange(1.75, 6.25, eps)
    y = [f(n)for n in x]
    x1 = x0
    for n in range(0, max_iter):
        fxn = f(x1)
        if abs(fxn) < eps:
            return x1
        dfxn = df(f, x1)
        if dfxn == 0:
            x1 = None
            return x1
        x1 = x1 - fxn/dfxn
    x1 = None
    return x1
print(newton_vis(f2, 4))