from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
)

from app.controllers.dashboard_controller import DashboardController

from app.gui.components.welcome_banner import WelcomeBanner
from app.gui.components.status_grid import StatusGrid
from app.gui.components.activity_panel import ActivityPanel
from app.gui.components.performance_chart import PerformanceChart


class DashboardPage(QWidget):
    """
    Main Dashboard Page
    """

    def __init__(self):
        super().__init__()

        # ==========================================
        # Controller
        # ==========================================

        self.controller = DashboardController()

        # ==========================================
        # Components
        # ==========================================

        self.status_grid = StatusGrid()

        self.activity_panel = ActivityPanel()

        self.cpu_chart = PerformanceChart(
            title="CPU Usage",
            maximum=100,
            history=60,
        )

        # ==========================================
        # Main Layout
        # ==========================================

        layout = QVBoxLayout(self)

        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        layout.addWidget(WelcomeBanner())

        layout.addWidget(self.status_grid)

        # ==========================================
        # Bottom Layout
        # ==========================================

        bottom_layout = QHBoxLayout()

        bottom_layout.setSpacing(20)

        bottom_layout.addWidget(
            self.activity_panel,
            1,
        )

        bottom_layout.addWidget(
            self.cpu_chart,
            1,
        )

        layout.addLayout(bottom_layout, 1)

        # ==========================================
        # Timer
        # ==========================================

        self.timer = QTimer(self)

        self.timer.timeout.connect(
            self.refresh_dashboard
        )

        self.timer.start(2000)

        # ==========================================
        # Initial Logs
        # ==========================================

        self.activity_panel.add_log(
            "Dashboard Started"
        )

        self.activity_panel.add_log(
            "System Monitor Ready"
        )

        # ==========================================
        # First Refresh
        # ==========================================

        self.refresh_dashboard()

    def refresh_dashboard(self):
        """
        Refresh dashboard with live system information.
        """

        data = self.controller.get_dashboard_data()

        # ==========================================
        # CPU
        # ==========================================

        cpu_card = self.status_grid.get_card("CPU")

        if cpu_card:

            cpu_card.update(
                value=f"{data['cpu']} %",
                status="Live",
            )

            self.cpu_chart.add_value(
                data["cpu"]
            )

        # ==========================================
        # RAM
        # ==========================================

        ram_card = self.status_grid.get_card("RAM")

        if ram_card:

            ram = data["ram"]

            ram_card.update(
                value=f"{ram['used_gb']} / {ram['total_gb']} GB",
                status=f"{ram['percent']} % Used",
            )

        # ==========================================
        # Internet
        # ==========================================

        internet_card = self.status_grid.get_card(
            "Internet"
        )

        if internet_card:

            internet = data["internet"]

            if internet == "Online":

                internet_card.update(
                    value="🟢 Online",
                    status="Connected",
                )

            else:

                internet_card.update(
                    value="🔴 Offline",
                    status="No Connection",
                    status_color="#EF4444",
                )