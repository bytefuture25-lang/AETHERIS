from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QHBoxLayout,
)

from app.core.constants import (
    APP_NAME,
    APP_VERSION,
    APP_CODENAME,
)


class Header(QFrame):
    def __init__(self):
        super().__init__()

        self.setFixedHeight(70)

        self.setObjectName("Header")

        layout = QHBoxLayout(self)

        layout.setContentsMargins(20, 10, 20, 10)

        title = QLabel(APP_NAME)
        title.setObjectName("AppTitle")

        version = QLabel(
            f"v{APP_VERSION} • {APP_CODENAME}"
        )

        status = QLabel("● Ready")
        status.setAlignment(Qt.AlignmentFlag.AlignRight)

        layout.addWidget(title)
        layout.addStretch()
        layout.addWidget(version)
        layout.addSpacing(20)
        layout.addWidget(status)