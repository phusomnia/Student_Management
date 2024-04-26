import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import seaborn as sns
from FrontEnd.Form_Menu import Menu
from Backend.Connection_Database import ConnectDB

class Window_Menu(QWidget):
    def __init__(self):
        super().__init__()

        self.UI = Menu()
        self.UI.setupMenu(self)
        
        self.DB = ConnectDB()
        #############################################################################
        self.UI.TTGVBtn.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_TTGV))
        #############################################################################
        self.show_gv_info("GV01001")
    #############################################################################
    def toggleForm(self, Frame, Form):
        Frame.setCurrentIndex(Frame.indexOf(Form))
    #############################################################################
    def show_gv_info(self, magv_search):
        search_result = self.DB.search_acc_gv(magv_search)

        if search_result:
            print(search_result)
            for gv_info in search_result:
                magv = gv_info['MAGV']
                tengv = gv_info['HOTEN']
                ngaysinh = gv_info['NGSINH']
                gioitinh = gv_info['GTINH']
                # khoa = gv_info['KHOA']
                tenkhoa = gv_info['TENKHOA']

            self.display_info_sv(magv, tengv, ngaysinh.strftime('%d-%m-%Y'), gioitinh, tenkhoa)
        else:
            print("No data found for the provided search criteria.")
    #############################################################################
    def display_info_sv(self, magv, tengv, ngaysinh, gioitinh, tenkhoa):
        self.UI.MaGV_Entry_TTGV.setText(magv)
        self.UI.Hoten_Entry_TTGV.setText(tengv)
        self.UI.Ngsinh_Entry_TTGV.setText(ngaysinh)
        self.UI.Gtinh_Entry_TTGV.setText(gioitinh)
        # ma_ten_khoa = f"{khoa} - {tenkhoa}"
        # self.UI.Khoa_Entry_TTGV.setText(ma_ten_khoa)
        self.UI.Khoa_Entry_TTGV.setText(tenkhoa)

        if self.DB.check_truongkhoa(magv):
            chucvu = "Trưởng Khoa"
            self.UI.Chuc_Vu_TTGV.setText(chucvu)
        else:
            chucvu = "Giảng viên"
            self.UI.Chuc_Vu_TTGV.setText(chucvu)
        
if __name__ == '__main__':
    APP  = QApplication([])
    WINDOW = Window_Menu()
    WINDOW.show()
    APP.exec()
