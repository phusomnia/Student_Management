from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit, QLabel
from PyQt6.QtGui import QTextCursor, QTextCharFormat, QColor
import sys

class SearchableTextEdit(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)

        search_layout = QHBoxLayout()
        layout.addLayout(search_layout)

        self.search_input = QLineEdit()
        search_layout.addWidget(self.search_input)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.clear_text)
        search_layout.addWidget(clear_button)

        self.no_matches_label = QLabel("No matches found.")
        self.no_matches_label.hide()
        search_layout.addWidget(self.no_matches_label)

        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search_text)
        search_layout.addWidget(search_button)

    def search_text(self):
        search_text = self.search_input.text().strip()
        if search_text:
            document = self.text_edit.document()
            cursor = QTextCursor(document)

            format_ = QTextCharFormat()
            format_.setBackground(QColor("yellow"))

            # Clear previous highlights
            cursor.movePosition(QTextCursor.MoveOperation.Start)
            cursor.select(QTextCursor.SelectionType.Document)
            cursor.setCharFormat(QTextCharFormat())

            search_words = search_text.split("\n")

            search_results = []

            for word in search_words:
                if word:
                    cursor = document.find(word)
                    while not cursor.isNull():
                        cursor.mergeCharFormat(format_)
                        search_results.append(cursor.selection().toPlainText())
                        cursor = document.find(word, cursor.position() + len(word))

            if search_results:
                self.no_matches_label.hide()
            else:
                # Clear highlights if no matches found
                cursor.movePosition(QTextCursor.MoveOperation.Start)
                cursor.select(QTextCursor.SelectionType.Document)
                cursor.setCharFormat(QTextCharFormat())
                self.no_matches_label.setText("No matches found.")
                self.no_matches_label.show()
        else:
            # If search box is empty, display "No matches found"
            # Clear highlights
            cursor = QTextCursor(self.text_edit.document())
            cursor.movePosition(QTextCursor.MoveOperation.Start)
            cursor.select(QTextCursor.SelectionType.Document)
            cursor.setCharFormat(QTextCharFormat())
            self.no_matches_label.setText("No matches found.")
            self.no_matches_label.show()

    def clear_text(self):
        self.text_edit.clear()
        self.search_input.clear()
        self.no_matches_label.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SearchableTextEdit()
    window.setGeometry(100, 100, 800, 600)
    window.show()
    sys.exit(app.exec())
