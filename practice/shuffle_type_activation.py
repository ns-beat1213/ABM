# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 23:07:53 2023

@author: nsbea
"""

import mesa


class MoneyAgent(mesa.Agent):
    """An agent with fixed initial wealth."""

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1

    def step(self):
        # The agent's step will go here.
        # For demonstration purposes we will print the agent's unique_id
        print("Hi, I am agent " + str(self.unique_id) + ".")

class AddAgent(mesa.Agent):
    """An agent with fixed initial wealth."""

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1

    def step(self):
        # The agent's step will go here.
        # For demonstration purposes we will print the agent's unique_id
        print("Hi, I am added agent " + str(self.unique_id) + ".")


class MoneyModel(mesa.Model):
    """A model with some number of agents."""

    def __init__(self, N):
        self.num_agents = N
        self.schedule = mesa.time.RandomActivationByType(self)
        # Create agents
        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
            self.schedule.add(a)
        for i in range(self.num_agents):
            b = AddAgent(i+self.num_agents, self)
            self.schedule.add(b)

    def step(self):
        """Advance the model by one step."""
        self.schedule.step(shuffle_types=False, shuffle_agents=False)
        

empty_model = MoneyModel(3)
empty_model.step()
