from __future__ import annotations

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QSizePolicy,
)


class MessageBubble(QFrame):
    """
    Modern reusable chat bubble.
    Supports copy button for AI messages.
    """

    def __init__(self, text: str, is_user: bool = False):
        super().__init__()

        self.is_user = is_user

        self.setObjectName("UserBubble" if is_user else "AIBubble")

        self.setMinimumWidth(140)
        self.setMaximumWidth(650)
        self.setSizePolicy(
            QSizePolicy.Policy.Maximum,
            QSizePolicy.Policy.Minimum,
        )

        root = QVBoxLayout(self)
        root.setContentsMargins(12, 10, 12, 10)
        root.setSpacing(8)

        self.label = QLabel(text)
        self.label.setWordWrap(True)
        self.label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.label.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Preferred,
        )

        root.addWidget(self.label)

        action_row = QHBoxLayout()
        action_row.setContentsMargins(0, 0, 0, 0)
        action_row.setSpacing(6)
        action_row.addStretch()

        self.copy_button = None

        if not is_user:
            self.copy_button = QPushButton("📋 Copy")
            self.copy_button.setObjectName("BubbleCopyButton")
            self.copy_button.setCursor(Qt.CursorShape.PointingHandCursor)
            self.copy_button.setFixedHeight(28)
            self.copy_button.clicked.connect(self.copy_message)
            action_row.addWidget(self.copy_button)

        root.addLayout(action_row)

    def copy_message(self):
        if self.is_user:
            return

        clipboard = QGuiApplication.clipboard()
        clipboard.setText(self.label.text())

        if self.copy_button is None:
            return

        self.copy_button.setText("✅ Copied!")
        self.copy_button.setEnabled(False)

        QTimer.singleShot(
            1800,
            self._reset_copy_button,
        )

    def _reset_copy_button(self):
        if self.copy_button is None:
            return

        self.copy_button.setText("📋 Copy")
        self.copy_button.setEnabled(True)