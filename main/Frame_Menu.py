from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem, QPushButton, QWidget, QApplication
from PyQt6.QtGui import QIntValidator
from FrontEnd.Form_Menu import Menu

from Backend.Connection_Database import ConnectDB
from Class_QLSV import QLSV

class Window_Menu(QWidget):
    def __init__(self):
        super().__init__()

        self.UI = Menu()
        self.UI.setupMenu(self)
        self.UI.SubFrame_GVBtn_4.setHidden(True)

        self.UI.AdminBtn.clicked.connect(self.toggleSubMenu)

    def toggleSubMenu(self):
        if self.UI.SubFrame_GVBtn_4.isVisible():
            self.UI.SubFrame_GVBtn_4.hide()
        else:
            self.UI.SubFrame_GVBtn_4.show()

        self.init_signal_slot_sidebar()
        
        # self.init_menu = QLSV(self.UI)
    
    def init_signal_slot_sidebar(self):
        self.UI.QLTKBtn.clicked.connect(self.Init_Form)
        self.UI.QLSVBtn.clicked.connect(self.QLSV_Form)
        self.UI.QLGVBtn.clicked.connect(self.QLGV_Form)
    # Khoi tao tra
    def Init_Form(self):
        index = self.UI.Frame_GV.indexOf(self.UI.Frame_Init)
        self.UI.Frame_GV.setCurrentIndex(index)

    def QLSV_Form(self):
        index = self.UI.Frame_GV.indexOf(self.UI.Frame_QLSV)
        self.UI.Frame_GV.setCurrentIndex(index)

    def QLGV_Form(self):
        index = self.UI.Frame_GV.indexOf(self.UI.Frame_QLGV)
        self.UI.Frame_GV.setCurrentIndex(index)


if __name__ == '__main__':
    APP  = QApplication([])
    WINDOW = Window_Menu()
    WINDOW.show()
    APP.exec()
