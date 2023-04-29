from classes.agent import Agent
from classes.linear_environment import LineEnvironment

import numpy as np

# Linear reinforcment learning
qtable = {}
episodes_number = 100000
finish = 5
agent = Agent(0.1, 0.9, qtable)
environment = LineEnvironment(finish)

agent.learn(episodes_number, environment)
agent.display_qtable()
