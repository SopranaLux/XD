import math
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('png', 'pdf')

def golden_section(f, a, b, eps=10**-4, max_iter=100):
    k = (math.sqrt(5) -1) / 2
    xl = b - k *(b -a)
    xr = a + k * (b - a)
    iter = 0
    while abs(a-b)>eps and iter < max_iter:
        srodek = (a+b) / 2
        if f(xl) < f(xr):
            b = xr
            xr = xl
            xl = b - k * ( b - a)
        else:
            a = xl
            xl = xr
            xr = a + k * (b -a)
        iter +=1 
    return srodek
def f2(x):
    return (x - 2)**2 - 1
print(golden_section(f2, 0, 5))

def golden_section_vis(f, a, b, eps=10**-4, max_iter=100):
    x = np.arange(a, b, eps)
    y = [f(n)for n in x]
    fig, ax = plt.subplots()
    ax.plot(x,y, linewidth=2.0)
    ax.grid(color = 'g', linestyle='--',linewidth=1.15, alpha=0.5)
    k = (math.sqrt(5) -1) / 2
    xl = b - k *(b -a)
    xr = a + k * (b - a)
    iter = 0
    while abs(a-b)>eps and iter < max_iter:
        srodek = (a+b) / 2
        plt.axvline(srodek)
        if f(xl) < f(xr):
            b = xr
            xr = xl
            xl = b - k * ( b - a)
        else:
            a = xl
            xl = xr
            xr = a + k * (b -a)
        iter +=1
    plt.show() 
    return srodek
print(golden_section_vis(f2, 0, 5))
