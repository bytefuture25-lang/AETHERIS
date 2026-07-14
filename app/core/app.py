import sys

from PySide6.QtWidgets import QApplication

from app.gui.window import MainWindow


class Application:

    def __init__(self):
        self.qt_app = QApplication(sys.argv)

        self.window = MainWindow()

    def run(self):
        self.window.show()

        return self.qt_app.exec()