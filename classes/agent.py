import random
import time
import numpy as np

from enums.colors import Colors


class Agent:
    def __init__(self, alfa, gamma, qtable):
        self.alfa = alfa
        self.gamma = gamma
        self.qtable = qtable

    def get_action(self, state, possible_actions):
        if state not in self.qtable:
            action = random.choice(possible_actions)
            self.qtable[state] = np.zeros(len(possible_actions))
        else:
            row = self.qtable[state]
            max_value = max(row)
            min_value = min(row)
            if max_value == min_value:
                action = random.choice(possible_actions)
            else:
                if random.randint(0, 10) == 0:
                    action = random.choice(possible_actions)
                else:
                    action = np.argmax(row)

        return action

    def get_best_action(self, state, possible_actions):
        row = self.qtable[state]
        max_value = max(row)
        min_value = min(row)
        if max_value == min_value:
            action = random.choice(possible_actions)
        else:
            action = np.argmax(row)

        return action

    def update(self, state, action, next_state, reward):
        if next_state not in self.qtable:
            self.qtable[next_state] = np.zeros(len(self.qtable[state]))
        self.qtable[state][action] += \
            self.alfa * (reward + self.gamma * max(self.qtable[next_state]) - self.qtable[state][action])

    def learn(self, episodes_number, environment, gui=False):
        for i in range(episodes_number):
            state = environment.reset()
            if gui is not False:
                environment.reset_gui()
                time.sleep(0.5)
            done = False

            while not done:
                action = self.get_action(state, environment.get_possible_actions())
                next_state, reward, done = environment.step(action)
                if next_state != state and gui is not False:
                    environment.color_rectangle(Colors.WHITE.value, state)
                    environment.color_rectangle(Colors.RED.value, next_state)
                    time.sleep(0.1)
                self.update(state, action, next_state, reward)
                state = next_state

    def display_qtable(self):
        for key in self.qtable:
            print(key, '->', self.qtable[key])
