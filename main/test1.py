import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from  Backend.Connection_Database import ConnectDB  # Import your ConnectDB class from your module

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt MySQL Example")
        self.layout = QVBoxLayout()

        # Connect to the database
        self.db = ConnectDB()

        # Button to perform a function
        self.btn_search_info = QPushButton("Search Information")
        self.btn_search_info.clicked.connect(self.search_info)
        self.layout.addWidget(self.btn_search_info)

        # Label to display the result
        self.lbl_result = QLabel()
        self.layout.addWidget(self.lbl_result)

        self.setLayout(self.layout)

    def search_info(self):
        # Perform the search operation using the database connection
        result = self.db.search_info_sv(masvtk="12345")  # Example search operation
        if isinstance(result, list):
            # Display the result in the label
            self.lbl_result.setText(str(result))
        else:
            # Display the error message if there's an exception
            self.lbl_result.setText("Error: " + str(result))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
