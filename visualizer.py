import matplotlib.pyplot as plt


def visualize(kohonen):

    for neuron_id in kohonen.neuron_id_iterator():
        plt.plot(*kohonen.neurons[neuron_id], 'ro')

    dims = kohonen.dims()
    for row in range(dims[0]):
        for i, j in zip(range(dims[1]), range(dims[1])[1:]):
            plt.plot(tuple(map(lambda x: x[0], (kohonen.neurons[row, i], kohonen.neurons[row, j]))),
                     tuple(map(lambda x: x[1], (kohonen.neurons[row, i], kohonen.neurons[row, j]))),
                     'b-')

    for column in range(dims[1]):
        for i, j in zip(range(dims[0]), range(dims[0])[1:]):
            plt.plot(tuple(map(lambda x: x[0], (kohonen.neurons[i, column], kohonen.neurons[j, column]))),
                     tuple(map(lambda x: x[1], (kohonen.neurons[i, column], kohonen.neurons[j, column]))),
                     'b-')

    plt.show()