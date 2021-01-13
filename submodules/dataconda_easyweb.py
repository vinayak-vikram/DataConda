#!/usr/bin/env python3

"""
The WebServer component to module DataConda (http://easy-breezy.xyz/DataConda / https://github.com/ploppy-pigeon/DataConda) by Vinayak Vikram
"""

from flask import Flask

app = Flask(__name__)
port = 1500
host = 'localhost'

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
