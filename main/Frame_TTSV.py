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
        self.UI.TTSVBtn.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_TTSV))
        #############################################################################
        self.labels = [self.UI.MaSV_Entry_TTSV, self.UI.Hoten_Entry_TTSV, self.UI.NgSinh_Entry_TTSV, self.UI.Gtinh_Entry_TTSV, self.UI.Sdt_Entry_TTSV,
                       self.UI.DiaChi_Entry_TTSV, self.UI.Lop_Entry_TTSV, self.UI.Khoa_Entry_TTSV]
        
        self.bieudo_frame = self.UI.Frame_BieuDo_TTSV

        self.show_info('222010001')

        self.create_chart('222010001')
    ############################################################################# 
    def toggleForm(self, Frame, Form):
        Frame.setCurrentIndex(Frame.indexOf(Form)) 
    #############################################################################
    def show_info(self, masv_search):
        search_result = self.DB.info_acc_sv(masv_search)
        if search_result:


            print("Search result:", search_result)
            for tuple_item in search_result:
                masv = tuple_item[0]
                tensv = tuple_item[1]
                ngaysinh = tuple_item[2]
                gioitinh = tuple_item[3]
                sdt = tuple_item[4]
                diachi = tuple_item[5]
                lop = tuple_item[6]
                khoa = tuple_item[7]

                gender = "Nam" if gioitinh == 1 else "Nữ"

                self.re(str(masv), tensv, ngaysinh.strftime('%d-%m-%Y'), gender, diachi, sdt, lop, khoa)

                print("Labels text set successfully.")
        else:
            print("No data found for the provided search criteria.")
    #############################################################################
    def re(self, id, name, date, gender, diachi ,sdt, lop, khoa):
        self.UI.MaSV_Entry_TTSV.setText(id)
        self.UI.Hoten_Entry_TTSV.setText(name)
        self.UI.NgSinh_Entry_TTSV.setText(date)
        self.UI.Gtinh_Entry_TTSV.setText(gender)
        self.UI.DiaChi_Entry_TTSV.setText(diachi)
        self.UI.Sdt_Entry_TTSV.setText(sdt)
        self.UI.Lop_Entry_TTSV.setText(lop)
        self.UI.Khoa_Entry_TTSV.setText(khoa)
    #############################################################################
    def create_chart(self, masv_search):
        result = self.DB.ketqua(masv_search)
        df = pd.DataFrame(result, columns=['DIEMTB_HE10'])
        chart = self.create_histogram(df)
        self.add_chart_to_frame(chart)
    #############################################################################
    def create_histogram(self, df):
        fig, ax = plt.subplots(figsize=(7, 2.6))
        sns.histplot(df['DIEMTB_HE10'], ax=ax, color='darkblue', edgecolor='black', kde=True)
        ax.set_title('')
        ax.set_ylabel('Điểm trung bình hệ 10')
        ax.set_xlabel('Số lượng môn học')
        plt.tight_layout()
        canvas = FigureCanvas(fig)
        plt.close()
        return canvas
    #############################################################################
    def add_chart_to_frame(self, chart):
        self.bieudo_frame.addWidget(chart)

if __name__ == '__main__':
    APP  = QApplication([])
    WINDOW = Window_Menu()
    WINDOW.show()
    APP.exec()
