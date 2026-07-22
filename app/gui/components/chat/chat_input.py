from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QTextEdit,
    QPushButton,
)


class ChatInput(QFrame):
    """
    Chat input widget.
    """

    message_sent = Signal(str)

    def __init__(self):
        super().__init__()

        self.setObjectName("ChatInput")

        layout = QHBoxLayout(self)

        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        # ==========================================
        # Input Box
        # ==========================================

        self.input = QTextEdit()

        self.input.setPlaceholderText(
            "Ask ÆTHERIS anything..."
        )

        self.input.setFixedHeight(80)

        # ==========================================
        # Send Button
        # ==========================================

        self.send_button = QPushButton("Send")

        self.send_button.setObjectName("PrimaryButton")

        self.send_button.clicked.connect(
            self.send_message
        )

        # ==========================================
        # Layout
        # ==========================================

        layout.addWidget(self.input, 1)
        layout.addWidget(self.send_button)

    # ==========================================
    # Send Message
    # ==========================================

    def send_message(self):

        text = self.input.toPlainText().strip()

        if not text:
            return

        self.message_sent.emit(text)

        self.input.clear()