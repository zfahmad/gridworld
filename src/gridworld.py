class Gridworld:
    def __init__(self, height: int, width: int, start: int, goal: int):
        self.height = height
        self.width = width
        self.grid = []

        for _ in range(height):
            row = []
            for _ in range(width):
                row.append(0)
            self.grid.append(row)

        self.actions = { "N": -width, "E": 1, "S": width, "W": -1 }
        self.start = start
        self.goal = goal

    def reset(self):
        return self.start

    def print_grid(self):
        print(self.grid)

    def get_actions(self, state: int) -> list: 
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
            


if __name__ == "__main__":
    gw = Gridworld(4, 5, 0, 19)
    gw.print_grid()
    print(gw.get_actions(0))
    print(gw.is_goal(0))
    print(gw.get_actions(19))
    print(gw.is_goal(19))
    print(gw.get_actions(6))
    print(gw.is_goal(6))
    print(gw.get_actions(10))
    print(gw.is_goal(10))
    print(gw.get_actions(34))
    print(gw.is_goal(34))
    
    for action in ["N", "E", "S", "W"]:
        print(gw.apply_action(6, action))
    
    for action in ["N", "E", "S", "W"]:
        print(gw.apply_action(5, action))
