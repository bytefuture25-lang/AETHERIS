from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
)


class BasePage(QWidget):
    """
    Base page for all ÆTHERIS pages.

    Provides:
    - Page title
    - Page subtitle
    - Content layout for child pages
    """

    def __init__(
        self,
        title: str,
        subtitle: str,
    ):
        super().__init__()

        # ==========================================
        # Root Layout
        # ==========================================

        self.root_layout = QVBoxLayout(self)

        self.root_layout.setContentsMargins(
            20,
            20,
            20,
            20,
        )

        self.root_layout.setSpacing(20)

        self.root_layout.setAlignment(
            Qt.AlignmentFlag.AlignTop
        )

        # ==========================================
        # Title
        # ==========================================

        self.title_label = QLabel(title)
        self.title_label.setObjectName("PageTitle")

        # ==========================================
        # Subtitle
        # ==========================================

        self.subtitle_label = QLabel(subtitle)
        self.subtitle_label.setObjectName("PageSubtitle")

        self.root_layout.addWidget(
            self.title_label
        )

        self.root_layout.addWidget(
            self.subtitle_label
        )

        # ==========================================
        # Content Layout
        # ==========================================

        self.content_layout = QVBoxLayout()

        self.content_layout.setSpacing(15)

        self.root_layout.addLayout(
            self.content_layout,
            1,
        )