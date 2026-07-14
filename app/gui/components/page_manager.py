from PySide6.QtWidgets import QStackedWidget

from app.gui.navigation import NAV_ITEMS


class PageManager(QStackedWidget):
    def __init__(self):
        super().__init__()

        self.pages = {}

        for item in NAV_ITEMS:
            page = item["page"]()

            self.pages[item["id"]] = page

            self.addWidget(page)

    def show_page(self, page_id: str):
        if page_id in self.pages:
            self.setCurrentWidget(self.pages[page_id])