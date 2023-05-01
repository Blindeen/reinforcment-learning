from classes.agent import Agent
from classes.linear_environment import LineEnvironment
from enums.constants import Constants

import pygame as p

# Linear reinforcment learning
qtable = {}
episodes_number = 100000
length = 6
finish = 5
surface = p.display.set_mode((600, 100))
agent = Agent(Constants.ALFA.value, Constants.GAMMA.value, qtable)
environment = LineEnvironment(length, finish, surface)
environment.init_gui()

agent.learn(episodes_number, environment, True)
agent.display_qtable()
