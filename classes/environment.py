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
