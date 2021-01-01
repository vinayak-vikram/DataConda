#!/usr/bin/env python3

"""
The Charts component to module DataConda (http://easy-breezy.xyz/DataConda / https://github.com/ploppy-pigeon/DataConda) by Vinayak Vikram
"""

import matplotlib
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

matplotlib.use("TkAgg")

class Chart(tk.Frame):
    """
    Make a (empty) chart widget in a Tk
    """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

    def add_graph(self, fig):
        """
        Add a Graph widget (param fig) to the Chart
        """
        self.mpl_canvas = FigureCanvasTkAgg(fig, self)
        self.mpl_canvas.show()
        self.mpl_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.toolbar = NavigationToolbar2TkAgg(self.mpl_canvas, self)
        self.toolbar.update()
        self.mpl_canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class Graph(Figure):
    """
    Add a Graph widget to your Chart widget
    Graph contains:
        -   Pie charts
        -   Bar charts
        -   Line plots
    """
    def __init__(self):
        Figure.__init__(self, figsize=(5, 5), dpi=100)
    def pie(self, data : list):
        """
        Make a pie chart with data (param data) as a list of portions to put in the pie chart
        """
        self.plot = self.add_subplot(111)
        dat = []
        for d in data:
            try:
                dat.append(float(d))
            except ValueError:
                raise ValueError("Pie portion must be int or float, not " + str(type(d))[7:-1])
        self.plot.pie(dat)
    def bar(self, data : dict):
        """
        Make a bar chart with data (param data) as a dictionary, each key is the position in the bar chart, each value is the height of the bar
        """
        cdata = []
        rdata = []
        for c,r in data.items():
            try:
                cdata.append(float(c))
            except ValueError:
                raise ValueError("Bar height must be int or float, not " + str(type(c))[7:-1])
            rdata.append(r)
        self.plot = self.add_subplot(111)
        self.plot.bar(cdata, rdata)
    def plt(self, data : dict):
        """
        Make a line plot with data (param data) as a dictionary, each key is the height of the point, each value is the position of the point
        """
        cdata = []
        rdata = []
        for c,r in data.items():
            try:
                cdata.append(float(c))
            except ValueError:
                raise ValueError("Point height must be int or float, not " + str(type(c))[7:-1])
            try:
                rdata.append(r)
            except ValueError:
                raise ValueError("Point position must be int or float, not " + str(type(c))[7:-1])
        self.plot = self.add_subplot(111)
        self.plot.plot(cdata, rdata)