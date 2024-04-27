import mysql.connector
import pandas as pd
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
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
        self.Frame_BieuDo = self.UI.Frame_BieuDo
        self.MaMH_TKD = self.UI.MaMH_Entry_TKD
        self.Search_btn = self.UI.SearchBtn_TKD
        self.chonBieudo = self.UI.BieuDo_CBox
        #############################################################################
        self.Search_btn.clicked.connect(self.on_search_button_clicked)
        #############################################################################
        self.UI.ThongKeBtn.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_ThongKeDiem))
        #############################################################################
    def toggleForm(self, Frame, Form):
        Frame.setCurrentIndex(Frame.indexOf(Form))
    ############################################################################
    def on_search_button_clicked(self):
        print("Test button") 
        self.create_chart()
    #############################################################################   
    def create_chart(self):
        mamh = self.MaMH_TKD.text()

        if not self.check_mamh_exists(mamh):
            QMessageBox.warning(self, "Lỗi", "Mã môn học không tồn tại.")
            return

        mydb = self.DB.get_connection()
        mycursor = mydb.cursor()
        query = f"""
        SELECT chitietbangdiem.DIEMTB_HE10
        FROM sinhvien, chitietbangdiem, bangdiem, nhommonhoc
        WHERE sinhvien.MASV = bangdiem.SV
            AND bangdiem.MABD = chitietbangdiem.BD
            AND chitietbangdiem.NHOM = nhommonhoc.MANHOM
            AND nhommonhoc.MH = '{mamh}';
        """
        mycursor.execute(query)
        result = mycursor.fetchall()
        mycursor.close()
        mydb.close()
    #############################################################################
        if not result:
            QMessageBox.information(self, "Thông báo", "Môn học chưa được nhập điểm.")
            return

        df = pd.DataFrame(result, columns=['DIEMTB_HE10'])

        bieudo_option = self.chonBieudo.currentText()
        if bieudo_option == "Tròn":
            chart = self.create_pie_chart(df)
        else:
            chart = self.create_histogram(df)

        self.add_chart_to_frame(chart)
    #############################################################################
    def check_mamh_exists(self, mamh):
        mydb = self.DB.get_connection()
        mycursor = mydb.cursor()
        query = f"SELECT COUNT(*) FROM nhommonhoc WHERE MH = '{mamh}';"
        mycursor.execute(query)
        result = mycursor.fetchone()
        mycursor.close()
        mydb.close()
        return result[0] > 0
    #############################################################################
    def create_histogram(self, df):
        plt.figure(figsize=(8, 4.8))
        ax = plt.subplot()
        sns.histplot(df['DIEMTB_HE10'], ax=ax, color='skyblue', edgecolor='black', kde=True)
        ax.set_title('Biểu đồ Histogram và KDE của Điểm trung bình hệ 10')
        ax.set_xlabel('Điểm trung bình hệ 10')
        ax.set_ylabel('Số lượng sinh viên')
        plt.tight_layout()

        canvas = FigureCanvas(plt.gcf())
        plt.close()
        return canvas
    #############################################################################
    def create_pie_chart(self, df):
        count_gt_4 = (df['DIEMTB_HE10'] > 4).sum()
        count_lt_4 = (df['DIEMTB_HE10'] < 4).sum()

        labels = ['>4', '<4']
        sizes = [count_gt_4, count_lt_4]

        plt.figure(figsize=(6, 6))
        ax = plt.subplot()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        ax.axis('equal')
        ax.set_title('Phân phối điểm trên và dưới 4')
        plt.tight_layout()

        canvas = FigureCanvas(plt.gcf())
        plt.close()
        return canvas
    #############################################################################
    def add_chart_to_frame(self, chart):
        if self.Frame_BieuDo.layout() is not None:
            self.remove_current_chart()       
        layout = self.Frame_BieuDo.layout()
        if self.Frame_BieuDo.layout() is None:
            layout = QVBoxLayout()
            self.Frame_BieuDo.setLayout(layout)
        
        layout.addWidget(chart)
        self.current_chart = chart
    #############################################################################
    def remove_current_chart(self):
        if self.current_chart:
            self.Frame_BieuDo.layout().removeWidget(self.current_chart)
            self.current_chart.deleteLater()
            self.current_chart = None
            
if __name__ == '__main__':
    APP  = QApplication([])
    WINDOW = Window_Menu()
    WINDOW.show()
    APP.exec()