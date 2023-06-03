from gridworld import Gridworld
from utils.visualize_grid import draw_gridworld

gw = Gridworld(11, 11, 0, 96)
for i in range(11):
    gw.grid[5][i] = 1
for i in range(11):
    gw.grid[i][5] = 1
gw.grid[5][2] = 0
gw.grid[5][8] = 0
gw.grid[2][5] = 0
gw.grid[8][5] = 0
print(gw.grid)
draw_gridworld(gw, gw.start, gw.goal, 0)
