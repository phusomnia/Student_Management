import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd
import matplotlib.pyplot as plt

from form_TTSV import TTSV
from connect_DB import ConnectDB

class SINHVIEN(QWidget):
    def __init__(self, masv_search):
        super().__init__()

        self.UI = TTSV()
        self.UI.setupUi(self)

        self.DB = ConnectDB()

        self.labels = [self.UI.masventry, self.UI.tensventry, self.UI.ngsinhentry, self.UI.gtinhentry, self.UI.sdtentry,
                       self.UI.dchientry, self.UI.lopentry, self.UI.khoaentry]

        self.bieudo_frame = QVBoxLayout(self.UI.Bieudo)

        self.show_info(masv_search)

        self.create_chart(masv_search)

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
                lop = tuple_item[6]
                khoa = tuple_item[7]

                gender = "Nam" if gioitinh == 1 else "Nữ"

                self.UI.re(str(masv), tensv, ngaysinh.strftime('%d-%m-%Y'), gender, sdt, lop, khoa)

                print("Labels text set successfully.")
        else:
            print("No data found for the provided search criteria.")

    def create_chart(self, masv_search):
        result = self.DB.ketqua(masv_search)
        if result:  # Kiểm tra xem có dữ liệu trả về không
            # Chuyển đổi result thành DataFrame
            df = pd.DataFrame(result, columns=['TENMH', 'DIEMTB_HE10'])
            fig, ax = plt.subplots(figsize=(10, 6))  # Chỉnh kích thước thành (width, height) mong muốn
            # Làm tiếp công việc với DataFrame như bình thường
            monhoc = df['TENMH']
            diem = df['DIEMTB_HE10']

            ax.bar( monhoc, diem, color='skyblue')

            # Đặt tiêu đề và nhãn cho trục x và y
            ax.set_ylabel('Điểm ')
            ax.set_xlabel('Môn học')
            ax.set_title('Biểu đồ điểm của sinh viên')

            # Chuyển đổi biểu đồ thành một đối tượng có thể hiển thị được trong PyQt
            canvas = FigureCanvas(fig)
            self.bieudo_frame.addWidget(canvas)
        else:
            print("Không có dữ liệu nào được trả về từ cơ sở dữ liệu.")


if __name__ == '__main__':
    APP = QApplication(sys.argv)
    WINDOW = SINHVIEN("222010001")
    WINDOW.show()
    sys.exit(APP.exec())
