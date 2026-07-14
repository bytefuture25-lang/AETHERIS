from PySide6.QtWidgets import QWidget, QVBoxLayout

from app.gui.components.welcome_banner import WelcomeBanner
from app.gui.components.status_grid import StatusGrid
from app.gui.components.activity_panel import ActivityPanel


class DashboardPage(QWidget):
    """
    Main Dashboard Page
    """

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        layout.addWidget(WelcomeBanner())
        layout.addWidget(StatusGrid())
        layout.addWidget(ActivityPanel(), 1)