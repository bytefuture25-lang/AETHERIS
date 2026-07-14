from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
)

from app.gui.components.status_card import StatusCard


class StatusGrid(QFrame):
    """
    Dashboard status card grid.
    """

    def __init__(self):
        super().__init__()

        self.setObjectName("StatusGrid")

        layout = QGridLayout(self)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setHorizontalSpacing(15)
        layout.setVerticalSpacing(15)

        cards = [

            ("Claude", "Offline", "Disconnected"),

            ("ChatGPT", "Offline", "Disconnected"),

            ("Ollama", "Ready", "Connected"),

            ("Gemini", "Offline", "Disconnected"),

            ("CPU", "-- %", "Idle"),

            ("RAM", "-- GB", "Waiting"),

            ("Internet", "Unknown", "Checking"),

            ("Voice", "Disabled", "Idle"),
        ]

        row = 0
        col = 0

        for title, value, status in cards:

            card = StatusCard(
                title,
                value,
                status,
            )

            layout.addWidget(card, row, col)

            col += 1

            if col == 4:
                col = 0
                row += 1