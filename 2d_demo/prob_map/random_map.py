import numpy as np
import matplotlib.pyplot as plt

# Create a 2D array of random probability values
probabilities = np.random.rand(100, 100)

# Create a color scale plot
# Pick color scheme by changing cmap: https://matplotlib.org/stable/users/explain/colors/colormaps.html
plt.imshow(probabilities, cmap='YlGn', interpolation='nearest')

# Show the color bar
plt.colorbar()

# Save the image before displaying it
plt.savefig('2d_demo/prob_map/random.png', dpi=300, bbox_inches='tight')

# Display the plot
plt.show()