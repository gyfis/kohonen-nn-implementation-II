import matplotlib.pyplot as plt
import lateral_inhibitions
from itertools import product


def visualize(kohonen):
    if kohonen.lateral_inhibition == lateral_inhibitions.gauss:
        visualize_square(kohonen)
    if kohonen.lateral_inhibition == lateral_inhibitions.gauss_hex:
        visualize_hex(kohonen)


def visualize_square(kohonen):
    for neuron_id in kohonen.neuron_id_iterator():
        plt.plot(*kohonen.neurons[neuron_id], 'ro')

    dims = kohonen.dims()
    for row, (i, j) in product(range(dims[0]), zip(range(dims[1]), range(dims[1])[1:])):
        plt.plot(*(lambda a, b: ((a[0], b[0]), (a[1], b[1])))(kohonen.neurons[row, i],kohonen.neurons[row, j]), 'b-')

    for column, (i, j) in product(range(dims[1]), zip(range(dims[0]), range(dims[0])[1:])):
        plt.plot(*(lambda a, b: ((a[0], b[0]), (a[1], b[1])))(kohonen.neurons[i, column],kohonen.neurons[j, column]), 'b-')

    plt.show()


def visualize_hex(kohonen):
    for neuron_id in kohonen.neuron_id_iterator():
        plt.plot(*kohonen.neurons[neuron_id], 'ro')

    dims = kohonen.dims()
    for row, (i, j) in product(range(dims[0]), zip(range(dims[1]), range(dims[1])[1:])):
        plt.plot(*(lambda a, b: ((a[0], b[0]), (a[1], b[1])))(kohonen.neurons[row, i], kohonen.neurons[row, j]), 'b-')

    # Downwards
    # Recommended to not mess with this
    # Every neuron is connected to neuron with offset (0, +1)
    for i, j in zip(range(dims[0]), range(dims[0])[1:]):
        for column in range(dims[1]):
            plt.plot(*(lambda a, b: ((a[0], b[0]), (a[1], b[1])))(kohonen.neurons[i, column],kohonen.neurons[j, column]), 'b-')

    # Even neurons are connected to neuron with offset (-1, +1)
    for i, j in list(zip(range(dims[0]), range(dims[1])[1:]))[::2]:
        for col1, col2 in zip(range(dims[1])[1:], range(dims[1])):
            plt.plot(*(lambda a, b: ((a[0], b[0]), (a[1], b[1])))(kohonen.neurons[i, col1],kohonen.neurons[j, col2]), 'b-')

    # Odd neurons are connected to neuron with offset (+1, +1)
    for i, j in list(zip(range(dims[0]), range(dims[1])[1:]))[1::2]:
        for col1, col2 in zip(range(dims[1]), range(dims[1])[1:]):
            plt.plot(*(lambda a, b: ((a[0], b[0]), (a[1], b[1])))(kohonen.neurons[i, col1],kohonen.neurons[j, col2]), 'b-')

    plt.show()