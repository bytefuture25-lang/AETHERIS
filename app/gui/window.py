from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)

from app.gui.theme import (
    STYLE_SHEET,
    WINDOW_HEIGHT,
    WINDOW_TITLE,
    WINDOW_WIDTH,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(WINDOW_TITLE)
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.setStyleSheet(STYLE_SHEET)

        self._build_ui()

    def _build_ui(self):
        central = QWidget()

        layout = QVBoxLayout()

        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title = QLabel("ÆTHERIS")

        title.setStyleSheet("""
            font-size:32px;
            font-weight:bold;
        """)

        subtitle = QLabel(
            "Personal AI Operating Intelligence"
        )

        version = QLabel("Version 0.1 • Genesis")

        status = QLabel("System Status : Ready")

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(20)
        layout.addWidget(version)
        layout.addWidget(status)

        central.setLayout(layout)

        self.setCentralWidget(central)

        statusbar = QStatusBar()

        statusbar.showMessage("Ready")

        self.setStatusBar(statusbar)