import matplotlib.pyplot as plt
from matplotlib import animation
from visualizer import visualize
import updater


def run(k, update_func=updater.uniform,
        steps=1000, vis_steps=50,
        alpha_init=0.3, alpha_const=100, alpha_speed=0.95,
        diameter_init=3, diameter_const=1, diameter_speed=1,
        xlim=(-1, 1), ylim=(-1, 1),
        points_style='ro', lines_style='b-',
        save_as_gif=False):

    fig = plt.figure()
    ax = fig.add_subplot(111, xlim=xlim, ylim=ylim)

    global curr_alpha, curr_diameter, points, lines

    points, = ax.plot([], [], points_style)
    lines, = ax.plot([], [], lines_style)

    curr_alpha = alpha_init
    curr_diameter = diameter_init

    def update_attributes(i):
        global curr_alpha, curr_diameter

        if i % alpha_const == 0:
            curr_alpha *= alpha_speed
        if i % diameter_const == 0:
            curr_diameter *= diameter_speed

    def init():
        lines.set_data([], [])
        points.set_data([], [])

    def loop(i):
        for j in range(vis_steps):
            update_func(k, curr_alpha=curr_alpha, curr_diameter=curr_diameter)
            update_attributes(i * vis_steps + j)
        visualize(k, points, lines)
        return points, lines

    anim = animation.FuncAnimation(fig, loop, init_func=init, frames=steps // vis_steps, interval=1, repeat=False)

    if save_as_gif:
        anim.save('gifs/%s.gif' % save_as_gif, writer='imagemagick')

    plt.show()
