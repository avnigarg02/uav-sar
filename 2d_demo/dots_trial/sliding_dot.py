import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Initialize the grid, the dot's position, and resolution (how many steps per step)
grid_size = 5
dot_position = [0, 0]  # Starting at the top left corner
res = 20

# Define the instructions
instructions = [('', 0)] + [('right', 1)] * 3 + [('up', 2)] * 2 + [('left', 1)] + [('down', 1)] * 2

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

# Initialize the plot
dot, = ax.plot(*dot_position, 'o')

# Set the limits and aspect ratio of the plot
ax.set_xlim(0, grid_size)
ax.set_ylim(0, grid_size)
ax.set_aspect('equal')

# Initialization function for the animation
def init():
    global dot_position
    dot_position = [0, 0]
    dot.set_data([dot_position[0]], [dot_position[1]])
    return dot,

# Generate a list of all positions for the animation
all_positions = [dot_position]
for instruction in instructions:
    direction, steps = instruction
    for _ in range(res):
        dot_position = move_dot(dot_position, direction, steps / res)
        all_positions.append(dot_position.copy())

# Update function for the animation
def update(num):
    global dot_position
    dot_position = all_positions[num]
    dot.set_data([dot_position[0]], [dot_position[1]])
    return dot,

# Create the animation
ani = FuncAnimation(fig, update, init_func=init, frames=len(all_positions), interval=1000/res, blit=True)

# Save the animation as a video file
ani.save('2d_demo/dots_trial/sliding_dot.gif')

# Display the animation
plt.show()