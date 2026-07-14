from PySide6.QtWidgets import (
    QHBoxLayout,
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

from app.gui.components.header import Header
from app.gui.components.sidebar import Sidebar
from app.gui.components.page_manager import PageManager


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(WINDOW_TITLE)
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setStyleSheet(STYLE_SHEET)

        self._build_ui()

    def _build_ui(self):

        central = QWidget()

        root_layout = QVBoxLayout(central)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        # Header
        self.header = Header()

        # Body
        body = QWidget()

        body_layout = QHBoxLayout(body)
        body_layout.setContentsMargins(0, 0, 0, 0)
        body_layout.setSpacing(0)

        # Sidebar
        self.sidebar = Sidebar()

        # Page Manager
        self.page_manager = PageManager()

        body_layout.addWidget(self.sidebar)
        body_layout.addWidget(self.page_manager, 1)

        root_layout.addWidget(self.header)
        root_layout.addWidget(body)

        self.setCentralWidget(central)

        # Status Bar
        status_bar = QStatusBar()
        status_bar.showMessage("ÆTHERIS Ready")
        self.setStatusBar(status_bar)

        # Connect Navigation
        self.sidebar.page_selected.connect(self.change_page)

        # Default Page
        self.change_page("dashboard")

    def change_page(self, page_id: str):

        self.page_manager.show_page(page_id)

        self.sidebar.set_active(page_id)
        
