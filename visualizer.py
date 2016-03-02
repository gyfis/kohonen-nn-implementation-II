import lateral_inhibitions
from itertools import product


def visualize(kohonen, points, lines):
    if kohonen.lateral_inhibition == lateral_inhibitions.gauss:
        return visualize_square(kohonen, points, lines)
    if kohonen.lateral_inhibition == lateral_inhibitions.gauss_hex:
        return visualize_hex(kohonen, points, lines)


def visualize_square(kohonen, points, lines):
    points.set_data(list(zip(*[kohonen.neurons[neuron_id] for neuron_id in kohonen.neuron_id_iterator()])))

    lines_data = []
    dims = kohonen.dims()

    for row, (i, j) in product(range(dims[0]), zip(range(dims[1]), range(dims[1])[1:])):
        lines_data.append(list(zip(*(kohonen.neurons[row, i], kohonen.neurons[row, j]))))
    for column, (i, j) in product(range(dims[1]), zip(range(dims[0]), range(dims[0])[1:])):
        lines_data.append(list(zip(*(kohonen.neurons[i, column], kohonen.neurons[j, column]))))

    def flatten(l):
        return list([l[0][0][0]] + list(t[1] for t in l[0])), list([l[1][0][0]] + list(t[1] for t in l[1]))

    # print(flatten(list(zip(*lines_data))))
    # lines.set_data(flatten(list(zip(*lines_data))))
    lines.set_data(list(zip(*lines_data)))


def visualize_hex(kohonen, points, lines):

    points_data = []
    lines_data = []

    dims = kohonen.dims()
    for row, (i, j) in product(range(dims[0]), zip(range(dims[1]), range(dims[1])[1:])):
        points_data.append(list(zip(*(kohonen.neurons[row, i], kohonen.neurons[row, j]))))

    # Downwards
    # Recommended to not mess with this
    # Every neuron is connected to neuron with offset (0, +1)
    for i, j in zip(range(dims[0]), range(dims[0])[1:]):
        for column in range(dims[1]):
            lines_data.append(list(zip(*(kohonen.neurons[i, column], kohonen.neurons[j, column]))))

    # Even neurons are connected to neuron with offset (-1, +1)
    for i, j in list(zip(range(dims[0]), range(dims[1])[1:]))[::2]:
        for col1, col2 in zip(range(dims[1])[1:], range(dims[1])):
            lines_data.append(list(zip(*(kohonen.neurons[i, col1], kohonen.neurons[j, col2]))))

    # Odd neurons are connected to neuron with offset (+1, +1)
    for i, j in list(zip(range(dims[0]), range(dims[1])[1:]))[1::2]:
        for col1, col2 in zip(range(dims[1]), range(dims[1])[1:]):
            lines_data.append(list(zip(*(kohonen.neurons[i, col1], kohonen.neurons[j, col2]))))

    points.set_data(list(zip(*points_data)))
    lines.set_data(list(zip(*lines_data)))
