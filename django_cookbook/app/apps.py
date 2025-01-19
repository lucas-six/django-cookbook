"""App configurations."""

from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    """App Config."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
