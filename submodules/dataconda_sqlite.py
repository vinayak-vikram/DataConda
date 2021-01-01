#!/usr/bin/env python3

"""
The Sqlite component to module DataConda (http://easy-breezy.xyz/DataConda / https://github.com/ploppy-pigeon/DataConda) by Vinayak Vikram
"""

import sqlite3 as sql

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
        print(self.output)