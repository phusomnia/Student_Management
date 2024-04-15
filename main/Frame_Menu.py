import sys
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QFrame, QMessageBox, QTableWidgetItem
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QIntValidator

from FrontEnd.Form_Menu import Menu
from FrontEnd.Form_QLSV import QLSV

class Window_Menu(QWidget):
    def __init__(self):
        super().__init__()

        self.UI = Menu()
        self.UI.setupMenu(self)
        self.init_signal_slot()

    def init_signal_slot(self):
        self.UI.AdminBtn.clicked.connect(self.Admin_Page)
        self.UI.GVBtn.clicked.connect(self.GV_Page)
    
    def Admin_Page(self):
        self.UI.stackedWidget.setCurrentIndex(0)
    
    def GV_Page(self):
        self.UI.stackedWidget.setCurrentIndex(0)
        
        
if __name__ == '__main__':
    APP  = QApplication(sys.argv)
    WINDOW = Window_Menu()
    WINDOW.show()
    sys.exit(APP.exec())
