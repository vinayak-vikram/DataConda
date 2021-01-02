#!/usr/bin/env python3

"""
DataConda (http://easy-breezy.xyz/DataConda / https://github.com/ploppy-pigeon/DataConda), developed by Vinayak Vikram, developer of EasyBreezy is a python library for data.

Its features include:
    -   Tkinter Grahing widgets
        -   Chart widgets (class Chart)
        -   Graph widgets (only work with DataConda Chart widgets)(class Graph)
    -   Data Servers/Web apps (class DataServer)
    -   Converting
    -   Parsing

Credits:
    -   StackOverflow for teaching me how to embed matplotlib charts in Tk (used for the Chart and Graph classes) (I fiddled around a bit also) (Link here: https://stackoverflow.com/questions/46332192/displaying-matplotlib-inside-tkinter)
"""

import sqlite3 as sql
import requests
import matplotlib.pyplot as mpl
import matplotlib
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from flask import Flask
from bs4 import BeautifulSoup

app = Flask(__name__)
port = 1500
host = 'localhost'

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

class WebServer():
    """
    Put and get data from IP address (param h (h defauts to 'localhost')) ports (param p (p defaults to 1500))
    """
    def __init__(self, p=1500, h='localhost'):
        global port
        global host
        port = p
        host = h
    def put(self, data, loc='/'):
        """
        Put data (param data) on server page (param loc (loc defaults to '/'))
        """
        @app.route(loc)
        def putat():
            return data
    def do(self):
        """
        Run the server on port (param p (p defaults to 1500)(p must be specified when creating your WebServer())) and host (param h (h defaults to 'localhost')(h must be specified when creating your WebServer()))
        """
        global host
        global port
        app.run(port=port, host=host)
    def get_data(self, where):
        data = requests.get(where)
        data = BeautifulSoup(data.text, 'html.parser')
        return data.prettify()

class SQLite():
    """
    Easy way to manipulate SQLite databases
    Connect to database db
    """
    def __init__(self, db):
        self.sqldb = sql.connect(db)
        self.cursor = self.sqldb.cursor()
    def run(self, cmd):
        """
        Run SQLite command cmd
        Usually used for things like CREATE TABLE, ALTER TABLE, etc
        """
        self.cursor.execute(cmd)
    def exe(self, cmd):
        """
        Run a SQLite command cmd and show the output
        Usually used for SELECT statements
        """
        self.output = self.cursor.execute(cmd).fetchall()
        return self.output

class Mutable():
    """
    Easy parsing and converting
    """
    def __init__(self, data):
        global tt
        tt = data
    class Parsable():
        """
        Easily parse things
        """
        def __init__(self):
            self.text = tt
        def quoteparse(self, splitter:str=" + ", quotechars:list=["'", '"'], vs:dict={}, sp:list=[' + ', '"', "'"], esc:tuple=('\\', '\\'), escmode:bool=True):
            """
            Drop the boring Regexing, just use quoteparse to parse your text
            splitter is what you use to add parts together (default to ' + ')
            quotechars is a list of chracters used as quotation marks
            vs is a dictionary of variables, each key is the variable name, each value is the variable value
            sp is a list of special characters
            esc is a tuple of 2 characters, one is the starting escape character, one is the ending escape character
            escmode is the escape mode. If escmode is True, only a starting escape character is used. If escmode is False, a starting and a ending escape character are used
            """
            text = self.text.split(splitter)
            self.vrs = vs
            output = []
            qchars = []
            for q in quotechars:
                qchars.append(q[0])
            for t in range(len(text)):
                txt = text[t]
                if txt[0] in qchars and txt[-1] in qchars:
                    output.append(txt[1:-1])
                elif txt[0] == esc[0][0] and txt[-1] == esc[1][0] and escmode == False:
                    output.append(sp[int(txt[1:-1])])
                elif txt[0] == esc[0][0] and escmode == True:
                    output.append(sp[int(txt[1:])])
                else:
                    name = txt
                    try:
                        output.append(str(self.vrs[name]))
                    except KeyError:
                        raise NameError("Variable " + txt + " does not exist")
            penultimate = tuple(output)
            end = "".join(penultimate)
            return end
        def cmdparse(self, argchars:tuple=("(", ")"), argsep:str=","):
            cmd = self.text[:self.text.find(argchars[0])]
            args = self.text[self.text.find(argchars[0]) + len(argchars[0]):len(self.text) - len(argchars[1])]
            return cmd, args.split(argsep)
    class Convertible():
        def __init__(self):
            self.text = tt
        def to_table(self):
            """
            Convert a dictionary to a table
            """
            try:
                table = self.text
                tabl = []
                hi = 0
                for h1, h2 in table.items():
                    if len(h1) > hi:
                        hi = len(h1)
                    if len(h2) > hi:
                        hi = len(h2)
                tabl.append("-" * ((hi * 2) + 5))
                for c1, c2 in table.items():
                    v1 = " " * (hi - len(c1))
                    v2 = " " * (hi - len(c2))
                    tabl.append("|" + c1 + v1 + " | " + c2 + v2 + "|")
                    tabl.append("-" * ((hi * 2) + 5))
                tabl = tuple(tabl)
                tabl = "\n".join(tabl)
                return tabl
            except AttributeError:
                raise TypeError("Only dictionaries can be expressed as tables, not " + str(type(table))[8:-2] + "s")  
