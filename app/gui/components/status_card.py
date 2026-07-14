from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
)


class StatusCard(QFrame):
    """
    Reusable dashboard status card.
    """

    def __init__(
        self,
        title: str,
        value: str,
        status: str = ""
    ):
        super().__init__()

        self.setObjectName("StatusCard")

        layout = QVBoxLayout(self)

        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(8)

        title_label = QLabel(title)
        title_label.setObjectName("CardTitle")

        value_label = QLabel(value)
        value_label.setObjectName("CardValue")

        status_label = QLabel(status)
        status_label.setObjectName("CardStatus")
        status_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        layout.addWidget(title_label)
        layout.addWidget(value_label)
        layout.addStretch()
        layout.addWidget(status_label)