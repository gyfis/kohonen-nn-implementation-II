import matplotlib.pyplot as plt
from matplotlib import animation
from visualizer import visualize3d, visualize
from mpl_toolkits.mplot3d import axes3d, Axes3D
import updater
from matplotlib import collections as mc
import numpy as np
from scipy.spatial import cKDTree
from itertools import product


def run_3d(k, alpha_stepper, diameter_stepper,
        update_func=updater.image3d,
        steps=1000, vis_steps=50, image_steps=10,
        xlim=(-1, 1), ylim=(-1, 1), zlim=(-1, 1),
        points_style='ro', lines_style='b-',
        pix=None, pix_size=None, save_as_gif=False):

    fig = plt.figure()
    ax = fig.add_subplot(121, projection='3d')
    im = fig.add_subplot(222)
    orig_im = fig.add_subplot(224)
    orig_im.imshow(np.array(pix))

    im_data = im.imshow(pix)
    # new_im_data = np.copy(im_data)

    ax.set_xlim3d(xlim)
    ax.set_ylim3d(ylim)
    ax.set_zlim3d(zlim)

    # init points, lines
    points, lines = visualize3d(k)

    plot_points = sum([ax.plot([], [], [], 'o', markersize=10) for _ in range(len(points))], [])
    # plot_points = sum([ax.plot([], [], [], 'o') for _ in range(len(points))], [])
    plot_lines = sum([ax.plot([], [], [], 'k-', alpha=0.25) for _ in range(len(lines))], [])

    # points, = ax.plot([], [], points_style)
    # points = []
    # lines = [ax.plot([], [], [])[0] for dat in počet čar]

    # drawn = []

    # lines_collection = mc.LineCollection([])
    #
    global image_i
    image_i = -1

    def loop(i):
        print(i, image_i)
        for j in range(vis_steps):
            update_func(k, curr_alpha=alpha_stepper(i * vis_steps + j), curr_diameter=diameter_stepper(i * vis_steps + j))
        points, lines = visualize3d(k)

        for i in range(len(points)):
            plot_points[i].set_data(points[i][0], points[i][1])
            plot_points[i].set_3d_properties(points[i][2])
            plot_points[i].set_color(points[i])

        for i in range(len(lines)):
            line_data = list(zip(*lines[i]))

            plot_lines[i].set_data(line_data[0], line_data[1])
            plot_lines[i].set_3d_properties(line_data[2])

        global image_i
        image_i += 1

        if image_i % image_steps == 0:
            nppoints = np.array(points)
            kdtree = cKDTree(nppoints)

            _, new_pix_idx = kdtree.query(pix, k=1)

            im_data.set_data(nppoints[new_pix_idx])

    anim = animation.FuncAnimation(fig, loop, frames=steps // vis_steps, interval=1, repeat=False)

    if save_as_gif:
        anim.save('gifs/{}.gif'.format(save_as_gif), writer='imagemagick')

    plt.show()


def run_simple(k, alpha_stepper, diameter_stepper,
        update_func=updater.uniform,
        steps=1000, vis_steps=50,
        xlim=(-1, 1), ylim=(-1, 1),
        points_style='ro', lines_style='b-',
        save_as_gif=False):

    fig = plt.figure()
    ax = fig.add_subplot(111, xlim=xlim, ylim=ylim)

    global points, lines

    points, = ax.plot([], [], points_style)
    lines_collection = mc.LineCollection([])

    def init():
        points.set_data([], [])
        ax.add_collection(lines_collection)

    def loop(i):
        for j in range(vis_steps):
            update_func(k, curr_alpha=alpha_stepper(i * vis_steps + j), curr_diameter=diameter_stepper(i * vis_steps + j))
        visualize(k, points, lines_collection)
        print(diameter_stepper(i * vis_steps + j))
        return points, lines_collection

    anim = animation.FuncAnimation(fig, loop, init_func=init, frames=steps // vis_steps, interval=1, repeat=False)

    if save_as_gif:
        anim.save('gifs/{}.gif'.format(save_as_gif), writer='imagemagick')

    plt.show()
