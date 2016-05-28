from kohonen import Kohonen, Layout
from master_loop import run_3d
from stepper import default_step
import updater
import matplotlib.image as mpimg


if __name__ == "__main__":
    im = mpimg.imread('images/Raudholar_medium.png')

    k = Kohonen(dims=(4, 2, 1), layout=Layout.square, init_type=True, use_alt_update=False, init_range=(0.0, 1.0))

    alpha_init = 1
    diameter_init = 4

    run_3d(k, alpha_stepper=default_step(init_val=alpha_init, step_every=100, p=-0.5),
           diameter_stepper=default_step(init_val=diameter_init, step_every=50, p=-0.5),
           xlim=(0, 1), ylim=(0, 1), zlim=(0, 1),
           update_func=updater.image3ddistributed(im), steps=3000, vis_steps=50, image_steps=1,
           pix=im)
