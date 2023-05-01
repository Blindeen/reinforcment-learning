from abc import ABC, abstractmethod


class Environment(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def step(self, action):
        pass

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def get_possible_actions(self, state=None):
        pass

    @abstractmethod
    def init_gui(self):
        pass

    @abstractmethod
    def reset_gui(self):
        pass

    @abstractmethod
    def color_rectangle(self, color, cooridinates):
        pass
