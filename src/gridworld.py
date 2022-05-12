class Gridworld:
    def __init__(self, height: int, width: int, start: int, goal: int):
        self.height = height
        self.width = width
        self.grid = []

        # Initialize the gridworld with a specified
        # number of rows and columns

        for _ in range(height):
            row = []
            for _ in range(width):
                row.append(0)
            self.grid.append(row)

        self.actions = { "N": -width, "E": 1, "S": width, "W": -1 }
        self.start = start
        self.goal = goal

    def reset(self):
        # Return the state to the start state
        return self.start

    def print_grid(self):
        # Print gridworld to terminal
        print(self.grid)

    def get_actions(self, state: int) -> list: 
        # Return a list of legal actions
        # Legal actions constitutes a movement in cardinal direction
        row = state // self.width
        col = state % self.width
        legalActions = []

        if state > self.height * self.width or self.grid[row][col] == 1:
            print("Invalid state!")
            return []

        # print(f"state: {state} row: {row} col: {col}")
        
        if col - 1 >= 0:
            if self.grid[row][col - 1] != 1:
                legalActions.append("W")

        if col + 1 < self.width:
            if self.grid[row][col + 1] != 1:
                legalActions.append("E")

        if row - 1 >= 0:
            if self.grid[row - 1][col] != 1:
                legalActions.append("N")

        if row + 1 < self.height:
            if self.grid[row + 1][col] != 1: 
                legalActions.append("S")

        return legalActions

    def apply_action(self, state, action) -> int:
        try:
            if action not in self.get_actions(state):
                raise ValueError
        except ValueError:
            print("Invalid action!")
            return state

        return state + self.actions[action]

    def is_goal(self, state) -> bool:
        return state == self.goal
            
