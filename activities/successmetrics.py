from random import shuffle
from matplotlib.pyplot import plot
from matplotlib import pyplot

class Plotter:

    def __init__(self):
        self.fig, self.ax = pyplot.subplots()

    def plot_range(self, f, a, b, lbl=None):
        x_coords = list(range(a, b))
        y_coords = []
        for n in range(a, b):
            y_coords += [f(n)]
        self.ax.plot(x_coords, y_coords, label=lbl)

    def show(self):
        self.fig.legend()
        self.ax.set_title("Asymptotic Analysis")
        self.ax.set_xlabel("n")
        self.ax.set_ylabel("g(n) or kf(n)")
        self.fig.show()


def compare(f, g, k=1):
    plotter = Plotter()
    plotter.plot_range(lambda x: k*f(x), 1, 100, "f")
    plotter.plot_range(g, 1, 100, "g")
    plotter.show()
