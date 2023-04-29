from classes.agent import Agent
from classes.square_environment import SquareEnvironment

# Square reinforcment learning
finish_coordinates = (3, 3)
qtable = {}
agent = Agent(0.1, 0.9, qtable)
environment = SquareEnvironment(finish_coordinates)

agent.learn(100000, environment)
agent.display_qtable()
