from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, QDialog, QLabel

class GradeDetailsDialog(QDialog):
    def __init__(self, grade, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Grade Details")
        layout = QVBoxLayout()
        self.label = QLabel(f"Grade: {grade}")
        layout.addWidget(self.label)
        self.setLayout(layout)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)  # Two columns: grade and details button
        self.table_widget.setHorizontalHeaderLabels(["Grade", "Details"])
        
        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        self.setLayout(layout)
        
        self.populate_table()

    def show_details(self):
        button = self.sender()
        if button:
            row = self.table_widget.indexAt(button.pos()).row()
            if row >= 0:
                grade = self.table_widget.item(row, 0).text()
                dialog = GradeDetailsDialog(grade, self)
                dialog.exec_()

    def populate_table(self):
        # Example data, replace with your actual data
        grade_data = [
            {"grade": "A", "details": ""},
            {"grade": "B", "details": ""},
            {"grade": "C", "details": ""},
            {"grade": "D", "details": ""},
            {"grade": "F", "details": ""},
        ]
        
        self.table_widget.setRowCount(len(grade_data))
        for row, data in enumerate(grade_data):
            grade_item = QTableWidgetItem(data["grade"])
            self.table_widget.setItem(row, 0, grade_item)
            
            details_button = QPushButton("Show Details")
            details_button.clicked.connect(self.show_details)
            self.table_widget.setCellWidget(row, 1, details_button)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
