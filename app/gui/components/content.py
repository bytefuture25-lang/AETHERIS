from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QFrame,
    QVBoxLayout,
)


class Content(QFrame):
    def __init__(self):
        super().__init__()

        self.setObjectName("Content")

        layout = QVBoxLayout(self)

        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title = QLabel("Welcome to ÆTHERIS")
        title.setObjectName("ContentTitle")

        subtitle = QLabel(
            "Personal AI Operating Intelligence"
        )

        info = QLabel(
            "Dashboard Foundation Loaded Successfully."
        )

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(20)
        layout.addWidget(info)