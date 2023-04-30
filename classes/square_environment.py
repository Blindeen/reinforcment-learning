from classes.environment import Environment
from enums.square_environment_moves import Moves


class SquareEnvironment(Environment):
    def __init__(self, dimensions, finish_cooridinates):
        self.track_index_x = 0
        self.track_index_y = 0
        self.dimensions = dimensions
        self.finish_cooridinates = finish_cooridinates

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
