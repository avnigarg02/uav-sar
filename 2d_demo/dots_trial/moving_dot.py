import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize the grid and the dot's position
grid_size = 5
dot_position = [0, 0]  # Starting at the top left corner

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

# Update function for the animation
def update(num):
    direction, steps = instructions[num]
    global dot_position
    dot_position = move_dot(dot_position, direction, steps)
    dot.set_data([dot_position[0]], [dot_position[1]])
    return dot,

# Create the animation
ani = FuncAnimation(fig, update, init_func=init, frames=len(instructions), interval=1000, blit=True)

# Save the animation as a video file
ani.save('2d_demo/moving_dot.gif')

# Display the animation
plt.show()
# Uncomment the following two and comment the above line if using Jupyter to run code
# from IPython.display import HTML
# HTML(ani.to_jshtml())