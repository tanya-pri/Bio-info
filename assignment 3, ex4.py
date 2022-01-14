import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

k_1 = 0.01
k__1 = 35
k_2 = 30

def enzyme_substrate(y, t, k_1, k__1, k_2):
  S=[]
  E=[]
  ES=[]
  P=[]
  S, E, ES, P = y
  dydt = [(k__1*ES) + ((-k_1)*E*S),
          ((-k_1)*E*S) + (k_2)*ES + (k__1)*ES,
          (-k__1)*ES - (k_2)*ES + ((k_1)*E*S),
          (k_2)*ES]
  return dydt

y0 = [20, 15, 0, 0]
t = np.linspace(0,200,30)

#scipy.integrate.odeint(func, y0(:array), t(:array), args=(), Dfun=None, col_deriv=0, full_output=0, mu=None, h0=0.0, hmax=0.0, hmin=0.0)
model = odeint(enzyme_substrate, y0, t, args=(k_1, k__1, k_2))

plt.plot(t, model[:, 0], 'r', label='S(t)')
plt.plot(t, model[:, 1], 'b', label='E(t)')
plt.plot(t, model[:, 2], 'g', label='ES(t)')
plt.plot(t, model[:, 3], 'y', label='P(t)')
plt.xlabel('Time')
plt.ylabel('Concentrations')
plt.title('Enzyme substrate model')
plt.legend()