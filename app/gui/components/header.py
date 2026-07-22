from turtle import right

from app.gui.components.live_clock import LiveClock
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
)

from app.core.constants import (
    APP_NAME,
    APP_VERSION,
    APP_CODENAME,
)


class Header(QFrame):
    """
    Top application header.
    """

    def __init__(self):
        super().__init__()

        self.setObjectName("Header")
        self.setFixedHeight(120)

        # ==========================
        # Main Layout
        # ==========================

        root = QHBoxLayout(self)

        root.setContentsMargins(20, 12, 20, 12)
        root.setSpacing(20)

        # ==========================
        # LEFT
        # ==========================

        left = QVBoxLayout()

        title = QLabel(APP_NAME)
        title.setObjectName("AppTitle")

        subtitle = QLabel("Personal AI Operating Intelligence")
        subtitle.setObjectName("AppSubtitle")

        left.addWidget(title)
        left.addWidget(subtitle)

        # ==========================
        # CENTER
        # ==========================

        center = QVBoxLayout()

        ai_title = QLabel("Current AI")
        ai_title.setObjectName("HeaderLabel")

        self.ai_status = QLabel("Ollama (Local)")
        self.ai_status.setObjectName("HeaderValue")

        center.addWidget(ai_title)
        center.addWidget(self.ai_status)

        # ==========================
        # RIGHT
        # ==========================

        right = QVBoxLayout()

        right.setSpacing(2)
        right.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.status = QLabel("🟢 Ready")
        self.status.setObjectName("HeaderStatus")
        self.status.setAlignment(Qt.AlignmentFlag.AlignRight)

        version = QLabel(f"v{APP_VERSION} • {APP_CODENAME}")
        version.setObjectName("HeaderVersion")
        version.setAlignment(Qt.AlignmentFlag.AlignRight)

        clock = LiveClock()

        right.setSpacing(4)

        right.addWidget(self.status)
        right.addWidget(version)
        right.addWidget(clock)

        # ==========================
        # Assemble
        # ==========================

        root.addLayout(left)
        root.addStretch()
        root.addLayout(center)
        root.addStretch()
        root.addLayout(right)