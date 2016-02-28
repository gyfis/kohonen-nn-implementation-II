from kohonen import Kohonen
from master_loop import run
import updater

if __name__ == "__main__":

    k = Kohonen(dims=(6, 6), layout="hex")

    count = 0
    cur_alpha = 0.3

    alpha_init = 0.3
    alpha_const = 100
    alpha_speed = 0.97

    diameter_init = 1.5
    diameter_const = 50
    diameter_speed = 0.999

    run(k, update_func=updater.uniform, steps=5000, vis_steps=50,
        alpha_init=alpha_init, alpha_const=alpha_const, alpha_speed=alpha_speed,
        diameter_init=diameter_init, diameter_const=diameter_const, diameter_speed=diameter_speed,
        save_as_gif=None)
