from PyQt6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QWidget,
)
from src.gui.search_widget import SearchWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stocks Discovery")

        self.main_layout = QVBoxLayout()

        self.search_widget = SearchWidget()

        self.main_layout.addWidget(self.search_widget)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)

        self.setCentralWidget(self.central_widget)
