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
        self.Frame_BieuDo_TTSV = self.UI.Frame_BieuDo_TTSV
        #############################################################################
        self.show_info("222010002")
        #############################################################################
        self.create_chart("222010002")
    ############################################################################# 
    def toggleForm(self, Frame, Form):
        Frame.setCurrentIndex(Frame.indexOf(Form)) 
    #############################################################################
    def show_info(self, masv_search):
        search_result = self.DB.info_acc_sv(masv_search)
        if search_result:
            print("Search result:", search_result)
            for sv_info in search_result:
                masv = sv_info['MASV']
                tensv = sv_info['HOTENSV']
                ngaysinh = sv_info['NGSINH']
                gioitinh = sv_info['GTINH']
                sdt = sv_info['SDT']
                diachi = sv_info['DCHI']
                lop = sv_info['LOP']
                khoa = sv_info['TENKHOA']
                khoahoc = sv_info['KHOAHOC']
                hedaotao = sv_info['HEDAOTAO']

                self.display_info_sv(str(masv), tensv, ngaysinh.strftime('%d-%m-%Y'), gioitinh, diachi, sdt, lop, khoa, khoahoc, hedaotao)
        else:
            print("No data found for the provided search criteria.")
    #############################################################################
    def display_info_sv(self, id, name, date, gtinh, diachi ,sdt, lop, khoa, khoahoc, hedaotao):
        self.UI.MaSV_Entry_TTSV.setText(id)
        self.UI.Hoten_Entry_TTSV.setText(name)
        self.UI.NgSinh_Entry_TTSV.setText(date)
        self.UI.Gtinh_Entry_TTSV.setText(gtinh)
        self.UI.DiaChi_Entry_TTSV.setText(diachi)
        self.UI.Sdt_Entry_TTSV.setText(sdt)
        self.UI.Lop_Entry_TTSV.setText(lop)
        self.UI.Khoa_Entry_TTSV.setText(khoa)
        self.UI.KhoaHK_Entry_TTSV.setText(khoahoc)
        self.UI.HDT_Entry_TTSV.setText(hedaotao)
        print("Labels text set successfully.")
    #############################################################################
    def create_chart(self, masv_search):
        result = self.DB.ketqua(masv_search)
        if result:
            df = pd.DataFrame(result, columns=['TENMH', 'DIEMTB_HE10'])
            fig, ax = plt.subplots(figsize=(10, 6))
            monhoc = df['TENMH']
            diem = df['DIEMTB_HE10']

            ax.bar( monhoc, diem, color='skyblue')

            ax.set_ylabel('Điểm')
            ax.set_xlabel('Môn học')
            ax.set_title('Biểu đồ điểm của sinh viên')

            canvas = FigureCanvas(fig)
            self.Frame_BieuDo_TTSV.addWidget(canvas)
        else:
            print("Không có dữ liệu nào được trả về từ cơ sở dữ liệu.")
    
if __name__ == '__main__':
    APP  = QApplication([])
    WINDOW = Window_Menu()
    WINDOW.show()
    APP.exec()
