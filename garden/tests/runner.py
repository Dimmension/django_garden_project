"""Module that provides runner for tests."""
from types import MethodType
from typing import Any

from django.db import connections
from django.db.backends.base.base import BaseDatabaseWrapper
from django.test.runner import DiscoverRunner


def prepare_db(self):
    """Prepare database for tests."""
    self.connect()
    self.connection.cursor().execute('CREATE SCHEMA IF NOT EXISTS garden;')
    self.connection.cursor().execute('CREATE EXTENSION postgis;')


class PostgresSchemaRunner(DiscoverRunner):
    """Represents postgres db runner."""

    def setup_databases(self, **kwargs: Any) -> list[tuple[BaseDatabaseWrapper, str, bool]]:
        """Set up db.

        Returns:
            list[tuple[BaseDatabaseWrapper, str, bool]]: _description_
        """
        for conn_name in connections:
            connection = connections[conn_name]
            connection.prepare_database = MethodType(prepare_db, connection)
        return super().setup_databases(**kwargs)
