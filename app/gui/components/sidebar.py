from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QPushButton,
    QVBoxLayout,
)

from app.gui.navigation import NAV_ITEMS


class Sidebar(QFrame):
    """
    ÆTHERIS Navigation Sidebar
    """

    page_selected = Signal(str)

    def __init__(self):
        super().__init__()

        self.setObjectName("Sidebar")
        self.setFixedWidth(220)

        self.buttons = {}

        self._build_ui()

    def _build_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(15, 20, 15, 20)
        layout.setSpacing(10)

        title = QLabel("Navigation")
        title.setObjectName("SidebarTitle")

        layout.addWidget(title)

        for item in NAV_ITEMS:

            button = QPushButton(item["title"])

            button.setObjectName("NavButton")

            button.setCursor(Qt.PointingHandCursor)

            button.setMinimumHeight(40)

            button.clicked.connect(
                lambda checked=False, page=item["id"]:
                self.page_selected.emit(page)
            )

            layout.addWidget(button)

            self.buttons[item["id"]] = button

        layout.addStretch()

    def set_active(self, page_id: str):

        for pid, button in self.buttons.items():

            if pid == page_id:
                button.setProperty("active", True)
            else:
                button.setProperty("active", False)

            button.style().unpolish(button)
            button.style().polish(button)