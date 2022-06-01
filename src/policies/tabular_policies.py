import random

from numpy import argmax, Inf

def epsilon_greedy(q_values: list, epsilon: float):
    # Returns max valued action with 1 - epsilon probability
    # Otherwise select a random action with epsilon probability
    
    rng_value = random.uniform(0, 1)
    if rng_value < epsilon:
        return random.choice(range(4))
    else:
        max_indices = []
        max_value = -Inf
        for ind, val in enumerate(q_values):
            if val > max_value:
                max_value = val
                max_indices = [ind]
            elif val == max_value:
                max_indices.append(ind)
        return random.choice(max_indices)

