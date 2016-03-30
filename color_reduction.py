from kohonen import Kohonen, Layout
from master_loop import run_3d
from stepper import default_step
import updater
import matplotlib.image as mpimg


if __name__ == "__main__":
    im = mpimg.imread('images/autumn.png')

    k = Kohonen(dims=(16, 1, 1), layout=Layout.square, init_type=True, use_alt_update=True, init_range=(0.0, 1.0),
                fixed_neuron_number=4, fixed_neuron_pos=[(249, 219, 66), (87, 166, 35), (94, 145, 238), (233, 70, 55)])

    alpha_init = 1
    diameter_init = 16

    run_3d(k, alpha_stepper=default_step(init_val=alpha_init, step_every=100, p=-0.9),
           diameter_stepper=default_step(init_val=diameter_init, step_every=50, p=-0.9),
           xlim=(0, 1), ylim=(0, 1), zlim=(0, 1),
           update_func=updater.image3ddistributed(im), steps=1000, vis_steps=5, image_steps=1,
           pix=im)

# yellow - 229 179 66
# green - 87 116 35
# blue - 94 145 208
# red - 203 70 55