from random import random
from agents.agent import Agent
import policies.tabular_policies as tp
from numpy import Inf

class Agent(Agent):
    def __init__(self, name, num_states, gamma, policy, alpha):
        self.name = name
        self.q_table = self.init_q_table(num_states)
        self.actions = ["N", "S", "E", "W"]
        self.gamma = gamma
        self.policy = policy
        self.alpha = alpha

    def init_q_table(self, num_states):
        q_table = []
        for _ in range(num_states):
            state_action_values = []
            for _ in range(4):
                state_action_values.append(0.0)
            q_table.append(state_action_values)
        return q_table

    def select_action(self, state) -> str:
        action_index = self.policy(self.q_table[state])
        return self.actions[action_index]
    
    def update(self, state, action, reward, next_state, next_action):
        q_val = self.q_table[state][self.actions.index(action)]

        max_value = -Inf
        for ind, val in enumerate(self.q_table[next_state]):
            if val > max_value:
                max_value = val

        q_prime_val = max_value

        self.q_table[state][self.actions.index(action)] = q_val + \
            self.alpha * (reward + self.gamma * q_prime_val - q_val)
        
