from classes.agent import Agent
from classes.square_environment import SquareEnvironment
from enums.constants import Constants

import pygame as p

# Square reinforcment learning
qtable = {}
episodes_number = 100000
dimensions = (4, 4)
finish_coordinates = (3, 1)
surface = p.display.set_mode((400, 400))
agent = Agent(Constants.ALFA.value, Constants.GAMMA.value, qtable)
environment = SquareEnvironment(dimensions, finish_coordinates, surface)
environment.init_gui()

agent.learn(episodes_number, environment, True)
agent.display_qtable()
