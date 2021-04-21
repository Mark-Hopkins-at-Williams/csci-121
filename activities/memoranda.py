from random import shuffle
from math import log
from matplotlib.pyplot import plot
from matplotlib import pyplot

COLOR1 = "#FF0000"
COLOR2 = "#0000FF"

class Plotter:

    def __init__(self):
        self.fig, self.ax = pyplot.subplots()

    def plot_range(self, f, a, b, lbl=None, color=None):
        x_coords = list(range(a, b))
        y_coords = []
        for n in range(a, b):
            y_coords += [f(n)]
        self.ax.plot(x_coords, y_coords, label=lbl, color=color)

    def show(self):
        self.fig.legend()
        self.ax.set_title("Asymptotic Analysis")
        self.ax.set_xlabel("n")
        self.ax.set_ylabel("g(n) or kf(n)")
        self.fig.show()


def compare(f, g, k=1):
    plotter = Plotter()
    plotter.plot_range(lambda x: k*f(x), 1, 15, "bigbubble", color=COLOR1)
    plotter.plot_range(g, 1, 15, "katesort", color=COLOR2)
    plotter.show()

def presentation():
    compare(lambda n: n**2, lambda n: n*log(n))


if __name__ == '__main__':
    presentation()
