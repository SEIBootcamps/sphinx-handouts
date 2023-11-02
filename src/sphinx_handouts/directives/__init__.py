from typing import TYPE_CHECKING

from . import admonitions

if TYPE_CHECKING:
    from sphinx.application import Sphinx


def setup(app: "Sphinx") -> None:
    admonitions.setup(app)
