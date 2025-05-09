"""App configurations."""

from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    """App Configuration."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    verbose_name = 'APP'
