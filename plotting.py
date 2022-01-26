import numpy as np
import matplotlib.pyplot as plt

Na=100
Nb=0
T=1000
t=0

time=[]
mol_A=[]
mol_B=[]

while True:
  if(Na==0):
    break
  k1 = 1
  k_1 = 2
  W = k1*Na
  tau= -np.log(np.random.uniform(0,1))/W
  t+=tau
  r=np.random.randn()*W
  if (r<W):
    Na-=1
    Nb+=1
  time.append(t)
  mol_A.append(Na)
  mol_B.append(Nb)

  if (t>T):
    break

plt.plot(time, mol_A, '-k', label='A')
plt.plot(time, mol_B, '--g', label='B')

plt.ylabel('concentration')
plt.xlabel('time')

plt.legend()
plt.show()


#A

class Transformation(gillespy2.Model):
    def __init__(self, parameter_values=None):
        # First call the gillespy2.Model initializer.
        gillespy2.Model.__init__(self, name='Transformation')

        # Define parameters for the rates of creation and dissociation.
        k_f = gillespy2.Parameter(name='k_f', expression=1)
        k_b = gillespy2.Parameter(name='k_b', expression=2)
        self.add_parameter([k_f, k_b])

        # Define variables for the molecular species representing M and D.
        m = gillespy2.Species(name='monomer', initial_value=2)
        d = gillespy2.Species(name='dimer',   initial_value=0)
        self.add_species([m, d])

        # The list of reactants and products for a Reaction object are each a
        # Python dictionary in which the dictionary keys are Species objects
        # and the values are stoichiometries of the species in the reaction.
        r_c = gillespy2.Reaction(name="A_becoming_B", rate=k_f, reactants={m:1}, products={d:1})
        r_d = gillespy2.Reaction(name="B_becoming_A", rate=k_b, reactants={d:1}, products={m:1})
        self.add_reaction([r_c, r_d])

        # Set the timespan for the simulation.
        self.timespan(numpy.linspace(0, 100, 101))


#B

import numpy as np
import matplotlib.pyplot as plt
omega = 4
lambda_scaling=10
class Bimolecular(gillespy2.Model):
    def __init__(self, parameter_values=None):
        # First call the gillespy2.Model initializer.
        gillespy2.Model.__init__(self, name='Bimolecular')

        # Define parameters for the rates of creation and dissociation.
        k_f = gillespy2.Parameter(name='k_f', expression=1/(omega))
        k_b = gillespy2.Parameter(name='k_b', expression=2/(omega))
        self.add_parameter([k_f, k_b])

        # Define variables for the molecular species representing M and D.
        A = gillespy2.Species(name='species_A', initial_value=3*lambda_scaling)
        B = gillespy2.Species(name='species_B', initial_value=1*lambda_scaling)
        C = gillespy2.Species(name='species_C',   initial_value=0*lambda_scaling)
        self.add_species([A, B, C])

        # The list of reactants and products for a Reaction object are each a
        # Python dictionary in which the dictionary keys are Species objects
        # and the values are stoichiometries of the species in the reaction.
        r_1 = gillespy2.Reaction(name="AB_becoming_C", rate=k_f, reactants={A:1, B:1}, products={C:1})
        r_2 = gillespy2.Reaction(name="C_becoming_AB", rate=k_b, reactants={C:1}, products={A:1, B:1})
        self.add_reaction([r_1, r_2])

        # Set the timespan for the simulation.
        self.timespan(np.linspace(0, 100, 101))

model = Bimolecular()
results1 = model.run(number_of_trajectories=10)

results1.plot(figsize=(8,6))
