from PySide6.QtGui import QColor
from PySide6.QtWidgets import QGraphicsDropShadowEffect


def create_shadow(
    blur=45,
    x=0,
    y=8,
    color=QColor(0, 212, 255, 90),
):
    """
    Create a reusable glow/shadow effect.
    """

    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(blur)
    shadow.setOffset(x, y)
    shadow.setColor(color)

    return shadow