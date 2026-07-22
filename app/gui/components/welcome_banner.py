from datetime import datetime

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QToolButton,
)

from app.gui.icon_manager import icon


class WelcomeBanner(QFrame):
    """
    Dashboard Hero Banner
    """

    def __init__(self):
        super().__init__()

        self.setObjectName("WelcomeBanner")

        root = QVBoxLayout(self)

        root.setContentsMargins(25, 20, 25, 20)
        root.setSpacing(15)

        # ==========================================
        # Greeting
        # ==========================================

        hour = datetime.now().hour

        if hour < 12:
            greeting = "Good Morning"
        elif hour < 17:
            greeting = "Good Afternoon"
        elif hour < 21:
            greeting = "Good Evening"
        else:
            greeting = "Good Night"

        title = QLabel(f"{greeting}, Harsh")
        title.setObjectName("BannerTitle")

        subtitle = QLabel(
            "Personal AI Operating Intelligence"
        )
        subtitle.setObjectName("BannerSubtitle")

        # ==========================================
        # Information Chips
        # ==========================================

        chip_layout = QHBoxLayout()
        chip_layout.setSpacing(12)

        chip_layout.addWidget(
            self.create_chip(
                "browser",
                "Windows"
            )
        )

        chip_layout.addWidget(
            self.create_chip(
                "ai",
                "Ollama Local"
            )
        )

        chip_layout.addWidget(
            self.create_chip(
                "dashboard",
                "Genesis v0.1"
            )
        )

        chip_layout.addStretch()

        # ==========================================
        # Layout
        # ==========================================

        root.addWidget(title)
        root.addWidget(subtitle)
        root.addSpacing(5)
        root.addLayout(chip_layout)

        root.setAlignment(Qt.AlignmentFlag.AlignTop)

    # =====================================================
    # Reusable Chip
    # =====================================================

    def create_chip(
        self,
        icon_name: str,
        text: str,
    ) -> QToolButton:

        button = QToolButton()

        button.setText(text)

        button.setIcon(
            icon(icon_name)
        )

        button.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon
        )

        button.setObjectName("BannerChip")

        button.setAutoRaise(True)

        button.setCursor(
            Qt.CursorShape.ArrowCursor
        )

        return button