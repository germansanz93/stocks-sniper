import sys

from PyQt6.QtWidgets import (
    QApplication,
)

from src.gui.main_window import MainWindow
from src.services.morningstar_service import call_morningstar_valuation, call_morningstar_stock_id
from src.services.files_service import assert_directory_existence, create_directory, save_in_file


def show_interface():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


def run_app():
    # show_interface()
    ticker = 'sbux'.lower()
    # container = call_morningstar_valuation(ticker)
    # print(container)
    is_data_present = assert_directory_existence(ticker)
    if not is_data_present:
        dir = create_directory(ticker)
        save_in_file(f'{dir}/{ticker}-search.json', call_morningstar_stock_id(ticker))
        save_in_file(f'{dir}/{ticker}-data.json', call_morningstar_valuation('0P00000546'))