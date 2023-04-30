from classes.agent import Agent
from classes.square_environment import SquareEnvironment
from enums.constants import Constants

# Square reinforcment learning
qtable = {}
episodes_number = 100000
dimensions = (4, 4)
finish_coordinates = (3, 3)
agent = Agent(Constants.ALFA.value, Constants.GAMMA.value, qtable)
environment = SquareEnvironment(dimensions, finish_coordinates)

agent.learn(episodes_number, environment)
agent.display_qtable()
