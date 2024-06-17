from PyQt6.QtWidgets import (
    QLineEdit,
    QPushButton,
    QWidget,
    QHBoxLayout,
    QListWidget,
    QVBoxLayout,
    QListWidgetItem
)

from src.services.stock_service import get_stock_info, search_stock
from PyQt6.QtCore import QThread, pyqtSignal


class SearchWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.search_bar = QLineEdit(self)
        self.search_button = QPushButton("Search", self)
        self.results_display = QListWidget(self)

        self.search_button.pressed.connect(self.search)

        self.search_layout = QHBoxLayout()
        self.search_layout.addWidget(self.search_bar)
        self.search_layout.addWidget(self.search_button)

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.search_layout)
        self.main_layout.addWidget(self.results_display)

        self.setLayout(self.main_layout)

    def search(self):
        query = self.search_bar.text()
        print("Search", query)
        self.results_display.clear()
        self.results_display.addItem(f"Searching for: {query}")
        self.thread = SearchThread(query)
        self.thread.result_ready.connect(self.display_results)
        self.thread.start()

    def display_results(self, results):
        self.results_display.clear()
        for result in results:
            item = QListWidgetItem(f"{result['name']} ({result['ticker']}) - {result['exchange']}")
            self.results_display.addItem(item)


class SearchThread(QThread):
    result_ready = pyqtSignal(list)

    def __init__(self, query):
        super().__init__()
        self.query = query

    def run(self):
        results = self.perform_search(self.query)
        self.result_ready.emit(results)

    def perform_search(self, query):
        # Replace the following with the actual implementation of get_stock_info
        return search_stock(query)
