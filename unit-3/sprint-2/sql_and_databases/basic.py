# -*- coding: utf-8 -*-
"""SQL helper classes.

The purpose of this warm-up is to examine how OOP principles can be
applied to SQL tasks.

You should try to complete the following code which will allow for
performing common database manipulations in an OOP context.
"""
from typing import Dict, List
from pathlib import Path

import pandas as pd
import sqlite3


def _validate_filepath(pattern: str) -> None:
    """Validate that a provided filepath exists.

    :param pattern: A filepath
    :type pattern: str
    :return: None if file exists.
    :raises: ?
    """
    # Your code here, for help look into the ``pathlib`` module


# Stretch: See if you can implement a database registry to handle multiple
#          databases simultaneously.
# _db_lookup: Dict[str, str] = {}
# _registered_databases = []
# _reserved_kwds = ['all']


def _df_to_statement(frame: pd.core.DataFrame) -> str:
    """Convert a pandas DataFrame to and SQL statement."""
    # Your code here


# Stretch: Implement a custom class for database errors.
# class DbError(AttributeError, KeyError):
#     """Error message for handling for database errors.
#
#     Extends on ``AttributeError``, ``KeyError``.
#     """

# Why inherit from ``object``?
# Zen of Python: Explicit is better than implicit.
class DbHelper(object):
    """A class to help with SQL Databases."""

    def __init__(self, db: str, statements=None) -> None:
        """
        :param db: Path to the database
        :type db: str
        """
        self._db = _validate_filepath(db)  # noqa
        self.connection, self.cursor = self._connect()

    def _connect(self) -> None:
        """Connect to the database."""
        # Your code here. As implied above this should return both
        # connection and cursor.

        # return conn, cur

    def create_table(self, data: str):
        """Create a table if it does not exist."""

    def execute(self, data: str):
        """Execute a single statement."""
        # if isinstance(self._db, pd.core.DataFrame):
        #     # Do something
        # else:
        #     # Do something else.

    def execute_many(self, data: List[str]):
        """Execute many statements."""

    def commit(self):
        """Commit changes to the database."""

    def close(self) -> None:
        """Close the database connection."""
        # Your code here a method to close out the connection.

    # stretch territory
    # context management
    # def __enter__(self):
    #     return self
    #
    # def __exit__(self, ext_type, exc_value, traceback):
    #     """Exit logic.
    #
    #     Defining exception handling here allows the class to be used
    #     inside of a ``with`` statement, and closed out upon error.
    #     """
    
