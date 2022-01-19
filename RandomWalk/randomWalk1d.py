import numpy as np
import matplotlib.pyplot as plt
import random

def randomWalk1D(number):
    x, y = 0, 0

    timepoints = np.arange(number + 1)
    positions = [y]

    for i in range(1, number + 1):
        step = random.choice([0,1])

        if step == 0:
            y += 1
        else:
            y -= 1

        positions.append(y)
    return timepoints, positions

time_data, pos_data = randomWalk1D(1000)
plt.plot(time_data, pos_data, 'r-')
plt.title('1D random walk in python')
plt.show()
