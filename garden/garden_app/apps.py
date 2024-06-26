"""Module that provides apps."""
from django.apps import AppConfig


class GardenAppConfig(AppConfig):
    """Represent django application config."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'garden_app'
