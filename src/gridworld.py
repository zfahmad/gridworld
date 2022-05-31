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

        if state > self.height * self.width or self.grid[row][col] == 1:
            print("Invalid state!")
            return []

        legalActions = ['N', 'S', 'E', 'W']
        return legalActions

    def apply_action(self, state, action) -> int:
        
        row = state // self.width
        col = state % self.width
        shift = 0

        if state > self.height * self.width or self.grid[row][col] == 1:
            print("Invalid state!")
            return state

        # print(f"state: {state} row: {row} col: {col}")
        
        if action == "W":
            if col - 1 >= 0 and self.grid[row][col - 1] != 1:
                shift = self.actions["W"]
            else:
                shift = 0

        if action == "E":
            if col + 1 < self.width and self.grid[row][col + 1] != 1:
                shift = self.actions["E"]
            else:
                shift = 0

        if action == "N":
            if row - 1 >= 0 and self.grid[row - 1][col] != 1:
                shift = self.actions["N"]
            else:
                shift = 0

        if action == "S":
            if row + 1 < self.height and self.grid[row + 1][col] != 1: 
                shift = self.actions["S"]
            else:
                shift = 0

        return state + shift

    def is_goal(self, state) -> bool:
        return state == self.goal
            
