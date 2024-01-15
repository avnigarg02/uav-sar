import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   RAW  DATA   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
basic_times = [
    [22, 53, 58, 71, 73, 87, 88, 90, 93, 95],
    [1, 6, 35, 38, 50, 67, 68, 95, 97, 99],
    [16, 21, 26, 68, 73, 73, 73, 77, 90, 95],
    [13, 23, 55, 55, 61, 63, 70, 84, 90, 98],
    [1, 40, 45, 47, 57, 60, 73, 90, 95, 99]
]

actual_time = [
    [7, 7, 15, 18, 18, 23, 39, 56, 67, 88],
    [1, 12, 13, 22, 25, 26, 27, 38, 38, 43],
    [13, 18, 21, 22, 26, 32, 35, 49, 55, 55],
    [8, 9, 13, 18, 24, 33, 34, 46, 57, 91],
    [2, 6, 17, 18, 18, 55, 58, 67, 99, 102]
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  MAKE  TABLE  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Convert basic_times and actual_time to numpy arrays
basic_times_np = np.array(basic_times)
actual_time_np = np.array(actual_time)

# Calculate the averages of basic_times and actual_time
basic_times_avg = np.mean(basic_times_np, axis=0)
actual_time_avg = np.mean(actual_time_np, axis=0)

# Create a DataFrame for basic_times and actual_time
df = pd.DataFrame(np.concatenate((basic_times_np, actual_time_np), axis=0), 
                  columns=[f'Target {i+1}' for i in range(basic_times_np.shape[1])])

# Add the averages to the DataFrame
df.loc['Basic Brute Force'] = basic_times_avg
df.loc['Our Algorithm'] = actual_time_avg

# Display the DataFrame
print(df)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MAKE GRAPHS  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create a list of targets found
targets_found = list(range(1, len(basic_times_avg) + 1))

# Create the plot
plt.plot(basic_times_avg, targets_found, marker='o', label='Basic Brute Force')
plt.plot(actual_time_avg, targets_found, marker='o', label='Our Algorithm')

# Set the labels and legend
plt.ylabel('Targets Found')
plt.xlabel('Time')
plt.legend()

# Save
directory = os.path.dirname(os.path.abspath(__file__)) + '/visuals' # location to save to
plt.savefig(os.path.join(directory, 'graph.png'))

# Show the plot
plt.show()

