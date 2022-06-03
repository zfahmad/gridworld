from agents.agent import Agent

class Agent(Agent):
    def __init__(self, name, num_states, n, gamma, policy, alpha):
        self.name = name
        self.q_table = self.init_q_table(num_states)
        self.actions = ["N", "S", "E", "W"]
        self.n = n
        self.gamma = gamma
        self.policy = policy
        self.alpha = alpha
        self.stored_states = []
        self.stored_actions = []
        self.stored_rewards = [0]

    def reset_agent(self):
        self.stored_states = []
        self.stored_actions = []
        self.stored_rewards = [0]

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

    def update(self, tau, T):
        G = sum([self.gamma**(i-tau-1)*self.stored_rewards[i] 
           for i in range(tau+1, min(tau+self.n, T)+1)])
        if tau + self.n < T:
            ind = tau + self.n
            G += self.gamma**(self.n) * self.q_table[self.stored_states[ind]][self.actions.index(self.stored_actions[ind])]
        val = self.q_table[self.stored_states[tau]][self.actions.index(self.stored_actions[tau])]
        self.q_table[self.stored_states[tau]][self.actions.index(self.stored_actions[tau])] = val + self.alpha * (G - val)
