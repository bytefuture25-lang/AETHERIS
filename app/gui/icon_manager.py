from pathlib import Path

from PySide6.QtGui import QIcon


ICON_PATH = (
    Path(__file__).parent
    / "assets"
    / "icons"
)


def icon(name: str) -> QIcon:
    """
    Load an SVG icon by filename.

    Example:
        icon("cpu")
    """

    return QIcon(
        str(
            ICON_PATH / f"{name}.svg"
        )
    )