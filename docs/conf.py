# docs/conf.py
import os
import sys

sys.path.insert(0, os.path.abspath(".."))

# O autodoc importa os módulos do app; strings lazy (gettext_lazy) exigem o Django configurado.
import django  # noqa: E402
from django.conf import settings  # noqa: E402

if not settings.configured:
    settings.configure(
        INSTALLED_APPS=["django.contrib.contenttypes", "django_abrasileirado"],
        USE_I18N=True,
    )
django.setup()

project = "django_abrasileirado"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx.ext.napoleon",  # se usar docstring Google/NumPy
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

root_doc = "index"

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

html_theme_options = {
    "navigation_depth": 4,
    "collapse_navigation": False,
    "sticky_navigation": True,
}
