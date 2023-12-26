import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize the grid, the dots' position, and resolution (how many steps per step)
grid_size = 5
dot_positions = [[0, 0], [4, 2]]  # Starting positions for two dots
res = 20

# Define the instructions
instructions = [
    [('', 0)] + [('right', 1)] * 3 + [('up', 2)] * 2 + [('left', 1)] + [('down', 1)] * 2,
    [('', 0)] + [('left', 1)] * 3 + [('down', 1)] * 2 + [('right', 1)] + [('up', 2)] * 2
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

# Initialize the plot with the initial positions of the dots
dots = [ax.plot(*dot_position, 'o')[0] for dot_position in dot_positions]

# Set the limits and aspect ratio of the plot
ax.set_xlim(0, grid_size)
ax.set_ylim(0, grid_size)
ax.set_aspect('equal')

# Initialization function for the animation
def init():
    global dot_positions
    dot_positions = [[0, 0], [4, 2]]
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
ani.save('2d_demo/dots_trial/sliding_dots.gif')

# Display the animation
plt.show()