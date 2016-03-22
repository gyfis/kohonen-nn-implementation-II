import lateral_inhibitions
from itertools import product


def visualize(kohonen, points, lines_col):
    if kohonen.lateral_inhibition == lateral_inhibitions.gauss_limited:
        return visualize_square(kohonen, points, lines_col)
    if kohonen.lateral_inhibition == lateral_inhibitions.gauss_hex:
        return visualize_hex(kohonen, points, lines_col)


def visualize_square(kohonen, points, lines_col):
    points.set_data(list(zip(*[kohonen.neurons[neuron_id] for neuron_id in kohonen.neuron_id_iterator()])))

    lines_data = []
    dims = kohonen.dims()

    for row, (i, j) in product(range(dims[0]), zip(range(dims[1]), range(dims[1])[1:])):
        lines_data.append((kohonen.neurons[row, i], kohonen.neurons[row, j]))
    for column, (i, j) in product(range(dims[1]), zip(range(dims[0]), range(dims[0])[1:])):
        lines_data.append((kohonen.neurons[i, column], kohonen.neurons[j, column]))

    lines_col.set_segments(lines_data)


def neighbors(l):
    return zip(range(l), range(l)[1:])


def visualize3d(kohonen):
    points = [kohonen.neurons[neuron_id] for neuron_id in kohonen.neuron_id_iterator()]

    dims = kohonen.dims()

    lines = []

    for layer, row, (i, j) in product(range(dims[0]), range(dims[1]), neighbors(dims[2])):
        lines.append((kohonen.neurons[layer, row, i], kohonen.neurons[layer, row, j]))

    for row, column, (i, j) in product(range(dims[1]), range(dims[2]), neighbors(dims[0])):
        lines.append((kohonen.neurons[i, row, column], kohonen.neurons[j, row, column]))

    for column, layer, (i, j) in product(range(dims[2]), range(dims[0]), neighbors(dims[1])):
        lines.append((kohonen.neurons[layer, i, column], kohonen.neurons[layer, j, column]))

    return points, lines


def visualize_hex(kohonen, points, lines_col):
    points.set_data(list(zip(*[kohonen.neurons[neuron_id] for neuron_id in kohonen.neuron_id_iterator()])))
    lines_data = []

    dims = kohonen.dims()

    # Sideways
    for row, (i, j) in product(range(dims[0]), zip(range(dims[1]), range(dims[1])[1:])):
        lines_data.append((kohonen.neurons[row, i], kohonen.neurons[row, j]))

    # Downwards
    # Recommended to not mess with this
    # Every neuron is connected to neuron with offset (0, +1)
    for i, j in zip(range(dims[0]), range(dims[0])[1:]):
        for column in range(dims[1]):
            lines_data.append((kohonen.neurons[i, column], kohonen.neurons[j, column]))
    # # Even neurons are connected to neuron with offset (-1, +1)
    for i, j in list(zip(range(dims[0]), range(dims[1])[1:]))[::2]:
        for col1, col2 in zip(range(dims[1])[1:], range(dims[1])):
            lines_data.append((kohonen.neurons[i, col1], kohonen.neurons[j, col2]))
    # # Odd neurons are connected to neuron with offset (+1, +1)
    for i, j in list(zip(range(dims[0]), range(dims[1])[1:]))[1::2]:
        for col1, col2 in zip(range(dims[1]), range(dims[1])[1:]):
            lines_data.append((kohonen.neurons[i, col1], kohonen.neurons[j, col2]))

    lines_col.set_segments(lines_data)
