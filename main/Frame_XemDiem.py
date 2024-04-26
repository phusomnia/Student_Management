from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem, QPushButton, QWidget, QApplication
from PyQt6.QtCore import QDate
from PyQt6.QtGui import QIntValidator, QDoubleValidator
from FrontEnd.Form_Menu import Menu
from Backend.Connection_Database import ConnectDB

class Window_Menu(QWidget):
    def __init__(self):
        super().__init__()

        self.UI = Menu()
        self.UI.setupMenu(self)
        
        self.DB = ConnectDB()
        #############################################################################
        self.Hocky_BD = self.UI.Hocky_Cbox_BD 
        self.Namhoc_BD = self.UI.NamHoc_Cbox_BD
        #############################################################################
        self.listbox_BangDiem = self.UI.tableWidget_BD
        self.listbox_BangDiem.setSortingEnabled(False)
        self.buttons_list_BangDiem = self.UI.Frame_Listbox_BD.findChildren(QPushButton)
        #############################################################################
        self.display_data_BD()
        #############################################################################
        self.UI.XemDiemBtn.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_BangDiem))
    #############################################################################
    def toggleForm(self, Frame, Form):
        Frame.setCurrentIndex(Frame.indexOf(Form))
    #############################################################################
    def show_data_BD(self, result):
        if result:
            self.listbox_QLSV.setRowCount(0)
            self.listbox_QLSV.setRowCount(len(result))

            for row, info in enumerate(result):
                info_list = [
                    info["MASV"],
                    info["HOTEN"],
                    info["NGSINH"],
                    info["GTINH"],
                    info["DCHI"],
                    info["SDT"],
                    info["LOP"]
                ]

                for column, item in enumerate(info_list):
                    cell_item = QTableWidgetItem(str(item))
                    self.listbox_QLSV.setItem(row, column, cell_item)
    #############################################################################
    def display_data_BD(self):
        search_result = self.DB.search_info_bangdiem()

        self.show_data_BD(search_result)
if __name__ == '__main__':
    APP  = QApplication([])
    WINDOW = Window_Menu()
    WINDOW.show()
    APP.exec()