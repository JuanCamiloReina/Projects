import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Walker:

    def __init__(self, number):
        """Define the amount of random walks to make"""
        self.number = number


    def one_dimension(self):
        # y(t) = y(t -1) + e
        self.y = 0
        timepoints = np.arange(self.number + 1)
        positions = [self.y]

        for i in range(self.number):
            step = np.random.randint(0 , 2)
            if step == 0:
                self.y += 1
            else:
                self.y -= 1
            positions.append(self.y)

        return positions, timepoints

    def plot_one_dimension(self):
        position, timepoint = self.one_dimension()
        plt.plot(timepoint, position, 'b-')
        plt.title('Random walk in 1 dimension')
        plt.show()

    def two_dimensions(self):
        self.x, self.y = np.zeros(self.number), np.zeros(self.number)
        for i in range(self.number):
            step = np.random.randint(0,4)
            if step == 0:
                self.x[i] = self.x[i - 1] + 1
                self.y[i] = self.y[i - 1]
            elif step == 1:
                self.x[i] = self.x[i - 1] - 1
                self.y[i] = self.y[i - 1]
            elif step == 2:
                self.x[i] = self.x[i - 1]
                self.y[i] = self.y[i - 1] + 1
            else:
                self.x[i] = self.x[i - 1]
                self.y[i] = self.y[i - 1] - 1
        return self.x, self.y

    def plot_two_dimension(self):
        data_x, data_y = self.two_dimensions()
        plt.plot(data_x, data_y)
        plt.title('Random walk in two dimensions')
        plt.show()

    def three_dimensions(self):
        self.x, self.y, self.z = np.zeros(self.number), np.zeros(self.number), np.zeros(self.number)
        for i in range(self.number):
            step = np.random.randint(0, 6)
            if step == 0:
                self.x[i] = self.x[i - 1] + 1
                self.y[i] = self.y[i - 1]
                self.z[i] = self.z[i - 1]
            elif step == 1:
                self.x[i] = self.x[i - 1] - 1
                self.y[i] = self.y[i - 1]
                self.z[i] = self.z[i - 1]
            elif step == 2:
                self.x[i] = self.x[i - 1]
                self.y[i] = self.y[i - 1] + 1
                self.z[i] = self.z[i - 1]
            elif step == 3:
                self.x[i] = self.x[i - 1]
                self.y[i] = self.y[i - 1] - 1
                self.z[i] = self.z[i - 1]
            elif step == 4:
                self.x[i] = self.x[i - 1]
                self.y[i] = self.y[i - 1]
                self.z[i] = self.z[i - 1] + 1
            else:
                self.x[i] = self.x[i - 1]
                self.y[i] = self.y[i - 1]
                self.z[i] = self.z[i - 1] - 1
        return self.x, self.y, self.z

    def plot_three_dimensions(self):
        x_data, y_data, z_data = self.three_dimensions()
        ax = plt.subplot(1, 1, 1, projection='3d')
        ax.plot(x_data, y_data,z_data, alpha=0.9)
        ax.scatter(x_data[-1],y_data[-1],z_data[-1])

        plt.show()

walker = Walker(1000)
#walker.plot_one_dimension()
#walker.plot_two_dimension()
walker.plot_three_dimensions()
