import threading
import time
from datetime import datetime

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from scipy.ndimage.filters import gaussian_filter1d

from core.Config import Config

config = Config()

class RealtimePlot(object):
    def __init__(self, title="Realtime Plot"):
        plt.style.use("dark_background")
        self.fig = plt.figure()
        self.title = title
        self.fig.canvas.set_window_title(title)
        self.ax = self.fig.add_subplot(111)
        self.x = []
        self.y = []
        self.setup_ax()
        self.lock = threading.RLock()

    def add_new_datapoint(self, timeIdentifier, dataPoint):
        dt_object = datetime.fromtimestamp(timeIdentifier / 1000)
        
        with self.lock:
            self.x.append(dt_object)
            self.y.append(float(dataPoint)) 
            number_of_points_on_plot = config["plot"]["max_number_of_points"]
            if (len(self.x) > number_of_points_on_plot):
                self.x = self.x[-number_of_points_on_plot:]
                self.y = self.y[-number_of_points_on_plot:]

    def setup_ax(self):
        self.ax.clear()
        self.ax.set_title(self.title)
        yf = lambda y, pos: f'{y:.2f}'
        self.ax.yaxis.set_major_formatter(FuncFormatter(yf))

    def start(self):
        while True:
            self.setup_ax()

            with self.lock:
                self.ax.plot(self.x, self.y,'ro', color='lightgrey')
                ysmoothed = gaussian_filter1d(self.y, sigma=config["plot"]["smoothing_sigma"])
                self.ax.plot(self.x, ysmoothed, color='brown')

            self.fig.canvas.draw()

            self.fig.show()
            plt.pause(0.05)
