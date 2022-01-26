'''1. What are the volume corrections for the stochastic rate constants cf and cb , and the species’ copy numbers, when scaling the volume by a factor of λ, if we are operating under the constraints of the thermodynamic limit definition?
 - they are proportional to the omega.'''

#2 deterministic trajectory

mport numpy as np
import matplotlib.pyplot as plt
v = 4
lambda_scaling=10
class Bimolecular(gillespy2.Model):
    def __init__(self, parameter_values=None ):
        # First call the gillespy2.Model initializer.
        gillespy2.Model.__init__(self, name='Bimolecular')

        # Define parameters for the rates of creation and dissociation.
        k_f = gillespy2.Parameter(name='k_f', expression=1/(v*lambda_scaling))
        k_b = gillespy2.Parameter(name='k_b', expression=2/(v*lambda_scaling))
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
results1 = model.run(number_of_trajectories=1)
results1. plot_mean_stdev(xscale='linear', yscale='linear', xaxis_label='Time', yaxis_label='Concentration', title='Evolution of A, B and C concentrations', show_title=True, style='default', show_legend=True, included_species_list=[], ddof=0, save_png=False, figsize=(7,2))