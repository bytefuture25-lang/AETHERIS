from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QFrame, QVBoxLayout


class WelcomeBanner(QFrame):
    """
    Welcome section shown on the Dashboard.
    """

    def __init__(self):
        super().__init__()

        self.setObjectName("WelcomeBanner")

        layout = QVBoxLayout(self)

        layout.setContentsMargins(20, 20, 20, 20)

        title = QLabel("Welcome to ÆTHERIS")
        title.setObjectName("BannerTitle")

        subtitle = QLabel(
            "Personal AI Operating Intelligence"
        )
        subtitle.setObjectName("BannerSubtitle")

        layout.addWidget(title)
        layout.addWidget(subtitle)

        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)