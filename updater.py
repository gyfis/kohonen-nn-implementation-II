import random


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
    k.update(pix[random.randrange(0, pix.shape[0]), random.randrange(0, pix.shape[1])][:3], alpha=curr_alpha, diameter=curr_diameter)


def image3d(pix):
    return lambda k, curr_alpha, curr_diameter: image3dupdate(pix, k, curr_alpha, curr_diameter)
