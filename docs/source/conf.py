"""Configure sphinx documentation."""

import datetime
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parents[2]))

_year = datetime.datetime.utcnow().year

author = ""  # noqa: F841
project = ""  # noqa: F841
project_copyright = f"2021-{_year},"  # noqa: F841
with open(
    pathlib.Path().resolve().parent.parent.joinpath("VERSION"), encoding="utf8"
) as f:
    release = version = f.read().strip()  # noqa: F841

extensions = [  # noqa: F841
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
]

autoclass_content = "both"  # noqa: F841
autosummary_generate = True  # noqa: F841
html_logo = "static/logo.png"  # noqa: F841
html_theme = "furo"  # noqa: F841
# https://pradyunsg.me/furo/customisation
html_theme_options = {  # noqa: F841
    "light_css_variables": {
        "color-brand-primary": "red",
        "color-brand-content": "#CC3333",
        "color-admonition-background": "orange",
    },
    "dark_css_variables": {
        "color-brand-primary": "red",
        "color-brand-content": "#CC3333",
        "color-admonition-background": "orange",
    },
    "sidebar_hide_name": True,
    "navigation_with_keys": True,
}
html_static_path = [  # noqa: F841
    "static",
]
intersphinx_mapping = {  # noqa: F841
    "python": ("https://docs.python.org/3/", None),
}
set_type_checking_flag = True  # noqa: F841
templates_path = [  # noqa: F841
    "templates",
]
