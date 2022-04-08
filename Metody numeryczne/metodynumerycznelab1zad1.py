from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('png', 'pdf')

def f(x):
    return (x-2)**3-x**2+2*x
def bisection_method(f, a, b, eps=10**-4, max_iter=100):
    srodek = 0
    iter = 0
    while abs(a-b)>eps and iter < max_iter:
        srodek = (a+b) / 2
        if f(a) * f(srodek) < 0:
            b = srodek
        elif f(b) * f(srodek) < 0:
            a = srodek
        elif f(srodek) == 0:
            return srodek
    return srodek

print(bisection_method(f, 1.5, 3, eps=10**-6))

def bisection_method_vis(f, a, b, eps=10**-4, max_iter=100):
    x = np.arange(a, b, eps)
    y = [f(n)for n in x]
    fig, ax = plt.subplots()
    ax.plot(x,y, linewidth=2.0)
    ax.grid(color = 'g', linestyle='--',linewidth=1.15, alpha=0.5)
    srodek = 0
    iter = 0
    while abs(a-b)>eps and iter < max_iter:
        srodek = (a+b) / 2
        plt.axvline(srodek)
        if f(a) * f(srodek) < 0:
            b = srodek
        elif f(b) * f(srodek) < 0:
            a = srodek
        elif f(srodek) == 0:
            return srodek
    plt.show()
    return srodek

print(bisection_method_vis(f, 1.5, 3, eps=10**-6))