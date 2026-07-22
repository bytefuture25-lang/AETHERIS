from datetime import datetime

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class LiveClock(QWidget):
    """
    Live date & time widget.
    """

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(1)

        self.time_label = QLabel()
        self.time_label.setObjectName("ClockTime")

        self.date_label = QLabel()
        self.date_label.setObjectName("ClockDate")

        layout.addWidget(self.time_label)
        layout.addWidget(self.date_label)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)

        self.update_clock()

    def update_clock(self):
        now = datetime.now()

        self.time_label.setText(
            now.strftime("%I:%M:%S %p")
        )

        self.date_label.setText(
            now.strftime("%A, %d %B %Y")
        )