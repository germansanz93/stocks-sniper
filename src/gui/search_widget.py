from PyQt6.QtWidgets import (
    QLineEdit,
    QPushButton,
    QWidget,
    QHBoxLayout
)


class SearchWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.search_bar = QLineEdit(self)
        self.search_button = QPushButton("Search", self)
        self.search_layout = QHBoxLayout()

        self.search_button.pressed.connect(self.search)

        self.search_layout.addWidget(self.search_bar)
        self.search_layout.addWidget(self.search_button)

        self.setLayout(self.search_layout)

    def search(self):
        print("Search", self.search_bar.text())
