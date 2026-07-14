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

        # -----------------------------
        # Title
        # -----------------------------
        self.title_label = QLabel(title)
        self.title_label.setObjectName("CardTitle")

        # -----------------------------
        # Value (Dynamic)
        # -----------------------------
        self.value_label = QLabel(value)
        self.value_label.setObjectName("CardValue")

        # -----------------------------
        # Status (Dynamic)
        # -----------------------------
        self.status_label = QLabel(status)
        self.status_label.setObjectName("CardStatus")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        # -----------------------------
        # Layout
        # -----------------------------
        layout.addWidget(self.title_label)
        layout.addWidget(self.value_label)
        layout.addStretch()
        layout.addWidget(self.status_label)

    # ---------------------------------
    # Update Methods
    # ---------------------------------

    def update_title(self, title: str):
        self.title_label.setText(title)

    def update_value(self, value: str):
        self.value_label.setText(value)

    def update_status(self, status: str):
        self.status_label.setText(status)

    def set_value_color(self, color: str):
        self.value_label.setStyleSheet(
            f"color: {color};"
        )

    def set_status_color(self, color: str):
        self.status_label.setStyleSheet(
            f"color: {color};"
        )

    def update(
        self,
        value: str,
        status: str,
        status_color: str = "#22C55E",
    ):
        """
        Update the entire card at once.
        """
        self.update_value(value)
        self.update_status(status)
        self.set_status_color(status_color)