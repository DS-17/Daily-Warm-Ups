# -*- coding: utf-8 -*-
"""Try implementing a helper class for interacting with SQL databases."""
# Author: Brian Thomas Ross <ml@brianthomasross.com>
# License: BSD-3-Clause
from pathlib import Path
import sqlite3
from typing import List


_valid_contexts: List[str] = ['sqlite',
                              # 'postgres',
                              # 'mongo'
                              ]


# Defining this function outside the scope of the class ensures that
# we can use it in the initializer, but if we import the helper class
# into another file it won't crowd the namespace.
def _valid_db_path(pattern: str):
    """Raise an exception in the event of invalid database."""


class DbHelper(object):
    """Helper class for interacting with SQL databases."""

    def __init__(self, path_to_database: str, context: str) -> None:
        f"""
        :param path_to_database: Database path.
        :param context: The type of database to use one of ``_valid_contexts``
        """

    def _connect(self):
        """Establish a connection to the database."""

    def execute(self, statement: str):
        """Execute a single query."""

    def query(self, query: str):
        """Return data from the database."""

    def commit(self):
        """Commit changes to the database."""

    def close(self):
        """Close the connection."""

    # # Stretch: Experiment with context management.
    # def __enter__(self):
    #     """Entering the context statement."""
    #
    # def __exit__(self, ext_type, exc_value, traceback):
    #     """Exiting the context statement."""
