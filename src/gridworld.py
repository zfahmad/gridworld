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

    def printGrid(self):
        print(self.grid)

    def getActions(self, state: int) -> list: 
        row = state // self.width
        col = state % self.width
        legalActions = []

        if state > self.height * self.width or self.grid[row][col] == 1:
            print("Invalid state!")
            return []

        print(f"state: {state} row: {row} col: {col}")
        
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

    def applyAction(self, state, action) -> int:
        if action not in self.getActions(state):
            print("Invalid action!")
            return state
        return state + self.actions[action]

    def isGoal(self, state) -> bool:
        return state == self.goal
            


if __name__ == "__main__":
    gw = Gridworld(4, 5, 0, 19)
    gw.printGrid()
    print(gw.getActions(0))
    print(gw.isGoal(0))
    print(gw.getActions(19))
    print(gw.isGoal(19))
    print(gw.getActions(6))
    print(gw.isGoal(6))
    print(gw.getActions(10))
    print(gw.isGoal(10))
    print(gw.getActions(34))
    print(gw.isGoal(34))
    
    for action in ["N", "E", "S", "W"]:
        print(gw.applyAction(6, action))
    
    for action in ["N", "E", "S", "W"]:
        print(gw.applyAction(5, action))
