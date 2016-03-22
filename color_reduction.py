from kohonen import Kohonen, Layout
from master_loop import run_3d
from stepper import default_step
import updater
from PIL import Image
import matplotlib.image as mpimg


if __name__ == "__main__":
    im = mpimg.imread('images/autumn.png')

    k = Kohonen(dims=(4, 4, 8), layout=Layout.square, init_type=None)

    alpha_init = 1
    diameter_init = k.dims()[0] * 0.9

    run_3d(k, alpha_stepper=default_step(init_val=alpha_init, step_every=100, p=-0.9),
           diameter_stepper=default_step(init_val=diameter_init, step_every=50, p=-0.5),
           xlim=(0, 1), ylim=(0, 1), zlim=(0, 1),
           update_func=updater.image3d(im), steps=1000, vis_steps=5, image_steps=1,
           pix=im)

