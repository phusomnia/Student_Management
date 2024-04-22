import mysql.connector
import pandas as pd
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import seaborn as sns
from FrontEnd.Form_Menu import Menu

class ConnectDB:
    @staticmethod
    def get_connection():
        return mysql.connector.connect(
            host='localhost',
            user='root',
            database='dulieu'
        )

class Window_Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.UI = Menu()
        self.UI.setupMenu(self)

        self.MaMH_TKD = self.UI.MaMH_Entry_TKD
        self.Search_btn = self.UI.SearchBtn_TKD
        self.chonBieudo = self.UI.BieuDo_CBox

        self.Search_btn.clicked.connect(self.on_search_button_clicked)

    def on_search_button_clicked(self):
        print("Test button") 
        self.create_chart()
    def create_chart(self):
        mamh = self.MaMH_TKD.text()

        if not self.check_mamh_exists(mamh):
            QMessageBox.warning(self, "Lỗi", "Mã môn học không tồn tại.")
            return

        mydb = ConnectDB.get_connection()
        mycursor = mydb.cursor()
        query = f"""
        SELECT chitietbangdiem.DIEMTB_HE10
        FROM sinhvien, chitietbangdiem, bangdiem, nhommonhoc
        WHERE sinhvien.MASV = bangdiem.MASV
            AND bangdiem.MABD = chitietbangdiem.BD
            AND chitietbangdiem.MANHOM = nhommonhoc.MANHOM
            AND nhommonhoc.MH = '{mamh}';
        """
        mycursor.execute(query)
        result = mycursor.fetchall()
        mycursor.close()
        mydb.close()

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
    
    def check_mamh_exists(self, mamh):
        mydb = ConnectDB.get_connection()
        mycursor = mydb.cursor()
        query = f"SELECT COUNT(*) FROM nhommonhoc WHERE MH = '{mamh}';"
        mycursor.execute(query)
        result = mycursor.fetchone()
        mycursor.close()
        mydb.close()
        return result[0] > 0
    
    
if __name__ == '__main__':
    APP  = QApplication([])
    WINDOW = Window_Menu()
    WINDOW.show()
    APP.exec()