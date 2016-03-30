from kohonen import Kohonen, Layout
from master_loop import run_swap
from stepper import default_step
import updater
import matplotlib.image as mpimg


if __name__ == "__main__":
    im1 = mpimg.imread('images/white_tiger.png')
    im2 = mpimg.imread('images/hsvrgb.png')

    k1 = Kohonen(dims=(8, 4, 4), layout=Layout.square, init_type=None)
    k2 = Kohonen(dims=(8, 4, 4), layout=Layout.square, init_type=None)

    alpha_init = 1
    diameter_init = k1.dims()[0] * 0.9

    run_swap(k1, k2, alpha_stepper=default_step(init_val=alpha_init, step_every=100, p=-0.9),
           diameter_stepper=default_step(init_val=diameter_init, step_every=50, p=-0.5),
           xlim=(0, 1), ylim=(0, 1), zlim=(0, 1),
           update_func1=updater.image3dscaled(im1), update_func2=updater.image3dscaled(im2),
             steps=1000, vis_steps=5, image_steps=1,
           pix1=im1, pix2=im2)

