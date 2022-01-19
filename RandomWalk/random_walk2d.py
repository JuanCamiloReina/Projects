import random
import numpy as np
import matplotlib.pyplot as plt

def random_walk_2d(n):
    x = np.zeros(n)
    y = np.zeros(n)

    for i in range(n):
        step = random.choice(['UP', 'DOWN', 'RIGHT', 'LEFT'])
        if step == 'UP':
            x[i] = x[i - 1] + 1
            y[i] = y[i - 1]
        elif step == 'DOWN':
            x[i] = x[i - 1] - 1
            y[i] = y[i - 1]
        elif step == 'RIGHT':
            x[i] = x[i - 1]
            y[i] = y[i - 1] + 1
        else:
            x[i] = x[i - 1]
            y[i] = y[i - 1] - 1
    return x, y
x_data, y_data = random_walk_2d(10000)

plt.title('2D random walk')
plt.plot(x_data, y_data)
plt.show()
