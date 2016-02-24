from kohonen import Kohonen
from visualizer import visualize
import random

if __name__ == "__main__":

    k = Kohonen(dims=(10, 10))

    count = 0
    cur_alpha = 0.3

    vis_const = 500
    alpha_const = 100
    alpha_speed = 0.99
    diameter_const = 3

    while True:
        k.update((random.uniform(0.25, 0.5) * random.randrange(-1, 2, 2), random.uniform(0.25, 0.5) * random.randrange(-1, 2, 2)), alpha=cur_alpha, diameter=diameter_const * ((count+1)/500)**-0.75)
        # k.update((random.uniform(-1, 1), random.uniform(-1, 1)), alpha=cur_alpha, diameter=5)

        if count % alpha_const == 0:
            cur_alpha *= alpha_speed

        if count % vis_const == 0:
            visualize(k)

        count += 1