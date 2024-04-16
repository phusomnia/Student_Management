import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFrame

class ToggleDropdownMenu(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Toggle Dropdown Menu')
        
        self.toggle_button = QPushButton('Toggle Menu')
        self.toggle_button.clicked.connect(self.toggleMenu)
        
        self.dropdown_frame = QFrame()
        self.dropdown_frame.setFrameStyle(QFrame.Shape.Panel | QFrame.Shadow.Raised)
        self.dropdown_frame.setLineWidth(1)  # Adjust the line width as needed

        self.label1 = QLabel('Option 1')
        self.label2 = QLabel('Option 2')
        self.label3 = QLabel('Option 3')
        
        layout_dropdown = QVBoxLayout(self.dropdown_frame)
        layout_dropdown.addWidget(self.label1)
        layout_dropdown.addWidget(self.label2)
        layout_dropdown.addWidget(self.label3)

        self.dropdown_frame.hide()  # Initially hide the dropdown frame
        
        layout = QVBoxLayout()
        layout.addWidget(self.toggle_button)
        layout.addWidget(self.dropdown_frame)
        
        self.setLayout(layout)
        
    def toggleMenu(self):
        if self.dropdown_frame.isVisible():
            self.dropdown_frame.hide()
        else:
            self.dropdown_frame.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ToggleDropdownMenu()
    ex.show()
    sys.exit(app.exec())
