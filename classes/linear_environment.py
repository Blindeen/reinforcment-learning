from classes.environment import Environment


class LineEnvironment(Environment):
    def __init__(self, length, finish):
        self.track_index = 0
        self.length = length
        self.finish = finish

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
