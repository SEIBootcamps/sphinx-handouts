import importlib.metadata
from typing import TYPE_CHECKING
from os import path
from pathlib import Path

from . import directives

if TYPE_CHECKING:
    from typing import Any, Dict

    from sphinx.application import Sphinx

__name__ = "sphinx_handouts"
__version__ = importlib.metadata.version("sphinx-handouts")

package_dir = Path(path.abspath(path.dirname(__file__)))
themes_dir = package_dir / "themes"
seibootcamps_theme_dir = themes_dir / "seibootcamps"


def setup(app: "Sphinx") -> "Dict[str, Any]":
    # Config values
    app.add_config_value(
        "handouts_font_preconnect",
        [
            "https://fonts.googleapis.com",
            "https://fonts.gstatic.com",
        ],
        rebuild="html",
    )

    # Theme: seibootcamps
    app.add_html_theme("seibootcamps", str(seibootcamps_theme_dir.resolve()))
    app.connect("html-page-context", add_preconnect_to_page_context)

    # Directives
    directives.setup(app)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def add_preconnect_to_page_context(app, _, __, context, ___) -> None:
    context["handouts_font_preconnect"] = app.config.handouts_font_preconnect
