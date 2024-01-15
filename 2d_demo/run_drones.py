import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D
import numpy as np
import os

from probability_map import randgrad_map, gradient_map, get_targets, my20x20map
from algorithms import sample, basic_algo, my20x20path

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ INITIALIZATION  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# setup
grid_size = 19
res = 2  # how smooth should animation be (higher = smoother, split each unit into this many)
speed = 100  # milliseconds per unit traveled
delay = 50  # how long to wait until animation restarts

probabilities = my20x20map()
target_positions = get_targets(probabilities, 10, seed=0)
directory = os.path.dirname(os.path.abspath(__file__)) + '/visuals' # location to save to
save = True

# Note: color options can be found: https://matplotlib.org/stable/gallery/color/named_colors.html

# TRIAL
# drones_init = [([0, 0], 'r'), ([100, 100], 'r')]
# drones_init = [([1000, 1000], 'r')]
# all_positions = sample(drones_init, res)
# save_to = 'animation'

# BASIC
# drones_init = [([0, 0], 'red'), ([5, 19], 'mediumorchid'), ([10, 0], 'darkorange'), ([15, 19], 'mediumvioletred')]
# all_positions = basic_algo(grid_size, drones_init, res)
# save_to = 'basic20x20'

# ACTUAL
drones_init = [([0, 0], 'red'), ([19, 14], 'mediumorchid'), ([19, 7], 'darkorange'), ([0, 19], 'mediumvioletred')]
all_positions = my20x20path(drones_init, res)
save_to = 'final20x20'


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   CREATE PLOT   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
fig, ax = plt.subplots()
# Note: change color scheme using cmap: https://matplotlib.org/stable/users/explain/colors/colormaps.html
ax.imshow(probabilities, cmap='YlGn', interpolation='nearest')

# Set the limits, aspect ratio, and grid lines of the plot
ax.set_xlim(-0.5, grid_size + 0.5)
ax.set_ylim(-0.5, grid_size + 0.5)
ax.set_aspect('equal')
ax.set_xticks(np.arange(-0.5, grid_size, 1))
ax.set_yticks(np.arange(-0.5, grid_size, 1))
ax.xaxis.set_tick_params(labelsize=0)
ax.yaxis.set_tick_params(labelsize=0)
ax.grid(True, which='both', color='dimgray', linewidth=1)

# Save the blank probability map
if save: plt.savefig(os.path.join(directory, 'prob_map_no_targets.png'))

# Create targets and save
targets = [ax.plot(*target_pos, 'o', color='dodgerblue')[0] for target_pos in target_positions]
if save: plt.savefig(os.path.join(directory, 'prob_map_with_targets.png'))

# Add the drones
start_locations = [ax.plot(*drone_pos, '*', color=c, markersize=10)[0] for drone_pos, c in drones_init]
drones = [ax.plot(*drone_pos, 'o', color=c)[0] for drone_pos, c in drones_init]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ANIMATION    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Get initial drone positions and initlize times list
drone_positions = [drone_pos for drone_pos, _ in drones_init]
target_hit_times = []

# Initialization function for the animation
def init():
    global drone_positions
    for drone, drone_position in zip(drones, drone_positions):
        drone.set_data([drone_position[0]], [drone_position[1]])
    return drones

# Create a Line2D object for each drone to trace its path
drone_paths = [Line2D([], [], color=color) for _, color in drones_init]
for drone_path in drone_paths:
    ax.add_line(drone_path)

# Update function for the animation
def update(num):
    global target_positions

    if num < len(all_positions[0]):
        for i in range(len(drone_positions)):
            drone_positions[i] = all_positions[i][num]
            drones[i].set_data([drone_positions[i][0]], [drone_positions[i][1]])

            # Check if the drone's current position matches any of the target positions
            matches = np.where(np.all(np.array(drone_positions[i]) == target_positions, axis=1))[0]
            target_hit_times.extend([num // res + 1] * matches.size)
            target_positions = np.delete(target_positions, matches, axis=0)

            # Update the drone path
            drone_paths[i].set_data(*zip(*all_positions[i][:num+1]))
        
    return drones + drone_paths


# Create the animation
ani = FuncAnimation(fig, update, init_func=init, frames=len(all_positions[0]) + delay, interval=speed/res, blit=True)

# Save the animation
if save: 
    ani.save(os.path.join(directory, save_to + '.gif'))
    plt.savefig(os.path.join(directory, save_to + '.png'))
else:
    ani.save(os.path.join(directory, 'temp.gif'))

# Print target hit times
print(target_hit_times)

# Display the animation
plt.show()
