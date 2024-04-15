from PyQt6.QtWidgets import QWidget, QApplication
from FrontEnd.Form_Menu import Menu_Form
from Class_QLSV import QLSV

class Window_Menu(QWidget):
    def __init__(self):
        super().__init__()

        self.UI = Menu_Form()
        self.UI.setupMenu(self)
        self.init_signal_slot_sidebar()

        # Initialize the QLSV class
        self.init_menu = QLSV(self.UI)

    def init_signal_slot_sidebar(self):
        self.UI.QLHPBtn.clicked.connect(self.Init_Page)
        self.UI.QLSVBtn.clicked.connect(self.Admin_Page)
    
    def Init_Page(self):
        indexFrame_Init = self.UI.Frame_GV.indexOf(self.UI.Frame_Init)
        self.UI.Frame_GV.setCurrentIndex(indexFrame_Init)

    def Admin_Page(self):
        indexFrame_QLSV = self.UI.Frame_GV.indexOf(self.UI.Frame_QLSV)
        self.UI.Frame_GV.setCurrentIndex(indexFrame_QLSV)


if __name__ == '__main__':
    APP  = QApplication([])
    WINDOW = Window_Menu()
    WINDOW.show()
    APP.exec()
