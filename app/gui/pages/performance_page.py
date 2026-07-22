from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QLabel,
)

from app.controllers.performance_controller import PerformanceController
from app.gui.components.performance_chart import PerformanceChart


class PerformancePage(QWidget):
    """
    Live System Performance Page
    """

    def __init__(self):
        super().__init__()

        # ==========================================
        # Controller
        # ==========================================

        self.controller = PerformanceController()

        # ==========================================
        # Main Layout
        # ==========================================

        root = QVBoxLayout(self)

        root.setContentsMargins(20, 20, 20, 20)
        root.setSpacing(20)

        # ==========================================
        # Title
        # ==========================================

        title = QLabel("Performance")
        title.setObjectName("PageTitle")

        subtitle = QLabel(
            "Live CPU, RAM, Disk and Network Monitoring"
        )
        subtitle.setObjectName("PageSubtitle")

        root.addWidget(title)
        root.addWidget(subtitle)

        # ==========================================
        # Charts Grid
        # ==========================================

        grid = QGridLayout()
        grid.setSpacing(20)

        self.cpu_chart = PerformanceChart(
            title="CPU Usage",
            maximum=100,
            history=60,
        )

        self.ram_chart = PerformanceChart(
            title="RAM Usage",
            maximum=100,
            history=60,
        )

        self.disk_chart = PerformanceChart(
            title="Disk Usage",
            maximum=100,
            history=60,
        )

        self.network_chart = PerformanceChart(
            title="Network",
            maximum=100,
            history=60,
        )

        grid.addWidget(self.cpu_chart, 0, 0)
        grid.addWidget(self.ram_chart, 0, 1)
        grid.addWidget(self.disk_chart, 1, 0)
        grid.addWidget(self.network_chart, 1, 1)

        root.addLayout(grid)

        # ==========================================
        # Auto Refresh Timer
        # ==========================================

        self.timer = QTimer(self)

        self.timer.timeout.connect(
            self.refresh_data
        )

        self.timer.start(1000)

        # ==========================================
        # First Refresh
        # ==========================================

        self.refresh_data()

    # =====================================================
    # Refresh Charts
    # =====================================================

    def refresh_data(self):
        """
        Refresh all live performance charts.
        """

        data = self.controller.get_performance_data()

        # CPU
        self.cpu_chart.add_value(
            data["cpu"]
        )

        # RAM
        self.ram_chart.add_value(
            data["ram"]["percent"]
        )

        # Disk
        self.disk_chart.add_value(
            data["disk"]["percent"]
        )

        # Internet (Temporary)
        if data["internet"] == "Online":
            self.network_chart.add_value(100)
        else:
            self.network_chart.add_value(0)