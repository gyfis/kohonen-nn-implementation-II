import matplotlib.pyplot as plt
from matplotlib import animation
from visualizer import visualize3d, visualize
import updater
from matplotlib import collections as mc
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.spatial import cKDTree


def run_swap(k1, k2, alpha_stepper, diameter_stepper,
        update_func1=updater.image3d, update_func2=updater.image3d,
        steps=1000, vis_steps=50, image_steps=10,
        xlim=(-1, 1), ylim=(-1, 1), zlim=(-1, 1),
        points_style='o', lines_style='k-',
        pix1=None, pix2=None, save_as_gif=False):

    fig = plt.figure()
    ax1 = fig.add_subplot(231, projection='3d')
    ax2 = fig.add_subplot(234, projection='3d')
    im1 = fig.add_subplot(235)
    im2 = fig.add_subplot(236)
    orig_im1 = fig.add_subplot(232)
    orig_im1.imshow(np.array(pix1))
    orig_im2 = fig.add_subplot(233)
    orig_im2.imshow(np.array(pix2))

    im_data1 = im1.imshow(pix1)
    im_data2 = im2.imshow(pix2)

    ax1.set_xlim3d(xlim)
    ax1.set_ylim3d(ylim)
    ax1.set_zlim3d(zlim)

    ax2.set_xlim3d(xlim)
    ax2.set_ylim3d(ylim)
    ax2.set_zlim3d(zlim)

    # init points, lines
    points1, lines1 = visualize3d(k1)
    points2, lines2 = visualize3d(k2)

    plot_points1 = sum([ax1.plot([], [], [], points_style, markersize=10) for _ in range(len(points1))], [])
    plot_lines1 = sum([ax1.plot([], [], [], lines_style, alpha=0.25) for _ in range(len(lines1))], [])

    plot_points2 = sum([ax2.plot([], [], [], points_style, markersize=10) for _ in range(len(points2))], [])
    plot_lines2 = sum([ax2.plot([], [], [], lines_style, alpha=0.25) for _ in range(len(lines2))], [])


    global image_i
    image_i = -1

    def loop(i):

        for j in range(vis_steps):
            update_func1(k1, curr_alpha=alpha_stepper(i * vis_steps + j), curr_diameter=diameter_stepper(i * vis_steps + j))
            update_func2(k2, curr_alpha=alpha_stepper(i * vis_steps + j), curr_diameter=diameter_stepper(i * vis_steps + j))
        points1, lines1 = visualize3d(k1)
        points2, lines2 = visualize3d(k2)

        for i in range(len(points1)):
            plot_points1[i].set_data(points1[i][0], points1[i][1])
            plot_points1[i].set_3d_properties(points1[i][2])
            plot_points1[i].set_color(np.clip(points1[i], 0, 1))

        for i in range(len(lines1)):
            line_data = list(zip(*lines1[i]))

            plot_lines1[i].set_data(line_data[0], line_data[1])
            plot_lines1[i].set_3d_properties(line_data[2])

        for i in range(len(points2)):
            plot_points2[i].set_data(points2[i][0], points2[i][1])
            plot_points2[i].set_3d_properties(points2[i][2])
            plot_points2[i].set_color(np.clip(points2[i], 0, 1))

        for i in range(len(lines2)):
            line_data = list(zip(*lines2[i]))

            plot_lines2[i].set_data(line_data[0], line_data[1])
            plot_lines2[i].set_3d_properties(line_data[2])

        global image_i
        image_i += 1

        if image_i % image_steps == 0:

            nppoints1 = np.clip(np.array(points1), 0, 1)
            nppoints2 = np.clip(np.array(points2), 0, 1)

            kdtree1 = cKDTree(nppoints1)
            kdtree2 = cKDTree(nppoints2)

            _, new_pix_idx = kdtree1.query(pix1, k=1)
            im_data1.set_data(nppoints2[new_pix_idx])

            _, new_pix_idx = kdtree2.query(pix2, k=1)
            im_data2.set_data(nppoints1[new_pix_idx])

    anim = animation.FuncAnimation(fig, loop, frames=steps // vis_steps, interval=1, repeat=False)

    if save_as_gif:
        anim.save('gifs/{}.gif'.format(save_as_gif), writer='imagemagick')

    plt.show()


def run_3d(k, alpha_stepper, diameter_stepper,
        update_func=updater.image3d,
        steps=1000, vis_steps=50, image_steps=10,
        xlim=(-1, 1), ylim=(-1, 1), zlim=(-1, 1),
        points_style='o', lines_style='k-',
        pix=None, save_as_gif=False):

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

    plot_points = sum([ax.plot([], [], [], points_style, markersize=10) for _ in range(len(points))], [])
    # plot_points = sum([ax.plot([], [], [], 'o') for _ in range(len(points))], [])
    plot_lines = sum([ax.plot([], [], [], lines_style, alpha=0.25) for _ in range(len(lines))], [])

    # points, = ax.plot([], [], points_style)
    # points = []
    # lines = [ax.plot([], [], [])[0] for dat in pocet car]

    # drawn = []

    # lines_collection = mc.LineCollection([])
    #
    global image_i
    image_i = -1

    def loop(i):

        for j in range(vis_steps):
            update_func(k, curr_alpha=alpha_stepper(i * vis_steps + j), curr_diameter=diameter_stepper(i * vis_steps + j))
        points, lines = visualize3d(k)

        for i in range(len(points)):
            plot_points[i].set_data(points[i][0], points[i][1])
            plot_points[i].set_3d_properties(points[i][2])
            plot_points[i].set_color(np.clip(points[i], 0, 1))

        if not k.use_alt_update:
            for i in range(len(lines)):
                line_data = list(zip(*lines[i]))

                plot_lines[i].set_data(line_data[0], line_data[1])
                plot_lines[i].set_3d_properties(line_data[2])

        global image_i
        image_i += 1

        if image_i % image_steps == 0:
            nppoints = np.clip(np.array(points), 0, 1)
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

    points, = ax.plot([], [], points_style)
    lines_collection = mc.LineCollection([], linestyles=lines_style)

    def init():
        points.set_data([], [])
        ax.add_collection(lines_collection)

    def loop(i):
        for j in range(vis_steps):
            update_func(k, curr_alpha=alpha_stepper(i * vis_steps + j), curr_diameter=diameter_stepper(i * vis_steps + j))
        visualize(k, points, lines_collection)
        print(diameter_stepper(i * vis_steps))
        return points, lines_collection

    anim = animation.FuncAnimation(fig, loop, init_func=init, frames=steps // vis_steps, interval=1, repeat=False)

    if save_as_gif:
        anim.save('gifs/{}.gif'.format(save_as_gif), writer='imagemagick')

    plt.show()
