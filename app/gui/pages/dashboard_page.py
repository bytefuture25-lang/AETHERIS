from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QWidget, QVBoxLayout

from app.controllers.dashboard_controller import DashboardController
from app.gui.components.activity_panel import ActivityPanel
from app.gui.components.status_grid import StatusGrid
from app.gui.components.welcome_banner import WelcomeBanner


class DashboardPage(QWidget):
    """
    Main Dashboard Page
    """

    def __init__(self):
        super().__init__()

        # Controller
        self.controller = DashboardController()

        # Components
        self.status_grid = StatusGrid()

        # Layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        layout.addWidget(WelcomeBanner())
        layout.addWidget(self.status_grid)
        layout.addWidget(ActivityPanel(), 1)

        # Auto Refresh Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh_dashboard)
        self.timer.start(2000)

        # First Update
        self.refresh_dashboard()

    def refresh_dashboard(self):
        """
        Refresh dashboard with live system information.
        """

        data = self.controller.get_dashboard_data()

        # -----------------------
        # CPU
        # -----------------------

        cpu_card = self.status_grid.get_card("CPU")

        if cpu_card:
            cpu_card.update(
                value=f"{data['cpu']} %",
                status="Live"
            )

        # -----------------------
        # RAM
        # -----------------------

        ram_card = self.status_grid.get_card("RAM")

        if ram_card:
            ram = data["ram"]

            ram_card.update(
                value=f"{ram['used_gb']} / {ram['total_gb']} GB",
                status=f"{ram['percent']} % Used"
            )

        # -----------------------
        # Disk
        # -----------------------

        disk_card = self.status_grid.get_card("Internet")

        if disk_card:
            disk = data["disk"]

            disk_card.update(
                value=f"{disk['percent']} %",
                status="Disk Usage"
            )