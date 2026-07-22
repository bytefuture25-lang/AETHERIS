from PySide6.QtCore import Qt, Signal, QSize
from app.gui.icon_manager import icon
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QPushButton,
    QVBoxLayout,
)

from app.core.constants import (
    APP_NAME,
    APP_VERSION,
    APP_CODENAME,
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
        self.setFixedWidth(240)

        self.buttons = {}

        self._build_ui()

    def _build_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(18, 20, 18, 20)
        layout.setSpacing(12)

        # ===================================
        # Logo
        # ===================================

        logo = QLabel(APP_NAME)
        logo.setObjectName("SidebarLogo")

        layout.addWidget(logo)

        # ===================================
        # Navigation Title
        # ===================================

        title = QLabel("Navigation")
        title.setObjectName("SidebarTitle")

        layout.addWidget(title)

        # ===================================
        # Navigation Buttons
        # ===================================

        for item in NAV_ITEMS:
            button = QPushButton(item["title"])

            # Load SVG Icon
            button.setIcon(icon(item["icon"]))

            # Icon Size
            button.setIconSize(QSize(22, 22))

            button.setObjectName("NavButton")

            button.setCursor(Qt.PointingHandCursor)

            button.setMinimumHeight(46)

            button.clicked.connect(
                lambda checked=False, page=item["id"]: self.page_selected.emit(page)
            )

            layout.addWidget(button)

            self.buttons[item["id"]] = button

        layout.addStretch()

        # ===================================
        # Footer
        # ===================================

        footer = QLabel(
            f"{APP_CODENAME}\nv{APP_VERSION}"
        )

        footer.setObjectName("SidebarFooter")

        footer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(footer)

    def set_active(self, page_id: str):

        for pid, button in self.buttons.items():

            button.setProperty(
                "active",
                pid == page_id
            )

            button.style().unpolish(button)
            button.style().polish(button)