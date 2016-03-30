import random
import numpy as np
from collections import defaultdict


def window_border(k, curr_alpha=100, curr_diameter=3):
    while True:
        x, y = random.uniform(0, 1), random.uniform(0, 1)
        if x > 0.333 and x < 0.666 and (y < 0.45 or y > 0.55):
            continue
        k.update((x, y), alpha=curr_alpha, diameter=curr_diameter)
        return
        # k.update((random.uniform(0, 0.33) * random.randrange(-1, 2, 2),
        #       random.uniform(0.0, 1.0 * random.randrange(-1, 2, 2)), alpha=curr_alpha, diameter=curr_diameter)


def uniform(k, curr_alpha=100, curr_diameter=3):
    k.update((random.uniform(0, 1), random.uniform(0, 1)), alpha=curr_alpha, diameter=curr_diameter)


def image3dupdate(pix, k, curr_alpha=100, curr_diameter=3):
    k.update(pix[random.randrange(0, pix.shape[0]), random.randrange(0, pix.shape[1])][:3],
             alpha=curr_alpha, diameter=curr_diameter)


def scale_color(c):
    return (c - 0.5) * 1.1 + 0.5


def image3dupdate_scaled(pix, k, curr_alpha=100, curr_diameter=3):
    k.update(scale_color(pix[random.randrange(0, pix.shape[0]), random.randrange(0, pix.shape[1])][:3]),
             alpha=curr_alpha, diameter=curr_diameter)


def image3dupdate_distributed(c, k, curr_alpha=100, curr_diameter=3):
    k.update(scale_color(c[random.randrange(len(c))][:3]),
             alpha=curr_alpha, diameter=curr_diameter)


def image3d(pix):
    return lambda k, curr_alpha, curr_diameter: image3dupdate(pix, k, curr_alpha, curr_diameter)


def image3dscaled(pix):
    return lambda k, curr_alpha, curr_diameter: image3dupdate_scaled(pix, k, curr_alpha, curr_diameter)


def image3ddistributed(pix):

    dist_const = 5.0
    dist_max = 200
    dist = defaultdict(list)

    for i in range(pix.shape[0]):
        for j in range(pix.shape[1]):
            c = pix[i, j]
            dist[tuple(map(int, np.floor(c * dist_const)))].append(c)

    for key, colors in dist.items():
        if len(colors) > dist_max:
            c = colors[:]
            random.shuffle(c)
            dist[key] = c[:dist_max]

    return lambda k, curr_alpha, curr_diameter: image3dupdate_distributed([c for l in dist.values() for c in l], k, curr_alpha, curr_diameter)


