import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize the grid, the dots' position, and resolution (how many steps per step)
grid_size = 100
dot_positions = [[0, 0], [80, 40]]  # Starting positions for two dots
res = 20

# Define the instructions
instructions = [
    [('', 0)] + [('right', 20)] * 3 + [('up', 40)] * 2 + [('left', 20)] + [('down', 20)] * 2,
    [('', 0)] + [('left', 20)] * 3 + [('down', 20)] * 2 + [('right', 20)] + [('up', 40)] * 2
]

# Function to move the dot
def move_dot(dot_position, direction, steps):
    new_position = dot_position.copy()
    if direction == 'up':
        new_position[1] += steps
    elif direction == 'down':
        new_position[1] -= steps
    elif direction == 'left':
        new_position[0] -= steps
    elif direction == 'right':
        new_position[0] += steps
    return new_position

# Create the figure and axis objects
fig, ax = plt.subplots()

# Create a 2D array of random probability values
probabilities = np.random.rand(grid_size, grid_size)

# Display the probabilities as a color map
# Pick color scheme by changing cmap: https://matplotlib.org/stable/users/explain/colors/colormaps.html
img = ax.imshow(probabilities, cmap='YlGn', interpolation='nearest')

# Initialize the plot with the initial positions and colors of the dots
colors = ['r', 'r']
dots = [ax.plot(*dot_position, color + 'o')[0] for dot_position, color in zip(dot_positions, colors)]

# Set the limits and aspect ratio of the plot
ax.set_xlim(0, grid_size)
ax.set_ylim(0, grid_size)
ax.set_aspect('equal')

# Initialization function for the animation
def init():
    global dot_positions
    # dot_positions = [[0, 0], [4, 2]]
    for dot, dot_position in zip(dots, dot_positions):
        dot.set_data([dot_position[0]], [dot_position[1]])
    return dots

# Generate a list of all positions for the animation for each dot
all_positions = []
for i in range(len(dot_positions)):
    positions = [dot_positions[i]]
    for instruction in instructions[i]:
        direction, steps = instruction
        for _ in range(res):
            dot_positions[i] = move_dot(dot_positions[i], direction, steps/res)
            positions.append(dot_positions[i].copy())
    all_positions.append(positions)

# Update function for the animation
def update(num):
    for i in range(len(dot_positions)):
        dot_positions[i] = all_positions[i][num]
        dots[i].set_data([dot_positions[i][0]], [dot_positions[i][1]])
    return dots

# Create the animation
ani = FuncAnimation(fig, update, init_func=init, frames=len(all_positions[0]), interval=1000/res, blit=True)

# Save the animation as a video file
ani.save('2d_demo/prob_map/map_with_dots.gif')

# Display the animation
plt.show()