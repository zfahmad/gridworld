from src.gridworld import Gridworld
from src.agents.sarsa import SarsaAgent
from src.policies.tabular_policies import epsilon_greedy
import matplotlib.pyplot as plt

gw = Gridworld(5, 5, 0, 24)
agent = SarsaAgent("sarsa", gw.width * gw.height, .99, "epsilon_greedy", 0.1, 0.1)
max_steps = 1000
num_episodes = 1000
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

plt.plot(steps_per_episode)
plt.show()
