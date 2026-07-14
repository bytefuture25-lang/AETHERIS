from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QStatusBar,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)

from app.gui.theme import (
    STYLE_SHEET,
    WINDOW_HEIGHT,
    WINDOW_TITLE,
    WINDOW_WIDTH,
)

from app.gui.components.header import Header
from app.gui.components.sidebar import Sidebar
from app.gui.components.content import Content


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(WINDOW_TITLE)
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setStyleSheet(STYLE_SHEET)

        self._build_ui()

    def _build_ui(self):
        central = QWidget()

        root_layout = QVBoxLayout()
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        header = Header()

        body = QWidget()

        body_layout = QHBoxLayout(body)
        body_layout.setContentsMargins(0, 0, 0, 0)
        body_layout.setSpacing(0)

        body_layout.addWidget(Sidebar())
        body_layout.addWidget(Content(), 1)

        root_layout.addWidget(header)
        root_layout.addWidget(body)

        central.setLayout(root_layout)

        self.setCentralWidget(central)

        status_bar = QStatusBar()
        status_bar.showMessage("ÆTHERIS Ready")
        self.setStatusBar(status_bar)