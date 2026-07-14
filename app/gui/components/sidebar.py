from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QPushButton,
    QVBoxLayout,
)


class Sidebar(QFrame):
    def __init__(self):
        super().__init__()

        self.setObjectName("Sidebar")
        self.setFixedWidth(220)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(15, 20, 15, 20)
        layout.setSpacing(10)

        title = QLabel("Navigation")
        title.setObjectName("SidebarTitle")

        layout.addWidget(title)

        items = [
            "🏠 Dashboard",
            "🤖 AI Chat",
            "🎤 Voice",
            "🧠 Memory",
            "⚙ Automation",
            "💻 Coding",
            "🌐 Browser",
            "🔌 Plugins",
            "⚙ Settings",
        ]

        for item in items:
            button = QPushButton(item)
            button.setCursor(Qt.PointingHandCursor)
            button.setObjectName("NavButton")
            button.setMinimumHeight(40)
            layout.addWidget(button)

        layout.addStretch()