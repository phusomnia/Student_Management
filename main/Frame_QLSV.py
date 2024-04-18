import sys
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QFrame, QMessageBox, QTableWidgetItem
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QIntValidator

from FrontEnd.Form_QLSV import QLSV
from Backend.Connection_Database import ConnectDB

class Window_QLSV(QWidget):
    def __init__(self):
        super().__init__()

        self.UI = QLSV()
        self.UI.setupQLSV(self)

        self.DB = ConnectDB()

        self.Masv = self.UI.MSSVEntry
        self.Masv.setValidator(QIntValidator())

        self.Hoten = self.UI.TenEntry
        self.Lop = self.UI.LopEntry
        self.Ngsinh = self.UI.NgsinhEntry
        self.GTinh = self.UI.ComboboxGtinh
        self.Sdt = self.UI.SDTEntry

        self.add_btn = self.UI.AddBtn
        self.update_btn = self.UI.UpdateBtn
        self.delete_btn = self.UI.DelBtn
        self.search_btn = self.UI.ExitBtn

        self.listbox_table = self.UI.tableWidget
        self.listbox_table.setSortingEnabled(False)
        self.buttons_list = self.UI.function_frame.findChildren(QPushButton)

        # Khoi tao cac chuc nang
        self.init_signal_slot()

        # Khoi tao hien thi du lieu dang co trong database
        # self.search_info()
        self.display_data()
    
    # Lien ket cac button voi cac ham chuc nang
    def init_signal_slot(self):
        self.add_btn.clicked.connect(self.add_info)
        self.update_btn.clicked.connect(self.update_info)
        self.delete_btn.clicked.connect(self.delete_info)
        self.search_btn.clicked.connect(self.search_info)

    # Bat va tat cac entry trong qua trinh nhap du lieu
    def disable_buttons(self):
        for button in self.buttons_list:
            button.setDisabled(True)
    def enable_buttons(self):
        for button in self.buttons_list:
            button.setDisabled(False)
            
    # Them du lieu
    def add_info(self):
        self.disable_buttons()

        sv_info = self.get_sv_info()

        if sv_info["MASV"] and sv_info["HOTEN"]:
            check_result = self.check_masv(new_masv=int(sv_info["MASV"]))

            if check_result:
                QMessageBox.information(self, "Canh bao", "Nhap lai masv!",
                                        QMessageBox.StandardButton.Ok)
                self.enable_buttons()
                return
            
            add_result = self.DB.add_info(
                masv=int(sv_info["MASV"]),
                hoten=sv_info["HOTEN"],
                lop=sv_info["LOP"],
                ngsinh=sv_info["NGSINH"],
                gtinh=sv_info["GTINH"],
                sdt=sv_info["SDT"]
            )
            
            if add_result:
                QMessageBox.information(self, "Canh bao", f"Them : {add_result} that bai!.",
                                        QMessageBox.StandardButton.Ok)

        else:
            QMessageBox.information(self, "Canh bao", "Nhap ma sinh vien va hoten",
                                    QMessageBox.StandardButton.Ok)
        
        self.display_data()
        self.enable_buttons()

    # Cap nhat du lieu 
    def update_info(self):
        if self.Masv.isEnabled():
            # Kiem tra xem da chon dong nao chua
            self.select_info()
        else:
            new_sv_info = self.get_sv_info()

            if new_sv_info["MASV"]:
                update_result = self.DB.update_info(
                    masv=new_sv_info["MASV"],
                    hoten=new_sv_info["HOTEN"],
                    lop=new_sv_info["LOP"],
                    ngsinh=new_sv_info["NGSINH"],
                    gtinh=new_sv_info["GTINH"],
                    sdt=new_sv_info["SDT"]
                )

                if update_result:
                    QMessageBox.information(self, "Canh bao",
                                            f"Cap nhap: {update_result} that bai!",
                                            QMessageBox.StandardButton.Ok)
                else:
                    self.Masv.setEnabled(True)
                    self.Hoten.clear()
                    self.Lop.clear()
                    self.Ngsinh.clear()
                    self.GTinh.setCurrentIndex(0)
                    self.Sdt.clear()
                    self.display_data()
            else:
                QMessageBox.information(self, "Canh bao",
                                        f"Chon 1 sinh vien de cap nhat",
                                        QMessageBox.StandardButton.Ok)

    def select_info(self):
        # Chon du lieu can chinh sua
        select_row = self.listbox_table.currentRow()
        if select_row != -1:
            self.Masv.setEnabled(False)
            s_Masv = self.listbox_table.item(select_row, 0).text().strip()
            s_Hoten =  self.listbox_table.item(select_row, 1).text().strip()
            s_Lop =  self.listbox_table.item(select_row, 2).text().strip()
            s_Ngsinh =  self.listbox_table.item(select_row, 3).text().strip()
            s_Gtinh =  self.listbox_table.item(select_row, 4).text().strip()
            s_Sdt =  self.listbox_table.item(select_row, 5).text().strip()

            # Set du lieu moi
            self.Masv.setText(s_Masv)
            self.Hoten.setText(s_Hoten)
            self.Lop.setText(s_Lop)
            self.Ngsinh.setText(s_Ngsinh)
            self.GTinh.setCurrentText(s_Gtinh)
            self.Sdt.setText(s_Sdt)
        else:
            QMessageBox.information(self, "Canh bao", "Hay chon 1 sinh vien",
                                    QMessageBox.StandardButton.Ok)
    # Xoa du lieu
    def delete_info(self):
        # Chon dong hien tai
        select_row = self.listbox_table.currentRow()
        if select_row != -1:
            selected_option = QMessageBox.warning(self, "Canh bao", "Ban muon xoa du lieu?",
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
                # Lay masv de thuc hien xoa
                Masv = self.listbox_table.item(select_row, 0).text().strip()

                delete_result = self.DB.delete_info(Masv)

                if not delete_result:
                    self.listbox_table.removeRow(select_row)
                else:
                    QMessageBox.information(self, "Canh bao",
                                            f"That bai xoa {delete_result}! hay thu lai.",
                                            QMessageBox.StandardButton.Ok)

        else:
            QMessageBox.information(self, "Canh bao", "Hay chon 1 sinh vien de xoa",
                                    QMessageBox.StandardButton.Ok)


            
    # Tim kiem du lieu trong database
    def search_info(self):
        sv_info = self.get_sv_info()

        search_result = self.DB.search_info(
            masvtk=sv_info["MASV"],
            hotentk=sv_info["HOTEN"],
            loptk=sv_info["LOP"],
            ngsinhtk=sv_info["NGSINH"],
            gtinhtk=sv_info["GTINH"],
            sdttk=sv_info["SDT"]
        )

        if search_result :
            self.show_data(search_result)
        else:
            self.display_data()
    
    def show_data(self, result):
        # lay du lieu tu bang tim kiem de gan du lieu tu database vao table
        if result:
            self.listbox_table.setRowCount(0)
            self.listbox_table.setRowCount(len(result))

            for row, info in enumerate(result):
                info_list = [
                    info["MASV"],
                    info["HOTEN"],
                    info["LOP"],
                    info["NGSINH"],
                    info["GTINH"],
                    info["SDT"],
                ]

                for column, item in enumerate(info_list):
                    cell_item = QTableWidgetItem(str(item))
                    self.listbox_table.setItem(row, column, cell_item)

    def display_data(self):
        # Lay du lieu tu ham tim kiem
        search_result = self.DB.search_info() # search info trong database

        # Hien thi data 
        self.show_data(search_result)
    
    def get_sv_info(self):
        # Lay du lieu tu input
        get_Masv = self.Masv.text().strip()
        get_Hoten = self.Hoten.text().strip()
        get_Lop = self.Lop.text().strip()
        get_Ngsinh = self.Ngsinh.text().strip()
        get_Gtinh = self.GTinh.currentText().strip()
        get_Sdt = self.Sdt.text().strip()

        # tao dict de luu cac bien
        sv_info = {
            "MASV": get_Masv,
            "HOTEN": get_Hoten, 
            "LOP": get_Lop, 
            "NGSINH": get_Ngsinh, 
            "GTINH": get_Gtinh, 
            "SDT": get_Sdt
        }

        return sv_info
    
    def check_masv(self, new_masv):
        result  = self.DB.search_info(masvtk=new_masv)
        return result
    
    
if __name__ == '__main__':
    APP  = QApplication(sys.argv)
    WINDOW = Window_QLSV()
    WINDOW.show()
    sys.exit(APP.exec())

