from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QHBoxLayout,
    QScrollArea,
    QWidget,
)

from app.gui.components.chat.message_bubble import MessageBubble
from app.gui.components.chat.typing_indicator import TypingIndicator


class ChatHistory(QFrame):
    """
    Modern scrollable chat history with streaming support.
    """

    def __init__(self):
        super().__init__()

        self.setObjectName("ChatHistory")

        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )

        self.container = QWidget()
        self.messages_layout = QVBoxLayout(self.container)
        self.messages_layout.setContentsMargins(20, 20, 20, 20)
        self.messages_layout.setSpacing(12)
        self.messages_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.scroll.setWidget(self.container)
        root.addWidget(self.scroll)

        self._typing = None
        self._stream_bubble = None

        self.add_ai_message(
            "👋 Hello Harsh!\n\nI am ÆTHERIS.\nHow can I help you today?"
        )

    def _scroll_bottom(self):
        bar = self.scroll.verticalScrollBar()
        bar.setValue(bar.maximum())

    def _create_row(self, bubble, is_user: bool):
        row = QHBoxLayout()
        row.setContentsMargins(0, 0, 0, 0)

        if is_user:
            row.addStretch()
            row.addWidget(bubble)
        else:
            row.addWidget(bubble)
            row.addStretch()

        self.messages_layout.addLayout(row)
        self._scroll_bottom()

    # ==================================================
    # Standard Messages
    # ==================================================

    def add_user_message(self, text: str):
        bubble = MessageBubble(text=text, is_user=True)
        self._create_row(bubble, True)

    def add_ai_message(self, text: str):
        bubble = MessageBubble(text=text, is_user=False)
        self._create_row(bubble, False)

    # ==================================================
    # Typing Indicator
    # ==================================================

    def show_typing(self):
        if self._typing is not None:
            return

        self._typing = TypingIndicator()

        row = QHBoxLayout()
        row.setContentsMargins(0, 0, 0, 0)
        row.addWidget(self._typing)
        row.addStretch()

        self.messages_layout.addLayout(row)
        self._scroll_bottom()

    def hide_typing(self):
        if self._typing is None:
            return

        self._typing.deleteLater()
        self._typing = None

    # ==================================================
    # Streaming
    # ==================================================

    def begin_ai_stream(self):
        self.hide_typing()

        if self._stream_bubble is not None:
            return

        self._stream_bubble = MessageBubble(text="", is_user=False)
        self._create_row(self._stream_bubble, False)

    def append_ai_stream(self, chunk: str):
        if not chunk:
            return

        if self._stream_bubble is None:
            self.begin_ai_stream()

        current = self._stream_bubble.label.text()
        self._stream_bubble.label.setText(current + chunk)
        self._scroll_bottom()

    def finish_ai_stream(self):
        self._stream_bubble = None