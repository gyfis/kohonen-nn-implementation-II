import random


def window_border(k, curr_alpha=100, curr_diameter=3):
    k.update((random.uniform(0.25, 0.5) * random.randrange(-1, 2, 2),
              random.uniform(0.25, 0.5) * random.randrange(-1, 2, 2)), alpha=curr_alpha, diameter=curr_diameter)


def uniform(k, curr_alpha=100, curr_diameter=3):
    k.update((random.uniform(-1, 1), random.uniform(-1, 1)), alpha=curr_alpha, diameter=curr_diameter)
