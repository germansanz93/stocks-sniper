from PyQt6.QtWidgets import (
    QLineEdit,
    QPushButton,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem,
)

from src.services.stock_service import get_stock_info, search_stock
from PyQt6.QtCore import QThread, pyqtSignal


class SearchWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.search_bar = QLineEdit(self)
        self.search_button = QPushButton("Search", self)
        self.results_display = QTableWidget(self)

        self.results_display.cellClicked.connect(self.row_click)

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
        self.results_display.setColumnCount(1)
        self.results_display.setRowCount(0)
        self.results_display.insertRow(0)
        self.results_display.setItem(0, 0, QTableWidgetItem(f"Searching for: {query}"))
        self.thread = SearchThread(query)
        self.thread.result_ready.connect(self.display_results)
        self.thread.start()

    def display_results(self, results):
        self.results_display.setColumnCount(3)
        self.results_display.setHorizontalHeaderLabels(["Name", "Ticker", "Exchange"])
        self.results_display.setRowCount(len(results))
        for row_index, result in enumerate(results):
            self.results_display.setItem(row_index, 0, QTableWidgetItem(result['name']))
            self.results_display.setItem(row_index, 1, QTableWidgetItem(result['ticker']))
            self.results_display.setItem(row_index, 2, QTableWidgetItem(result['exchange']))

            # Adjust column widths after populating the table
        small_cols_width = int(0.2 * self.results_display.width())
        self.results_display.setColumnWidth(1, small_cols_width)
        self.results_display.setColumnWidth(2, small_cols_width)
        self.results_display.setColumnWidth(0, self.results_display.width() - 2 * small_cols_width)

    def row_click(self, row, column):
        name = self.results_display.item(row, 0).text()
        ticker = self.results_display.item(row, 1).text()
        exchange = self.results_display.item(row, 2).text()
        print(f"Row {row} clicked: {name} ({ticker}) - {exchange}")
        self.thread = GetStockInfoThread(exchange, ticker)
        self.thread.result_ready.connect(self.display_stock_info)
        self.thread.start()

    def display_stock_info(self, stock_info):
        # Display the stock_info in the way you want
        print(stock_info)

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

class GetStockInfoThread(QThread):
    result_ready = pyqtSignal(dict)

    def __init__(self, exchange, ticker):
        super().__init__()
        self.ticker = ticker
        self.exchange = exchange

    def run(self):
        stock_info = get_stock_info(self.exchange, self.ticker)
        self.result_ready.emit(stock_info)