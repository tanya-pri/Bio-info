import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
h = 0.0001
t = np.linspace(1, 100, 100)
S=0.3
Vmax=3
Km=3
P0=0
Si=0


def y(Vmax, Si, Km, h):
    a = []
    b = []
    S = Si
    while S < 100:
        a.append(Vmax * S / (S + Km)), b.append(S)
        S += h
    plt.xlabel('[S]')
    plt.ylabel('V')
    plt.title('velocity of the reaction as a function of time', fontsize='large')
    plt.plot(b, a)


y(Vmax, Si, Km, h)