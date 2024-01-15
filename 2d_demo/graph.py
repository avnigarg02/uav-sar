import matplotlib.pyplot as plt
import os

basic_times = [22, 53, 58, 71, 73, 87, 88, 90, 93, 95]
actual_time = [7, 7, 15, 18, 18, 23, 39, 56, 67, 88]

# Create a list of targets found
targets_found = list(range(1, len(basic_times) + 1))

# Create the plot
plt.plot(basic_times, targets_found, marker='o', label='Basic Times')
plt.plot(actual_time, targets_found, marker='o', label='Actual Time')

# Set the labels and legend
plt.ylabel('Targets Found')
plt.xlabel('Time')
plt.legend()

# Save
directory = os.path.dirname(os.path.abspath(__file__)) + '/visuals' # location to save to
plt.savefig(os.path.join(directory, 'graph.png'))

# Show the plot
plt.show()

