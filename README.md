# Palette extraction and other tasks using Kohonen self-organizing maps

This is our implementation of Kohonen algorithm for palette reduction. Here are some examples of `color_reduction.py`:

```
im = mpimg.imread('images/Raudholar_medium.png')

k = Kohonen(dims=(4, 2, 1), layout=Layout.square, init_type=True, use_alt_update=False, init_range=(0.0, 1.0))

alpha_init = 1
diameter_init = 4

run_3d(k, alpha_stepper=default_step(init_val=alpha_init, step_every=100, p=-0.5),
       diameter_stepper=default_step(init_val=diameter_init, step_every=50, p=-0.5),
       xlim=(0, 1), ylim=(0, 1), zlim=(0, 1),
       update_func=updater.image3ddistributed(im), steps=3000, vis_steps=50, image_steps=1,
       pix=im)
```
![](https://www.dropbox.com/s/by6b902uppwtj6b/Raudholar_medium_4_2_1.gif?dl=1)

```
im = mpimg.imread('images/Raudholar_medium.png')

k = Kohonen(dims=(4, 4, 2), layout=Layout.square, init_type=True, use_alt_update=False, init_range=(0.0, 1.0))

alpha_init = 1
diameter_init = 4

run_3d(k, alpha_stepper=default_step(init_val=alpha_init, step_every=100, p=-0.5),
       diameter_stepper=default_step(init_val=diameter_init, step_every=50, p=-0.5),
       xlim=(0, 1), ylim=(0, 1), zlim=(0, 1),
       update_func=updater.image3ddistributed(im), steps=3000, vis_steps=50, image_steps=1,
       pix=im)
```
![](https://www.dropbox.com/s/s0s7bmcia3yzq8j/Raudholar_medium_4_4_2.gif?dl=1)
```
im = mpimg.imread('images/Virginia_medium.png')

k = Kohonen(dims=(4, 2, 1), layout=Layout.square, init_type=True, use_alt_update=False, init_range=(0.0, 1.0))

alpha_init = 1
diameter_init = 4

run_3d(k, alpha_stepper=default_step(init_val=alpha_init, step_every=100, p=-0.5),
       diameter_stepper=default_step(init_val=diameter_init, step_every=50, p=-0.5),
       xlim=(0, 1), ylim=(0, 1), zlim=(0, 1),
       update_func=updater.image3ddistributed(im), steps=3000, vis_steps=50, image_steps=1,
       pix=im)
```
![](https://www.dropbox.com/s/tk55ze88a7u2gur/Virginia_medium_4_2_1.gif?dl=1)
```
im = mpimg.imread('images/Virginia_medium.png')

k = Kohonen(dims=(4, 4, 2), layout=Layout.square, init_type=True, use_alt_update=False, init_range=(0.0, 1.0))

alpha_init = 1
diameter_init = 4

run_3d(k, alpha_stepper=default_step(init_val=alpha_init, step_every=100, p=-0.5),
       diameter_stepper=default_step(init_val=diameter_init, step_every=50, p=-0.5),
       xlim=(0, 1), ylim=(0, 1), zlim=(0, 1),
       update_func=updater.image3ddistributed(im), steps=3000, vis_steps=50, image_steps=1,
       pix=im)
```
![](https://www.dropbox.com/s/5jpgn2610ycyqq0/Virginia_medium_4_4_2.gif?dl=1)
