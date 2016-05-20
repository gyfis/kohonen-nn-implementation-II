from kohonen import Kohonen, Layout
from master_loop import run_3d
from stepper import default_step
import updater
import matplotlib.image as mpimg


if __name__ == "__main__":
    im = mpimg.imread('images/autumn.png')

    # k = Kohonen(dims=(16, 1, 1), layout=Layout.square, init_type=True, use_alt_update=True, init_range=(0.0, 1.0),
    #             fixed_neuron_number=4, fixed_neuron_pos=[(249, 219, 66), (87, 166, 35), (94, 145, 238), (233, 70, 55)])

    k = Kohonen(dims=(4, 4, 2), layout=Layout.square, init_type=True, use_alt_update=True, init_range=(0.0, 1.0))

    alpha_init = 1
    diameter_init = 4

    run_3d(k, alpha_stepper=default_step(init_val=alpha_init, step_every=400, p=-0.5),
           diameter_stepper=default_step(init_val=diameter_init, step_every=200, p=-0.5),
           xlim=(0, 1), ylim=(0, 1), zlim=(0, 1),
           update_func=updater.image3ddistributed(im), steps=1000000, vis_steps=50, image_steps=1,
           pix=im)

# yellow - 229 179 66
# green - 87 116 35
# blue - 94 145 208
# red - 203 70 55


# palette = [[0.95778394100655839, 0.51887502876111136, 0.0023532581760844964], [0.7439204327164779, 1.00275303875708, 1.0306757029804325], [-0.017144334775310681, 0.51187519854987484, 0.86955482581427512], [0.26704245043412655, 0.99097890385211285, 1.0476657496718478], [0.073862210366775538, 0.2225654349130694, 0.16258002054694526], [0.96502266888130483, 0.73714591451626654, 0.44163585978351705], [0.50527200244184978, 0.65941021326315996, 0.64086657808619707], [0.52516475568030796, 0.32270377934709271, 0.041850012353518179]]
