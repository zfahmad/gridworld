from gridworld import Gridworld
from agents.sarsa import SarsaAgent
import policies.tabular_policies
import matplotlib.pyplot as plt
import numpy as np

gw = Gridworld(10, 10, 0, 80)
for i in range(7):
    gw.grid[7][i] = 1
max_steps = 1000
num_episodes = 200
num_trials = 100
avg_num_steps = np.zeros(num_episodes)
policy = getattr(policies.tabular_policies, "epsilon_greedy")

for trial in range(num_trials):
    agent = SarsaAgent("sarsa", gw.width * gw.height, .99, policy, 0.1)
    steps_per_episode = []

    for episode in range(num_episodes):
        state = gw.start
        action = agent.select_action(state)
        step = 0
        terminate = False
        while step < max_steps and not terminate:
            next_state = gw.apply_action(state, action)
            terminate, reward = gw.is_goal(next_state)
            next_action = agent.select_action(next_state)
            agent.update(state, action, reward, next_state, next_action)
            state = next_state
            action = next_action
            step += 1
        steps_per_episode.append(step)
    
    avg_num_steps += np.array(steps_per_episode)

avg_num_steps = avg_num_steps / num_trials
plt.plot(avg_num_steps)
plt.show()
