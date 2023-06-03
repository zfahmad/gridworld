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
flags.DEFINE_integer("n", 1, "Forward steps.")
flags.DEFINE_string("log_path", "./", "Path to output directory.")
flags.DEFINE_string("log_file", "logfile", "Log filename.")


def main(argv):
    del argv
    gw = Gridworld(11, 11, 0, 62)
    for i in range(11):
        gw.grid[5][i] = 1
    for i in range(11):
        gw.grid[i][5] = 1
    gw.grid[5][2] = 0
    gw.grid[5][8] = 0
    gw.grid[2][5] = 0
    gw.grid[8][5] = 0
    agent_module = importlib.import_module("agents." + FLAGS.agent)

    avg_num_steps = np.zeros(FLAGS.num_episodes)
    policy = getattr(policies.tabular_policies, FLAGS.policy)

    for _ in range(FLAGS.num_trials):
        agent = agent_module.Agent(FLAGS.agent, gw.width * gw.height, 
                                  FLAGS.n, FLAGS.gamma, policy, FLAGS.alpha)
        steps_per_episode = []

        for _ in range(FLAGS.num_episodes):
            T = np.Inf
            state = gw.start
            agent.reset_agent()
            agent.stored_states.append(state)
            action = agent.select_action(state)
            agent.stored_actions.append(action)
            step = 0
            tau = 0
            while tau != T - 1:
                if step < T:
                    next_state = gw.apply_action(state, action)
                    terminate, reward = gw.is_goal(next_state)
                    agent.stored_states.append(next_state)
                    agent.stored_rewards.append(reward)
                    if terminate or step == FLAGS.max_steps - 1:
                        T = step + 1
                    else:
                        next_action = agent.select_action(next_state)
                        agent.stored_actions.append(next_action)
                        state = next_state
                        action = next_action
                tau = step - agent.n + 1
                if tau >= 0:
                    agent.update(tau, T) 
                step += 1

            steps_per_episode.append(step)
        
        avg_num_steps += np.array(steps_per_episode)

    avg_num_steps = avg_num_steps / FLAGS.num_trials
    np.save(FLAGS.log_path + "/" + FLAGS.log_file, avg_num_steps)
    plt.plot(avg_num_steps)
    plt.savefig(FLAGS.log_path + "/" + FLAGS.log_file)


if __name__ == "__main__":
    app.run(main)
