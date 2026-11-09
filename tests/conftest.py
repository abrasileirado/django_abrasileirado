"""Configuração mínima do Django para os testes do pacote."""

import django
from django.conf import settings


def pytest_configure() -> None:
    """Configura o Django com o app instalado antes da coleta dos testes."""
    if not settings.configured:
        settings.configure(
            INSTALLED_APPS=[
                "django.contrib.contenttypes",
                "django_abrasileirado",
            ],
            DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
            USE_I18N=True,
        )
    django.setup()
