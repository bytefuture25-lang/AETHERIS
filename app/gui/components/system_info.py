from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QGridLayout,
)


class SystemInfo(QFrame):
    """
    Displays basic system information.
    """

    def __init__(self):
        super().__init__()

        self.setObjectName("SystemInfo")

        layout = QGridLayout(self)

        layout.setContentsMargins(20, 20, 20, 20)
        layout.setHorizontalSpacing(20)
        layout.setVerticalSpacing(10)

        title = QLabel("💻 System Information")
        title.setObjectName("SystemInfoTitle")

        layout.addWidget(title, 0, 0, 1, 2)

        self.hostname = QLabel("--")
        self.os = QLabel("--")
        self.python = QLabel("--")
        self.processor = QLabel("--")
        self.internet = QLabel("--")

        rows = [
            ("Hostname", self.hostname),
            ("OS", self.os),
            ("Python", self.python),
            ("Processor", self.processor),
            ("Internet", self.internet),
        ]

        row = 1

        for label, widget in rows:

            left = QLabel(label)
            left.setObjectName("InfoLabel")

            widget.setObjectName("InfoValue")

            layout.addWidget(left, row, 0)
            layout.addWidget(widget, row, 1)

            row += 1

    def update_info(self, data: dict):
        """
        Update system information.
        """

        self.hostname.setText(data["hostname"])
        self.os.setText(data["os"])
        self.python.setText(data["python"])
        self.processor.setText(data["processor"])
        self.internet.setText(data["internet"])