from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import (
    QLabel,
    QFrame,
    QHBoxLayout,
)


class TypingIndicator(QFrame):
    """
    Animated typing indicator.
    """

    def __init__(self):
        super().__init__()

        self.setObjectName("TypingIndicator")

        self.label = QLabel("●")
        self.label.setObjectName("TypingLabel")

        layout = QHBoxLayout(self)

        layout.setContentsMargins(16, 12, 16, 12)

        layout.addWidget(self.label)

        self.frame = 0

        self.timer = QTimer(self)

        self.timer.timeout.connect(
            self.animate
        )

        self.timer.start(350)

    def animate(self):

        self.frame = (self.frame + 1) % 4

        self.label.setText(
            "●" * (self.frame + 1)
        )