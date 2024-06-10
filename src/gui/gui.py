import sys

from PyQt6.QtWidgets import (
    QApplication,
)

from src.gui.main_window import MainWindow


def show_interface():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
