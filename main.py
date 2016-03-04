from kohonen import Kohonen, Layout
from master_loop import run
from stepper import default_step
import updater


if __name__ == "__main__":

    k = Kohonen(dims=(300, 1), layout=Layout.square, init_type=None)

    alpha_init = 1
    diameter_init = k.dims()[0] * 0.9

    run(k, alpha_stepper=default_step(init_val=alpha_init, step_every=50, p=-0.3),
        diameter_stepper=default_step(init_val=diameter_init, step_every=50, p=-1.2),
        xlim=(0, 1), ylim=(0, 1),
        update_func=updater.window_border, steps=50000, vis_steps=20, save_as_gif=None)
