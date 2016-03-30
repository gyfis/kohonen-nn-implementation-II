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
    def __init__(self, dims=(15, 15), layout=Layout.square, init_type=None, init_range=(0.4, 0.6),
                 use_alt_update=False, fixed_neuron_number=0, fixed_neuron_pos=None):
        size = dims + (len(dims), )
        self.neurons = np.random.uniform(init_range[0], init_range[1], size) if init_type else np.zeros(size)

        for i in range(fixed_neuron_number):
            self.neurons[(i, 0, 0)] = np.array(fixed_neuron_pos[i]) / 255.0

        self.lateral_inhibition = {
            Layout.square: lateral_inhibitions.gauss,
            Layout.hex: lateral_inhibitions.gauss_hex
        }[layout]
        self.use_alt_update = use_alt_update
        self.fixed_neuron_number = fixed_neuron_number

    def neuron_id_iterator(self):
        return product(*map(range, self.neurons.shape[:-1]))

    def dims(self):
        return self.neurons.shape

    def get_sorted_neuron_ids(self, weights):
        return sorted(list(self.neuron_id_iterator()), key=lambda n_id: dist(weights, self.neurons[n_id]))

    def update(self, weights, diameter=1, alpha=0.05):
        if self.use_alt_update:
            self.update_alt(weights, diameter, alpha)
            return

        min_neuron_id = min((neuron_id for neuron_id in self.neuron_id_iterator()),
                            key=lambda x: dist(weights, self.neurons[x]))

        for neuron_id in self.neuron_id_iterator():
            neuron = self.neurons[neuron_id]
            neuron += self.lateral_inhibition(neuron_id, min_neuron_id, diameter) * (weights - neuron) * alpha

    def update_alt(self, weights, diameter=5, alpha=0.05):
        sorted_neuron_ids = self.get_sorted_neuron_ids(weights)
        for neuron_id in sorted_neuron_ids[:round(diameter)]:
            if neuron_id[0] < self.fixed_neuron_number:
                continue
            neuron = self.neurons[neuron_id]
            neuron += (weights - neuron) * alpha
