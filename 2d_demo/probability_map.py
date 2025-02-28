import numpy as np


def random_map(grid_size):
    return np.random.rand(grid_size, grid_size)


def gradient_map(grid_size):
    # Generate random values from 0 to 1
    map_array = np.empty((grid_size, grid_size))
    
    # Assign higher values to higher rows
    for i in range(grid_size):
        map_array[i] = (i) / grid_size
    
    return map_array


def randgrad_map(grid_size):
    # Generate random values from 0 to 1
    map_array = np.random.rand(grid_size, grid_size)
    
    # Assign higher values to higher rows
    for i in range(grid_size):
        map_array[i] *= (i + 1)
    
    return map_array


def my20x20map():
    return np.flip(np.array([
        [.1, .1, .2, .2, .2, .2, .4, .6, .6, .6, .4, .2, .1, .1, .1, .1, .1, .1, .1, .1],
        [.2, .2, .4, .4, .4, .4, .2, .4, .6, .6, .6, .4, .2, .2, .2, .1, .1, .1, .1, .1],
        [.2, .4, .6, .6, .6, .6, .4, .4, .6, .6, .6, .4, .4, .4, .4, .2, .1, .1, .1, .1],
        [.2, .4, .6, .6, .6, .6, .6, .4, .4, .6, .6, .6, .6, .6, .6, .4, .2, .2, .2, .2],
        [.1, .2, .4, .6, .6, .6, .6, .6, .4, .6, .6, .6, .6, .6, .6, .6, .4, .4, .4, .4],
        [.1, .1, .2, .4, .6, .6, .6, .6, .4, .4, .4, .4, .4, .4, .6, .6, .6, .6, .6, .6],
        [.1, .1, .2, .4, .6, .6, .6, .4, .6, .6, .4, .2, .2, .4, .6, .6, .6, .6, .6, .6],
        [.1, .1, .1, .2, .4, .4, .4, .6, .8, .8, .6, .4, .2, .2, .4, .4, .4, .4, .4, .4],
        [.1, .1, .1, .1, .2, .2, .4, .6, .8, .8, .6, .4, .2, .1, .2, .2, .2, .2, .2, .2],
        [.1, .1, .1, .1, .1, .2, .4, .6, .8, .8, .6, .4, .2, .1, .1, .1, .1, .1, .1, .1],
        [.1, .1, .1, .1, .1, .2, .4, .6, .8, .8, .6, .4, .2, .1, .1, .1, .1, .2, .2, .2],
        [.1, .1, .1, .1, .1, .2, .4, .6, .8, .8, .6, .4, .2, .2, .2, .2, .2, .4, .4, .4],
        [.1, .1, .1, .1, .1, .2, .4, .6, .8, .8, .6, .4, .2, .4, .4, .4, .4, .6, .6, .6],
        [.1, .1, .1, .1, .1, .2, .4, .6, .8, .8, .6, .4, .4, .6, .6, .6, .6, .8, .8, .8],
        [.1, .1, .1, .1, .1, .2, .4, .6, .8, .8, .6, .6, .6, .8, .8, .8, .8, .8, .6, .6],
        [.1, .1, .1, .2, .2, .4, .4, .6, .8, .8, .6, .8, .8, .8, .6, .6, .6, .6, .4, .4],
        [.1, .1, .2, .4, .4, .6, .6, .8, .8, .8, .8, .6, .6, .6, .4, .4, .4, .4, .2, .2],
        [.1, .2, .4, .6, .6, .8, .8, .8, .8, .8, .6, .4, .4, .4, .2, .2, .2, .2, .1, .1],
        [.2, .4, .6, .8, .8, .8, .6, .6, .8, .8, .6, .4, .2, .2, .1, .1, .1, .1, .1, .1],
        [.4, .6, .8, .8, .6, .6, .4, .6, .8, .8, .6, .4, .2, .1, .1, .1, .1, .1, .1, .1],
    ]), axis=0)


def get_targets(probabilities, num, seed=-1):
    # Set the seed value if provided
    if seed != -1:
        np.random.seed(seed)

    # Flatten the probabilities and normalize them to sum to 1
    weights = probabilities.flatten()
    weights /= weights.sum()

    # Choose indices from the flattened array using the probabilities as weights
    grid_size = len(probabilities)
    indices = np.random.choice(np.arange(grid_size*grid_size), size=num, p=weights)

    # Convert the chosen indices back to 2D coordinates and return
    row_indices, col_indices = np.unravel_index(indices, probabilities.shape)
    return np.column_stack((col_indices, row_indices))

