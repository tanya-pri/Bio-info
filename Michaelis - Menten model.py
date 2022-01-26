class MichaelisMenten(Model):
    def __init__(self, parameter_values=None):
        Model.__init__(self, name='Michaelis_Menten')

        # parameters
        k1 = Parameter(name='k1', expression=0.01)
        k_1 = Parameter(name='k_1', expression=35)
        k2 = Parameter(name='k2', expression=30)
        self.add_parameter([k1, k_1, k2])

        # Species
        S = Species(name='Substrate', initial_value=301)
        E = Species(name='Enzyme', initial_value=120)
        ES = Species(name='Complex ES', initial_value=0)
        P = Species(name='Product', initial_value=0)
        self.add_species([S, E, ES, P])

        # reactions
        r1 = Reaction(name="r1", reactants={S: 1, E: 1}, products={ES: 1}, rate=k1)

        r2 = Reaction(name="r2", reactants={ES: 1}, products={S: 1, E: 1}, rate=k_1)

        r3 = Reaction(name="r3", reactants={ES: 1}, products={E: 1, P: 1}, rate=k2)
        self.add_reaction([r1, r2, r3])
        self.timespan(np.linspace(0, 100, 101))
example9 = MichaelisMenten()
results9 = example9.run(number_of_trajectories=10)
results9.plot()