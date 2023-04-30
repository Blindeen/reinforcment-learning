from classes.agent import Agent
from classes.linear_environment import LineEnvironment
from enums.constants import Constants

# Linear reinforcment learning
qtable = {}
episodes_number = 100000
length = 6
finish = 5
agent = Agent(Constants.ALFA.value, Constants.GAMMA.value, qtable)
environment = LineEnvironment(length, finish)

agent.learn(episodes_number, environment)
agent.display_qtable()
