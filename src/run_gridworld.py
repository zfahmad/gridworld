from absl import app
from absl import flags
from gridworld import Gridworld
import policies.tabular_policies
import matplotlib.pyplot as plt
import numpy as np
import importlib


FLAGS = flags.FLAGS
flags.DEFINE_integer("max_steps", 500, "Maximum number of steps per episode.")
flags.DEFINE_integer("num_episodes", 50, "Number of episodes.")
flags.DEFINE_integer("num_trials", 10, "Number of trials to run.")
flags.DEFINE_string("policy", None, "Policy to use for selecting actions.")
flags.DEFINE_string("agent", None, "RL algorithm for agent to use.")
flags.DEFINE_float("gamma", 0.99, "Discount factor.")
flags.DEFINE_float("alpha", 0.1, "Learning rate.")


def main(argv):
    del argv
    gw = Gridworld(10, 10, 0, 80)
    for i in range(7):
        gw.grid[7][i] = 1
    agent_module = importlib.import_module("agents." + FLAGS.agent)

    avg_num_steps = np.zeros(FLAGS.num_episodes)
    policy = getattr(policies.tabular_policies, FLAGS.policy)

    for trial in range(FLAGS.num_trials):
        agent = agent_module.Agent(FLAGS.agent, gw.width * gw.height, 
                                  FLAGS.gamma, policy, FLAGS.alpha)
        steps_per_episode = []

        for episode in range(FLAGS.num_episodes):
            state = gw.start
            action = agent.select_action(state)
            step = 0
            terminate = False
            while step < FLAGS.max_steps and not terminate:
                next_state = gw.apply_action(state, action)
                terminate, reward = gw.is_goal(next_state)
                next_action = agent.select_action(next_state)
                agent.update(state, action, reward, next_state, next_action)
                state = next_state
                action = next_action
                step += 1
            steps_per_episode.append(step)
        
        avg_num_steps += np.array(steps_per_episode)

    avg_num_steps = avg_num_steps / FLAGS.num_trials
    plt.plot(avg_num_steps)
    plt.show()


if __name__ == "__main__":
    app.run(main)
