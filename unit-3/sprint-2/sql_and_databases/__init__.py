# -*- coding: utf-8 -*-
"""
=================
SQL and Databases
=================

Try creating a helper class for interacting with an SQL database.
"""
from pathlib import Path
import sqlite3


_valid_contexts: List[str] = ['sqlite',
                              # 'postgres',
                              # 'mongo'
                              ]


def _valid_db_path(pattern: str):
    """Validate whether a given string represents a path to a database."""


class DbHelper(object):
    """Helper class for interacting with SQL databases."""

    def __init__(self, path_to_database: str, context: str) -> None:
        f"""
        :param path_to_database: Database path.
        :type path_to_database: str

        :param context: The type of database to use one of ``_valid_contexts``.
        :type context: str
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

    def __enter__(self):
        """Entering a context statement."""

    def __exit__(self, ext_type, exc_value, traceback):
        """Exiting a context statement."""
