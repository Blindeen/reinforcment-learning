from classes.agent import Agent
from classes.linear_environment import LineEnvironment

import numpy as np

# Linear reinforcment learning
track = np.array(['S', ' ', ' ', ' ', ' ', 'G'])
qtable = {}
agent = Agent(0.1, 0.9, qtable)
environment = LineEnvironment(track)

agent.learn(100000, environment)

agent.display_qtable()
