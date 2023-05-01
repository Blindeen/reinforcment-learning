from classes.environment import Environment
from enums.square_environment_moves import Moves
from enums.colors import Colors

import pygame as p


class SquareEnvironment(Environment):
    def __init__(self, dimensions, finish_cooridinates, surface):
        self.track_index_x = 0
        self.track_index_y = 0
        self.dimensions = dimensions
        self.finish_cooridinates = finish_cooridinates
        self.surface = surface

    def step(self, action):
        if action == Moves.LEFT.value:
            if self.track_index_x != 0:
                self.track_index_x -= 1
        elif action == Moves.RIGHT.value:
            if self.track_index_x != self.dimensions[1] - 1:
                self.track_index_x += 1
        elif action == Moves.UP.value:
            if self.track_index_y != 0:
                self.track_index_y -= 1
        elif action == Moves.DOWN.value:
            if self.track_index_y != self.dimensions[0] - 1:
                self.track_index_y += 1

        if (self.track_index_y, self.track_index_x) == self.finish_cooridinates:
            reward = 1
            done = True
        else:
            reward = 0
            done = False

        return (self.track_index_y, self.track_index_x), reward, done

    def reset(self):
        self.track_index_x = 0
        self.track_index_y = 0
        return self.track_index_y, self.track_index_x

    def get_possible_actions(self, state=None):
        if state is None:
            return [Moves.LEFT.value, Moves.RIGHT.value, Moves.UP.value, Moves.DOWN.value]

    def init_gui(self):
        p.init()
        p.display.set_caption('Square reinforcment learning')

        for row in range(self.dimensions[0]):
            for col in range(self.dimensions[1]):
                p.draw.rect(self.surface, Colors.WHITE.value, p.Rect(col * 101, row * 101, 99, 99))

        p.display.flip()

    def reset_gui(self):
        p.draw.rect(
            self.surface, Colors.GOLD.value,
            p.Rect(self.finish_cooridinates[1] * 101,
                   self.finish_cooridinates[0] * 101,
                   99,
                   99
                   )
        )
        p.draw.rect(self.surface, Colors.RED.value, p.Rect(self.track_index_y, self.track_index_x, 99, 99))
        p.display.flip()

    def color_rectangle(self, color, coordinates):
        p.draw.rect(self.surface, color, p.Rect(coordinates[1] * 101, coordinates[0] * 101, 99, 99))
        p.display.flip()
