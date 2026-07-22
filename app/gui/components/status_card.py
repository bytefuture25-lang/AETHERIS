from app.gui.effects import create_shadow
from app.gui.icon_manager import icon
from PySide6.QtCore import QSize
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QProgressBar,
)


class StatusCard(QFrame):
    """
    Reusable dashboard status card.
    """

    ICON_MAP = {
        "CPU": "cpu",
        "RAM": "ram",
        "Internet": "internet",
        "Voice": "microphone",

        "Claude": "ai",
        "ChatGPT": "ai",
        "Gemini": "ai",
        "Ollama": "ai",
    }

    def __init__(
        self,
        title: str,
        value: str,
        status: str = ""
    ):
        super().__init__()

        self.setObjectName("StatusCard")

        # =========================================
        # Main Layout
        # =========================================

        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)

        # =========================================
        # Header
        # =========================================

        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(0, 0, 0, 0)

        self.icon_button = QPushButton()

        self.icon_button.setObjectName("CardIcon")

        self.icon_button.setFlat(True)

        self.icon_button.setEnabled(False)

        self.icon_button.setIcon(
            icon(
                self.ICON_MAP.get(title, "ai")
            )
        )

        self.icon_button.setIconSize(
            QSize(20, 20)
        )

        self.icon_button.setFixedSize(24, 24)
        self.title_label = QLabel(title)
        self.title_label.setObjectName("CardTitle")

        header_layout.addWidget(self.icon_button)
        header_layout.addSpacing(8)
        header_layout.addWidget(self.title_label)
        header_layout.addStretch()

        # =========================================
        # Main Value
        # =========================================

        self.value_label = QLabel(value)
        self.value_label.setObjectName("CardValue")

        # =========================================
        # Progress Bar
        # =========================================

        self.progress = QProgressBar()
        self.progress.setObjectName("CardProgress")
        self.progress.setRange(0, 100)
        self.progress.setValue(0)
        self.progress.setTextVisible(False)

        # =========================================
        # Status
        # =========================================

        self.status_label = QLabel(status)
        self.status_label.setObjectName("CardStatus")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        # =========================================
        # Build Layout
        # =========================================

        layout.addLayout(header_layout)
        layout.addWidget(self.value_label)
        layout.addWidget(self.progress)
        layout.addStretch()
        layout.addWidget(self.status_label)

        # =========================================
        # Glass Shadow (Apply Once)
        # =========================================

        self.setGraphicsEffect(
            create_shadow(
                blur=40,
                x=0,
                y=8,
            )
        )

    # ==================================================
    # Update Methods
    # ==================================================

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

    def set_progress(self, value: int):
        """
        Update progress bar.
        """
        value = max(0, min(100, value))
        self.progress.setValue(value)

    def update(
        self,
        value: str,
        status: str,
        status_color: str = "#22C55E",
    ):
        """
        Update the complete card.
        """

        self.update_value(value)
        self.update_status(status)
        self.set_status_color(status_color)

        # Automatically update progress if the
        # value contains a percentage.

        try:
            number = int(
                float(
                    value.replace("%", "").strip()
                )
            )

            self.progress.setValue(number)

        except Exception:
            pass