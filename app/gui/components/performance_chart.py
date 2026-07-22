from collections import deque

from PySide6.QtCharts import (
    QChart,
    QChartView,
    QLineSeries,
    QValueAxis,
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QFrame, QVBoxLayout


class PerformanceChart(QFrame):
    """
    Reusable live performance chart.
    """

    def __init__(
        self,
        title: str = "Performance",
        maximum: int = 100,
        history: int = 60,
    ):
        super().__init__()

        self.setObjectName("PerformanceChart")

        self.maximum = maximum
        self.history = history

        self.values = deque(
            [0] * history,
            maxlen=history,
        )

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)

        # --------------------------
        # Series
        # --------------------------

        self.series = QLineSeries()

        # --------------------------
        # Chart
        # --------------------------

        self.chart = QChart()
        self.chart.setTitle(title)
        self.chart.legend().hide()

        self.chart.addSeries(self.series)

        self.chart.setBackgroundVisible(False)
        self.chart.setPlotAreaBackgroundVisible(False)

        # --------------------------
        # X Axis
        # --------------------------

        self.axis_x = QValueAxis()
        self.axis_x.setRange(0, history)

        # --------------------------
        # Y Axis
        # --------------------------

        self.axis_y = QValueAxis()
        self.axis_y.setRange(0, maximum)

        self.chart.addAxis(
            self.axis_x,
            Qt.AlignmentFlag.AlignBottom,
        )

        self.chart.addAxis(
            self.axis_y,
            Qt.AlignmentFlag.AlignLeft,
        )

        self.series.attachAxis(self.axis_x)
        self.series.attachAxis(self.axis_y)

        # --------------------------
        # View
        # --------------------------

        self.view = QChartView(self.chart)

        self.view.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        layout.addWidget(self.view)

        self.refresh()

    def refresh(self):
        """
        Redraw chart.
        """

        self.series.clear()

        for index, value in enumerate(self.values):
            self.series.append(index, value)

    def add_value(
        self,
        value: float,
    ):
        """
        Add a new value.
        """

        self.values.append(value)

        self.refresh()