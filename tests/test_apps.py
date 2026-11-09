"""Testes de registro do app django_abrasileirado."""

from django.apps import apps

from django_abrasileirado import migrations
from django_abrasileirado.apps import DjangoAbrasileiradoConfig


def test_app_registrado() -> None:
    config = apps.get_app_config("django_abrasileirado")
    assert isinstance(config, DjangoAbrasileiradoConfig)
    assert config.name == "django_abrasileirado"


def test_verbose_name() -> None:
    config = apps.get_app_config("django_abrasileirado")
    assert str(config.verbose_name) == "django_abrasileirado"


def test_pacote_migrations_importavel() -> None:
    assert migrations.__author__.startswith("Kelson da Costa Medeiros")
