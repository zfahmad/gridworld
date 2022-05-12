from gridworld import Gridworld
from utils.visualize_grid import draw_gridworld

gw = Gridworld(10, 10, 0, 19)
gw.grid[1][1] = 1
gw.grid[2][1] = 1
gw.grid[3][1] = 1
gw.grid[4][1] = 1
draw_gridworld(gw, 4, 88, 0)
