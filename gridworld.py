import random as rnd


class GridWorld:
    def __init__(self, grid_spec):

        grid_spec = grid_spec.split('|')

        self.dim = [int(i) for i in grid_spec[0].split(',')]
        goal = [int(i) for i in grid_spec[-1].split(',')]
        self.start = [int(i) for i in grid_spec[-2].split(',')]

        grid = []

        for i in range(self.dim[0]):
            row = []
            for j in range(self.dim[1]):
                row.append(' ')
            grid.append(row)

        grid[self.start[0]][self.start[1]] = '@'
        grid[goal[0]][goal[1]] = 'O'

        for spec in grid_spec[1:-2]:

            wall = spec.split(':')
            beg = [int(i) for i in wall[0].split(',')]
            end = [int(i) for i in wall[1].split(',')]

            for i in range(beg[0], end[0] + 1):
                for j in range(beg[1], end[1] + 1):
                    grid[i][j] = 'x'

        self.grid = grid

    def get_actions(self, state):
        actions = []

        # Check for North move

        if state[0] - 1 >= 0:
            if self.grid[state[0] - 1][state[1]] != 'x':
                actions.append('N')

        # Check for South move

        if state[0] + 1 < self.dim[0]:
            if self.grid[state[0] + 1][state[1]] != 'x':
                actions.append('S')

        # Check for West move

        if state[1] - 1 >= 0:
            if self.grid[state[0]][state[1] - 1] != 'x':
                actions.append('W')

        # Check for East move

        if state[1] + 1 < self.dim[1]:
            if self.grid[state[0]][state[1] + 1] != 'x':
                actions.append('E')

        return actions

    def get_new_state(self, state, action):

        if action == "N":
            new_state = [state[0] - 1, state[1]]
        elif action == "S":
            new_state = [state[0] + 1, state[1]]
        elif action == "E":
            new_state = [state[0], state[1] + 1]
        else:
            new_state = [state[0], state[1] - 1]

        return new_state

    def reward(self, state):
        if self.grid[state[0]][state[1]] == 'O':
            r = 1
        else:
            r = 0

        return r

    def print_maze(self):
        height = len(self.grid)
        # width = len(self.board[0])

        for i in range(height):
            print('| ' + ' '.join(self.grid[i]) + ' |')


class Agent:
    def __init__(self, grid, gamma=1.0, t=100, epsilon=0.1, alpha=0.5):
        self.grid = grid
        self.gamma = gamma
        self.t = t
        self.start = self.grid.start
        self.epsilon = epsilon
        self.alpha = alpha

        self.V = []
        self.Q = []

        for i in range(grid.dim[0]):
            row = []
            for j in range(grid.dim[1]):
                row.append(0)
            self.V.append(row)

        for i in range(grid.dim[0]):
            row = []
            for j in range(grid.dim[1]):
                row.append({'N': 0, 'S': 0, 'E': 0, 'W': 0})
            self.Q.append(row)

    def select(self, s, actions):
        ran = rnd.random()
        a_max = []
        val_max = 0

        if ran > self.epsilon:

            for key in actions:
                val = self.Q[s[0]][s[1]][key]
                if val > val_max:
                    val_max = val
                    a_max = [key]
                elif val == val_max:
                    a_max.append(key)

            action = rnd.choice(a_max)

        else:

            action = rnd.choice(actions)

        return action

    def q_learning(self, s):
        t = 0
        cum_r = 0
        actions = self.grid.get_actions(s)
        a = self.select(s, actions)

        while t < self.t and self.grid.grid[s[0]][s[1]] != 'O':
            s_ = self.grid.get_new_state(s, a)
            actions = self.grid.get_actions(s_)
            a_ = self.select(s_, actions)
            r = self.grid.reward(s_)
            cum_r += r
            self.Q[s[0]][s[1]][a] += self.alpha * (r + self.gamma * (
                self.Q[s_[0]][s_[1]][a_])
                                                   - self.Q[s[0]][s[1]][a])
            s = s_
            a = a_
            t += 1

        return cum_r

    def trials(self, num_trials):
        tot_r = 0
        for _ in range(num_trials):
            tot_r += self.q_learning(self.grid.start)


spec = '5,5|0,1:0,2|2,1:3,1|2,3:2,4|3,0:3,0|3,3:3,3|0,4:0,4|1,0|3,4'

m = GridWorld(spec)
m.print_maze()

ms = Agent(m, gamma=0.2, alpha=0.2)
ms.trials(1000)
