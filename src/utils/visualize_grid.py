import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle


def draw_gridworld(gw, start, goal, state):
    sq_height = 1 / gw.height
    sq_width = 1 / gw.width
    x = 0
    y = 0

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.plot = ([0, 1], [0, 1])

    for row in range(gw.height):
        for col in range(gw.width):
            if gw.grid[col][row] == 1:
                ax.add_patch(Rectangle((x, y), sq_width, sq_height, 
                         edgecolor='black', facecolor='black', lw=1))
            else:
                ax.add_patch(Rectangle((x, y), sq_width, sq_height, 
                         edgecolor='black', facecolor='white', lw=1))

            x += sq_width 
        y += sq_height
        x = 0

    x = goal // gw.height * sq_width
    y = goal % gw.height * sq_height
    ax.add_patch(Rectangle((x, y), sq_width, sq_height, 
                 edgecolor='black', facecolor='darkgreen', lw=1, alpha=0.6))

    x = start // gw.height * sq_width
    y = start % gw.height * sq_height
    ax.add_patch(Rectangle((x, y), sq_width, sq_height, 
                 edgecolor='black', facecolor='slateblue', lw=1, alpha=0.6))

    x = state // gw.height * sq_width + 0.5 * sq_width
    y = state % gw.height * sq_height + 0.5 * sq_height
    ax.add_patch(Circle((x, y), radius=0.3*min(sq_height, sq_width), 
                 edgecolor='black', facecolor='orange', lw=3))


    plt.show()

