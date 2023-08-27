import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the update function for each frame of the animation
def update(frame):
    # Clear the previous plot
    plt.cla()

    # Generate new data for each solution
    x = np.linspace(0, 2 * np.pi, 100)
    y1 = np.sin(x + frame * 0.1)  # Solution 1
    y2 = np.cos(x + frame * 0.1)  # Solution 2
    y3 = np.sin(x + frame * 0.1) + np.cos(x + frame * 0.1)  # Solution 3

    # Plot each solution
    plt.plot(x, y1, label='Solution 1')
    plt.plot(x, y2, label='Solution 2')
    plt.plot(x, y3, label='Solution 3')

    # Add title and legend
    plt.title('Animated Solutions')
    plt.legend()

# Create the figure and axis
fig, ax = plt.subplots()

# Create the animation
animation = FuncAnimation(fig, update, frames=100, interval=100)

# Show the plot
plt.show()
