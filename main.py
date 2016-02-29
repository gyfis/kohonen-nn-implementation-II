from kohonen import Kohonen, Layout
from master_loop import run
import updater


if __name__ == "__main__":

    k = Kohonen(dims=(5, 5), layout=Layout.square, init_type=None)

    count = 0
    cur_alpha = 0.3

    alpha_init = 0.3
    alpha_const = 100
    alpha_speed = 0.98

    diameter_init = 1.5
    diameter_const = 50
    diameter_speed = 0.98

    run(k, update_func=updater.uniform, steps=20000, vis_steps=20,
        alpha_init=alpha_init, alpha_const=alpha_const, alpha_speed=alpha_speed,
        diameter_init=diameter_init, diameter_const=diameter_const, diameter_speed=diameter_speed,
        save_as_gif=None)
