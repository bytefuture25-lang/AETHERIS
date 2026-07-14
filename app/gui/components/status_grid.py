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

        # Store references to every StatusCard
        self.cards = {}

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

            # Save the card so we can update it later
            self.cards[title] = card

            layout.addWidget(card, row, col)

            col += 1

            if col == 4:
                col = 0
                row += 1

    def get_card(self, name: str):
        """
        Return a StatusCard by its title.
        Example:
            cpu = self.get_card("CPU")
        """
        return self.cards.get(name)