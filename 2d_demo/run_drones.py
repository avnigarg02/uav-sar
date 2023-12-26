import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os

from probability_map import make_map, get_targets
from algorithms import basic_algo

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ INITIALIZATION  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
grid_size = 99
drones_init = [([10, 10], 'r'), ([90, 90], 'r')]
res = 20  # how smooth should animation be
probabilities = make_map(grid_size)
target_positions = get_targets(probabilities, 10)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   CREATE PLOT   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
fig, ax = plt.subplots()
# Note: change color scheme using cmap: https://matplotlib.org/stable/users/explain/colors/colormaps.html
ax.imshow(probabilities, cmap='YlGn', interpolation='nearest')
drones = [ax.plot(*drone_pos, color + 'o')[0] for drone_pos, color in drones_init]
targets = [ax.plot(*target_pos, 'bo')[0] for target_pos in target_positions]

# Set the limits and aspect ratio of the plot
ax.set_xlim(0, grid_size)
ax.set_ylim(0, grid_size)
ax.set_aspect('equal')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ANIMATION    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Define the instructions
instructions = [
    [('', 0)] + [('right', 20)] * 3 + [('up', 20)] * 4 + [('left', 20)] + [('down', 20)] * 2,
    [('', 0)] + [('left', 20)] * 3 + [('down', 20)] * 4 + [('right', 20)] + [('up', 20)] * 2
]

# Function to move the drones
def move_drone(drone_pos, direction, steps):
    new_pos = drone_pos.copy()
    if direction.lower().startswith('u'):
        new_pos[1] += steps
    elif direction.lower().startswith('d'):
        new_pos[1] -= steps
    elif direction.lower().startswith('l'):
        new_pos[0] -= steps
    elif direction.lower().startswith('r'):
        new_pos[0] += steps
    return new_pos

# Generate a list of all positions for the animation for each drone
drone_positions = [drone_pos for drone_pos, _ in drones_init]
all_positions = []
for i in range(len(drone_positions)):
    positions = [drone_positions[i]]
    for instruction in instructions[i]:
        direction, steps = instruction
        for _ in range(res):
            drone_positions[i] = move_drone(drone_positions[i], direction, steps/res)
            positions.append(drone_positions[i].copy())
    all_positions.append(positions)


# Initialization function for the animation
def init():
    global drone_positions
    for drone, drone_position in zip(drones, drone_positions):
        drone.set_data([drone_position[0]], [drone_position[1]])
    return drones


# Update function for the animation
def update(num):
    for i in range(len(drone_positions)):
        drone_positions[i] = all_positions[i][num]
        drones[i].set_data([drone_positions[i][0]], [drone_positions[i][1]])
    return drones


# Create the animation
ani = FuncAnimation(fig, update, init_func=init, frames=len(all_positions[0]), interval=1000/res, blit=True)

# Save the animation
directory = os.path.dirname(os.path.abspath(__file__))
ani.save(os.path.join(directory, 'animation.gif'))

# Display the animation
plt.show()
