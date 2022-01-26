import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

k1 = 1
k_1 = 2

def model(z, t, k1, k_1):
  A = z[0]
  B = z[1]
  dAdt= -k1* A + k_1*B
  dBdt= -k_1* B + k1 *A
  return [dAdt, dBdt]
z0 = [2,0]
t = np.linspace(0, 200, 100)
z = odeint(model, z0, t, args=(k1, k_1))
A = z[:,0]
B = z[:,1]

plt.plot(t, A, '-k', label='A')
plt.plot(t, B, '--g', label='B')
plt.ylabel('concentration')
plt.xlabel('time')
plt.legend()
plt.show()

#stochastic model

class Transformation(gillespy2.Model):
  def __init__(self, parameter_values=None):
    # First call the gillespy2.Model initializer.
    gillespy2.Model.__init__(self, name='Transformation')

    # Define parameters for the rates of creation and dissociation.
    k_f = gillespy2.Parameter(name='k_f', expression=0.005)
    k_b = gillespy2.Parameter(name='k_b', expression=0.08)
    self.add_parameter([k_f, k_b])

    # Define variables for the molecular species representing M and D.
    m = gillespy2.Species(name='monomer', initial_value=2)
    d = gillespy2.Species(name='dimer', initial_value=0)
    self.add_species([m, d])

    # The list of reactants and products for a Reaction object are each a
    # Python dictionary in which the dictionary keys are Species objects
    # and the values are stoichiometries of the species in the reaction.
    r_c = gillespy2.Reaction(name="A_becoming_B", rate=k_f, reactants={m: 1}, products={d: 1})
    r_d = gillespy2.Reaction(name="B_becoming_A", rate=k_b, reactants={d: 1}, products={m: 1})
    self.add_reaction([r_c, r_d])

    # Set the timespan for the simulation.
    self.timespan(numpy.linspace(0, 100, 101))
