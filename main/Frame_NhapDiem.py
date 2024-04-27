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

        ## NHAP DIEM DATA
        self.MaMon_QLD = self.UI.MaMH_Entry_QLD
        self.MaNhom_QLD = self.UI.MaNhom_Entry_QLD
        self.MaSV_QLD = self.UI.MaSV_Entry_QLD
        self.DiemQT = self.UI.DiemQT_Entry_QLD
        self.DiemQT.setValidator(QDoubleValidator())
        self.HesoQT = self.UI.HSQT_Entry_QLD
        self.HesoQT.setValidator(QDoubleValidator())
        self.DiemThi = self.UI.DiemThi_Entry_QLD
        self.DiemThi.setValidator(QDoubleValidator())
        self.HesoThi = self.UI.HST_Entry_QLD
        self.HesoThi.setValidator(QDoubleValidator())
        self.NamHoc_QLD = self.UI.NamHoc_Cbox_QLD
        self.HocKy_QLD = self.UI.HocKy_CBox_QLD

        ## NHAP DIEM BTN
        self.search_btn_QLD = self.UI.SearchBtn_QLD
        self.update_btn_QLD = self.UI.UpdateBtn_QLD

        ## NHAP DIEM
        self.listbox_QLD = self.UI.tableWidget_QLD
        self.listbox_QLD.setSortingEnabled(False)
        self.buttons_list_QLD = self.UI.Frame_Listbox_QLD.findChildren(QPushButton)

        ## LINK 
        self.search_btn_QLD.clicked.connect(self.search_info_QLD)
        # self.search_btn_QLD.clicked.connect(self.get_info_bangdiem_QLD)
        self.update_btn_QLD.clicked.connect(self.update_info_chitietbangdiem_QLD)
    #############################################################################
        self.UI.ChamDiemBtn.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_NhapDiem))
    #############################################################################
    def toggleForm(self, Frame, Form):
        Frame.setCurrentIndex(Frame.indexOf(Form))
    #############################################################################
    def update_info_chitietbangdiem_QLD(self):
        if self.MaMon_QLD.isEnabled():
            self.select_info_QLD()
        else:
            new_info_ctbd = self.get_nhapdiem_info()
            result_bangdiem = self.get_info_bangdiem_QLD()
            if new_info_ctbd["MAMH"]:
                # Mo rong phuong thuc de tinh diemtb he4, diem chu, xep loai
                diem_qt = float(new_info_ctbd["DIEM_QT"])
                diem_thi = float(new_info_ctbd["DIEMTHI"])
                heso_qt = float(new_info_ctbd["HESO_QT"])
                heso_thi = float(new_info_ctbd["HESO_THI"])
                diemtb_he10 = ((diem_qt*heso_qt) + (diem_thi*heso_thi))
                # Convert diemtb_10 sang diemtb_he4
                if diemtb_he10 >= 8.5 and diemtb_he10 <= 10: 
                    diemtb_he4 = 4 
                    xeploai = 'A'
                elif diemtb_he10 >= 7.0 and diemtb_he10 <= 8.4:
                    diemtb_he4 = 3
                    xeploai = 'B'
                elif diemtb_he10 >= 5.5 and diemtb_he10 <= 6.9:
                    diemtb_he4 = 2
                    xeploai = 'C'
                elif diemtb_he10 >= 4.0 and diemtb_he10 <= 5.4:
                    diemtb_he4 = 1
                    xeploai = 'D'
                else:
                    diemtb_he4 = 0
                    xeploai = 'F'
                #
                for new_info_bd in result_bangdiem:
                    tong_tc_hk = int(new_info_bd["SUM(MH.SOTC)"])
                    tk_he10 = round(float(new_info_bd["SUM(CTBD.DIEMTB_HE10*MH.SOTC)"]) / tong_tc_hk, 2)
                    tk_he4 = float(new_info_bd["SUM(CTBD.DIEMTB_HE4*MH.SOTC)"])/tong_tc_hk
                    print(tong_tc_hk, tk_he10, tk_he4)
                # Kiem diemqt, diemthi la tu 0 den 10 diem
                # va tong he so cac diem la 1.0
                if 0 <= diem_qt <= 10 and 0 <= diem_thi <= 10 and 0 <= heso_qt <= 1.0 and 0 <= heso_thi <= 1.0 and (heso_qt + heso_thi) == 1.0:
                    update_result_ctbd = self.DB.update_info_nhapdiem(
                        new_info_ctbd["MAMH"],
                        new_info_ctbd["MANHOM"],
                        new_info_ctbd["MASV"],
                        diem_qt,
                        heso_qt,
                        diem_thi,
                        heso_thi,
                        diemtb_he10,
                        diemtb_he4,
                        xeploai
                    )

                    update_result_bd = self.DB.update_info_bd_nhapdiem(
                        new_info_ctbd["MASV"],
                        tk_he10,
                        tk_he4
                    )

                    if update_result_ctbd:
                        QMessageBox.information(self, "Cảnh báo", f"Cập nhật: {update_result_ctbd} thất bại!", QMessageBox.StandardButton.Ok)
                    elif update_result_bd:
                        QMessageBox.information(self, "Cảnh báo", f"Cập nhật: {update_result_bd} thất bại!", QMessageBox.StandardButton.Ok)
                    else:
                        self.MaMon_QLD.setEnabled(True)
                        self.MaNhom_QLD.setEnabled(True)
                        self.MaSV_QLD.setEnabled(True)
                        self.search_info_QLD()
                        self.MaMon_QLD.clear()
                        self.MaNhom_QLD.clear()
                        self.MaSV_QLD.clear()
                        self.DiemQT.clear()
                        self.HesoQT.clear()
                        self.DiemThi.clear()
                        self.HesoThi.clear()
                else:
                    QMessageBox.information(self, "Cảnh báo", "Điểm thi và điểm quá trình từ 1-10. Hệ số quá trình vả hệ số thi tổng bằng 1.0", QMessageBox.StandardButton.Ok)
            else:
                QMessageBox.information(self, "Cảnh báo", "Chọn 1 sinh viên để cập nhật điểm", QMessageBox.StandardButton.Ok)
    #############################################################################
    def get_info_bangdiem_QLD(self):
        new_info_ctbd = self.get_nhapdiem_info() 
        result_bangdiem = self.DB.search_info_bd_nhapdiem(new_info_ctbd["MASV"],new_info_ctbd["HOCKY"],new_info_ctbd["NAMHOC"])
        return result_bangdiem
    #############################################################################
    def select_info_QLD(self):
        select_row = self.listbox_QLD.currentRow()
        if select_row != -1:
            self.MaMon_QLD.setEnabled(False)
            self.MaNhom_QLD.setEnabled(False)
            self.MaSV_QLD.setEnabled(False)
            s_MaMon_QLD = self.listbox_QLD.item(select_row, 1).text().strip()
            s_MaNhom_QLD = self.listbox_QLD.item(select_row, 2).text().strip()
            s_MaSV_QLD = self.listbox_QLD.item(select_row, 3).text().strip()
            s_DiemQT_QLD = self.listbox_QLD.item(select_row, 5).text().strip()
            s_HSQT_QLD = self.listbox_QLD.item(select_row, 6).text().strip()
            s_DiemThi_QLD = self.listbox_QLD.item(select_row, 7).text().strip()
            s_HST_QLD = self.listbox_QLD.item(select_row, 8).text().strip()

            self.MaMon_QLD.setText(s_MaMon_QLD)
            self.MaNhom_QLD.setText(s_MaNhom_QLD)
            self.MaSV_QLD.setText(s_MaSV_QLD)
            self.DiemQT.setText(s_DiemQT_QLD)
            self.HesoQT.setText(s_HSQT_QLD)
            self.DiemThi.setText(s_DiemThi_QLD)
            self.HesoThi.setText(s_HST_QLD)
        else:
            QMessageBox.information(self, "Cảnh báo", "Hãy chọn 1 môn", QMessageBox.StandardButton.Ok)
    ##############################################################################
    def search_info_QLD(self):
        nhapdiem_info = self.get_nhapdiem_info()

        search_result = self.DB.search_info_ctdb_nhapdiem(
            mamhtk= nhapdiem_info["MAMH"],
            manhomtk= nhapdiem_info["MANHOM"],
            masvtk= nhapdiem_info["MASV"],
            hockytk= nhapdiem_info["HOCKY"],
            namhoctk= nhapdiem_info["NAMHOC"]
        )

        if search_result:
            self.show_data_QLD(search_result)
        else:
            self.clear_listbox_QLD()
    ############################################################################s
    def clear_listbox_QLD(self):
        self.listbox_QLD.clearContents()
        self.listbox_QLD.setRowCount(0) 
    ############################################################################
    ##  HIEN THI NHAP DIEM
    def show_data_QLD(self, result):
        if result:
            self.listbox_QLD.setRowCount(0)
            self.listbox_QLD.setRowCount(len(result))

            for row, info in enumerate(result):
                nhapdiem_info = [
                    info["MAGV"],
                    info["MAMH"],
                    info["NHOM"],
                    info["MASV"],
                    info["HOTENSV"],
                    info["DIEM_QT"],
                    info["HESO_QT"],
                    info["DIEMTHI"],
                    info["HESO_THI"],
                    info["DIEMTB_HE10"],
                    info["DIEMTB_HE4"],
                    info["DIEMTK_HE10"],
                    info["DIEMTK_HE4"],
                    info["DIEMTB_TL"],
                    info["XEPLOAI"],
                    info["HOCKY"],
                    info["NAMHOC"]
                ]
                for column, item in enumerate(nhapdiem_info):
                    cell_item = QTableWidgetItem(str(item))
                    self.listbox_QLD.setItem(row, column, cell_item)
    #############################################################################
    def display_data_QLD(self):
        ## LAY DU LIEU DE HIEN THI
        search_result = self.DB.search_info_nhapdiem(magvtk="GV01001")

        ## HIEN THI
        self.show_data_QLD(search_result)
    #############################################################################  
    def get_nhapdiem_info(self):
        get_MaMH = self.MaMon_QLD.text().strip()
        get_MaNhom = self.MaNhom_QLD.text().strip()
        get_MaSV = self.MaSV_QLD.text().strip()
        get_DiemQT = self.DiemQT.text().strip()
        get_HSQT = self.HesoQT.text().strip()
        get_DiemThi = self.DiemThi.text().strip()
        get_HST = self.HesoThi.text().strip()
        get_HocKy = self.HocKy_QLD.currentText().strip()
        get_NamHoc = self.NamHoc_QLD.currentText().strip()

        diem_info = {
            "MAMH": get_MaMH,
            "MANHOM": get_MaNhom,
            "MASV": get_MaSV,
            "DIEM_QT": get_DiemQT,
            "HESO_QT":  get_HSQT,
            "DIEMTHI": get_DiemThi,
            "HESO_THI": get_HST,
            "HOCKY": get_HocKy,
            "NAMHOC": get_NamHoc
        }

        return diem_info
    #############################################################################
if __name__ == '__main__':
    APP  = QApplication([])
    WINDOW = Window_Menu()
    WINDOW.show()
    APP.exec()