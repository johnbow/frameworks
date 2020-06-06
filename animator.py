from matplotlib import animation as ani
from matplotlib import pyplot as plt


class PlotAnimation:

    def __init__(self, x, y_list,
                 frames=60,
                 duration=2,
                 plot_update=None,):
        self.x = x
        self.y_list = y_list
        self.frames = frames
        self.duration = duration
        self.plot_update = plot_update
        self.line, = plt.plot([], [], lw=3)
        self.anim = None

    def animate(self, i):
        plt.cla()
        self.line, = plt.plot(self.x, self.y_list[i])
        if self.plot_update is not None:
            self.plot_update()
        return self.line,

    def init_func(self):
        self.line.set_data([], [])
        return self.line,

    def save(self, filename):
        print(f"saving animation as {filename}. fps: {int(self.frames / self.duration)}. "
              f"duration: {self.duration}sec.\nmatplotlib might need to try another saving method...")
        fig = plt.figure(1)
        self.anim = ani.FuncAnimation(fig, self.animate, frames=self.frames,
                                      interval=int(self.duration * 1000 / self.frames))
        self.anim.save(filename)
        print("animation saved")

    def start(self):
        if self.anim is None:
            fig = plt.figure(1)
            self.anim = ani.FuncAnimation(fig, self.animate, frames=self.frames,
                                          interval=int(self.duration * 1000 / self.frames))
        plt.show()


class ContourAnimation:

    def __init__(self, x, y, z_list,
                 frames=60,
                 duration=2,
                 plot_update=None,
                 levels=None):
        self.x = x
        self.y = y
        self.z_list = z_list
        self.frames = frames
        self.duration = duration
        self.plot_update = plot_update
        self.levels = levels
        self.anim = None

    def animate(self, i):
        plt.cla()
        if self.levels is not None:
            cont = plt.contourf(self.x, self.y, self.z_list[i], self.levels)
        else:
            cont = plt.contourf(self.x, self.y, self.z_list[i])
        if self.plot_update is not None:
            self.plot_update(i)
        return cont

    def save(self, filename):
        print(f"saving animation as {filename}. fps: {int(self.frames / self.duration)}. "
              f"duration: {self.duration}sec.\nmatplotlib might need to try another saving method...")
        fig = plt.figure(1)
        self.anim = ani.FuncAnimation(fig, self.animate, frames=self.frames,
                                      interval=int(self.duration * 1000 / self.frames))
        self.anim.save(filename)
        print("animation saved")

    def start(self):
        if self.anim is None:
            fig = plt.figure(1)
            self.anim = ani.FuncAnimation(fig, self.animate, frames=self.frames,
                                          interval=int(self.duration * 1000 / self.frames))
        plt.show()
