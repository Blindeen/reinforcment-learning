from classes.environment import Environment
from enums.colors import Colors

import pygame as p


class LineEnvironment(Environment):
    def __init__(self, length, finish, surface):
        self.track_index = 0
        self.length = length
        self.finish = finish
        self.surface = surface

    def step(self, action):
        if action == 0:
            if self.track_index != 0:
                self.track_index -= 1
        if action == 1:
            if self.track_index != self.length - 1:
                self.track_index += 1

        if self.track_index == self.finish:
            reward = 1
            done = True
        else:
            reward = 0
            done = False

        return self.track_index, reward, done

    def reset(self):
        self.track_index = 0
        return self.track_index

    def get_possible_actions(self, state=None):
        if state is None:
            return [0, 1]
        else:
            if state == 0:
                return [1]

    def init_gui(self):
        p.init()
        p.display.set_caption('Linear reinforcment learning')

        for col in range(self.length):
            p.draw.rect(self.surface, Colors.WHITE.value, p.Rect(col * 101, 0, 99, 99))

        p.display.flip()

    def reset_gui(self):
        p.draw.rect(self.surface, Colors.GOLD.value, p.Rect(self.finish * 101, 0, 99, 99))
        p.draw.rect(self.surface, Colors.RED.value, p.Rect(self.track_index, 0, 99, 99))
        p.display.flip()

    def color_rectangle(self, color, cooridinates):
        p.draw.rect(self.surface, color, p.Rect(cooridinates * 101, 0, 99, 99))
        p.display.flip()
