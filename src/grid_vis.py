from gridworld import Gridworld
from utils.visualize_grid import draw_gridworld

gw = Gridworld(10, 10, 0, 19)
gw.grid[1][1] = 1
gw.grid[1][2] = 1
gw.grid[1][3] = 1
gw.grid[1][4] = 1
print(gw.grid)
draw_gridworld(gw, gw.start, gw.goal, 0)
