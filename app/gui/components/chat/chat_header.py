from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QHBoxLayout,
)


class ChatHeader(QFrame):
    """
    Header shown above the AI conversation.
    """

    def __init__(self):
        super().__init__()

        self.setObjectName("ChatHeader")

        layout = QHBoxLayout(self)

        layout.setContentsMargins(15, 12, 15, 12)
        layout.setSpacing(15)

        # ==========================================
        # AI Name
        # ==========================================

        self.title = QLabel("ÆTHERIS AI")
        self.title.setObjectName("ChatHeaderTitle")

        # ==========================================
        # Current Model
        # ==========================================

        self.model = QLabel("Model: qwen3:4b")
        self.model.setObjectName("ChatHeaderModel")

        # ==========================================
        # Status
        # ==========================================

        self.status = QLabel("🟢 Connected")
        self.status.setObjectName("ChatHeaderStatus")

        layout.addWidget(self.title)
        layout.addStretch()
        layout.addWidget(self.model)
        layout.addSpacing(20)
        layout.addWidget(self.status)

    # ==========================================
    # Update Methods
    # ==========================================

    def set_model(self, model: str):
        self.model.setText(f"Model: {model}")

    def set_status(self, status: str):
        self.status.setText(status)