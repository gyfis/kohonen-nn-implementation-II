import numpy as np
from itertools import product
from operator import sub
import lateral_inhibitions
from enum import Enum


class Layout(Enum):
    square = 1,
    hex = 2


def dist(neuron1, neuron2):
    return sum(abs(neuron1 - neuron2))


def id_dist(id1, id2):
    return sum(map(abs, map(sub, id1, id2)))


class Kohonen(object):
    def __init__(self, dims=(15, 15), layout=Layout.square, init_type=None, init_range=(0.4, 0.6)):
        size = dims + (len(dims), )
        self.neurons = np.random.uniform(init_range[0], init_range[1], size) if init_type else np.zeros(size)
        self.lateral_inhibition = {
            Layout.square: lateral_inhibitions.gauss,
            Layout.hex: lateral_inhibitions.gauss_hex
        }[layout]

    def neuron_id_iterator(self):
        return product(*map(range, self.neurons.shape[:-1]))

    def dims(self):
        return self.neurons.shape

    def update(self, weights, diameter=1, alpha=0.05):
        min_neuron_id = min((neuron_id for neuron_id in self.neuron_id_iterator()),
                            key=lambda x: dist(weights, self.neurons[x]))

        for neuron_id in self.neuron_id_iterator():
            neuron = self.neurons[neuron_id]
            neuron += self.lateral_inhibition(neuron_id, min_neuron_id, diameter) * (weights - neuron) * alpha
