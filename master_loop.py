import matplotlib.pyplot as plt
from matplotlib import animation
from visualizer import visualize
import updater
from matplotlib import collections as mc


def run(k, alpha_stepper, diameter_stepper,
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
        anim.save('gifs/%s.gif' % save_as_gif, writer='imagemagick')

    plt.show()
