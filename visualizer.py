import matplotlib.pyplot as plt
import numpy as np

points, = plt.plot([], [], 'ro')
lines, = plt.plot([], [], 'b-')
plt.ion()


def clear():
    points.set_xdata([])
    points.set_ydata([])
    lines.set_xdata([])
    lines.set_ydata([])


def visualize(kohonen):
    # clear()

    for neuron_id in kohonen.neuron_id_iterator():
        points.set_xdata(np.append(points.get_xdata(), kohonen.neurons[neuron_id][0]))
        points.set_xdata(np.append(points.get_ydata(), kohonen.neurons[neuron_id][1]))

    dims = kohonen.dims()
    for row in range(dims[0]):
        for i, j in zip(range(dims[1]), range(dims[1])[1:]):
            lines.set_xdata(np.append(lines.get_xdata(), tuple(map(lambda x: x[0], (kohonen.neurons[row, i], kohonen.neurons[row, j])))))
            lines.set_ydata(np.append(lines.get_ydata(), tuple(map(lambda x: x[1], (kohonen.neurons[row, i], kohonen.neurons[row, j])))))

    for column in range(dims[1]):
        for i, j in zip(range(dims[0]), range(dims[0])[1:]):
            lines.set_xdata(np.append(lines.get_xdata(), tuple(map(lambda x: x[0], (kohonen.neurons[i, column], kohonen.neurons[j, column])))))
            lines.set_ydata(np.append(lines.get_ydata(), tuple(map(lambda x: x[1], (kohonen.neurons[i, column], kohonen.neurons[j, column])))))

    plt.show()
    plt.pause(1)
