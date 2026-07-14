from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QTextEdit,
    QVBoxLayout,
)


class ActivityPanel(QFrame):
    """
    Dashboard activity log panel.
    """

    def __init__(self):
        super().__init__()

        self.setObjectName("ActivityPanel")

        layout = QVBoxLayout(self)

        layout.setContentsMargins(15, 15, 15, 15)

        title = QLabel("Recent Activity")
        title.setObjectName("ActivityTitle")

        self.log = QTextEdit()
        self.log.setReadOnly(True)

        layout.addWidget(title)
        layout.addWidget(self.log)

    def add_log(self, message: str):
        self.log.append(message)

    def clear_logs(self):
        self.log.clear()