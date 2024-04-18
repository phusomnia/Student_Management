from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem, QPushButton, QWidget, QApplication
from PyQt6.QtCore import QDate
from PyQt6.QtGui import QIntValidator
from Backend.Connection_Database import ConnectDB

class QLSV:
    def __init__(self, UI):
        self.DB = ConnectDB()

        self.Masv = UI.MaSV_Entry
        self.Masv.setValidator(QIntValidator())

        self.Hoten = UI.TenSV_Entry
        self.Lop = UI.LopSV_Entry
        self.Dchi = UI.DiaChiSV_Entry
        self.Ngsinh = UI.NgSinhSV_Entry
        self.GTinh = UI.ComboboxGtinh
        self.Sdt = UI.SdtSV_Entry

        self.add_btn = UI.AddBtn_QLSV
        self.update_btn = UI.UpdateBtn_QLSV
        self.delete_btn = UI.DelBtn_QLSV

        self.listbox_table = UI.tableWidgetQLSV
        self.listbox_table.setSortingEnabled(False)
        self.buttons_list = UI.Frame_Listbox_QLSV.findChildren(QPushButton)

        # Khoi tao cac chuc nang
        self.init_signal_slot_QLSV()

        # Khoi tao hien thi du lieu dang co trong database
        self.display_data_QLSV()

    def init_signal_slot_QLSV(self):
        self.add_btn.clicked.connect(self.add_info_QLSV)
        self.update_btn.clicked.connect(self.update_info_QLSV)
        self.delete_btn.clicked.connect(self.delete_info_QLSV)

    def disable_buttons(self):
        for button in self.buttons_list:
            button.setDisabled(True)

    def enable_buttons(self):
        for button in self.buttons_list:
            button.setDisabled(False)

    def add_info_QLSV(self):
        self.disable_buttons()

        sv_info = self.get_sv_info()

        if sv_info["MASV"] and sv_info["HOTEN"]:
            check_result = self.check_masv(new_masv=int(sv_info["MASV"]))

            if check_result:
                QMessageBox.information(self, "Canh bao", "Nhap lai masv!", QMessageBox.StandardButton.Ok)
                self.enable_buttons()
                return

            add_result = self.DB.add_info(
                masv=int(sv_info["MASV"]),
                hoten=sv_info["HOTEN"],
                lop=sv_info["LOP"],
                diachi=sv_info["DCHI"],
                ngsinh=sv_info["NGSINH"],
                gtinh=sv_info["GTINH"],
                sdt=sv_info["SDT"]
            )

            if add_result:
                QMessageBox.information(self, "Canh bao", f"Them : {add_result} that bai!.", QMessageBox.StandardButton.Ok)

        else:
            QMessageBox.information(self, "Canh bao", "Nhap ma sinh vien va hoten", QMessageBox.StandardButton.Ok)

        self.display_data_QLSV()
        self.enable_buttons()

    def update_info_QLSV(self):
        if self.Masv.isEnabled():
            # Kiem tra xem da chon dong nao chua
            self.select_info_QLSV()
        else:
            new_sv_info = self.get_sv_info()

            if new_sv_info["MASV"]:
                update_result = self.DB.update_info(
                    masv=new_sv_info["MASV"],
                    hoten=new_sv_info["HOTEN"],
                    lop=new_sv_info["LOP"],
                    diachi=new_sv_info["DCHI"],
                    ngsinh=new_sv_info["NGSINH"],
                    gtinh=new_sv_info["GTINH"],
                    sdt=new_sv_info["SDT"]
                )

                if update_result:
                    QMessageBox.information(self, "Canh bao", f"Cap nhap: {update_result} that bai!", QMessageBox.StandardButton.Ok)
                else:
                    self.Masv.setEnabled(True)
                    self.Masv.clear()
                    self.Hoten.clear()
                    self.Lop.clear()
                    self.Dchi.clear()
                    self.Ngsinh.clear()
                    self.GTinh.setCurrentIndex(0)
                    self.Sdt.clear()
                    self.display_data_QLSV()
            else:
                QMessageBox.information(self, "Canh bao", f"Chon 1 sinh vien de cap nhat", QMessageBox.StandardButton.Ok)

    def select_info_QLSV(self):
        # Chon du lieu can chinh sua
        select_row = self.listbox_table.currentRow()
        if select_row != -1:
            self.Masv.setEnabled(False)
            s_Masv = self.listbox_table.item(select_row, 0).text().strip()
            s_Hoten =  self.listbox_table.item(select_row, 1).text().strip()
            s_Lop =  self.listbox_table.item(select_row, 2).text().strip()
            s_Dchi = self.listbox_table.item(select_row, 3).text().strip()
            s_Ngsinh =  self.listbox_table.item(select_row, 4).text().strip()
            s_Gtinh =  self.listbox_table.item(select_row, 5).text().strip()
            s_Sdt =  self.listbox_table.item(select_row, 6).text().strip()

            # Set du lieu moi
            self.Masv.setText(s_Masv)
            self.Hoten.setText(s_Hoten)
            self.Lop.setText(s_Lop)
            self.Dchi.setText(s_Dchi)
            self.Ngsinh.setDate(QDate.fromString(s_Ngsinh, 'yyyy-MM-dd'))
            self.GTinh.setCurrentText(s_Gtinh)
            self.Sdt.setText(s_Sdt)
        else:
            QMessageBox.information(self, "Canh bao", "Hay chon 1 sinh vien", QMessageBox.StandardButton.Ok)

    def delete_info_QLSV(self):
        # Chon dong hien tai
        select_row = self.listbox_table.currentRow()
        if select_row != -1:
            selected_option = QMessageBox.warning(self, "Canh bao", "Ban muon xoa du lieu?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
                # Lay masv de thuc hien xoa
                Masv = self.listbox_table.item(select_row, 0).text().strip()

                delete_result = self.DB.delete_info(Masv)

                if not delete_result:
                    self.listbox_table.removeRow(select_row)
                else:
                    QMessageBox.information(self, "Canh bao", f"That bai xoa {delete_result}! hay thu lai.", QMessageBox.StandardButton.Ok)

        else:
            QMessageBox.information(self, "Canh bao", "Hay chon 1 sinh vien de xoa", QMessageBox.StandardButton.Ok)

    def search_info_QLSV(self):
        sv_info = self.get_sv_info()

        search_result = self.DB.search_info(
            masvtk=sv_info["MASV"],
            hotentk=sv_info["HOTEN"],
            loptk=sv_info["LOP"],
            dchitk=sv_info["DCHI"],
            ngsinhtk=sv_info["NGSINH"],
            gtinhtk=sv_info["GTINH"],
            sdttk=sv_info["SDT"]
        )

        self.show_data_QLSV(search_result)

    def show_data_QLSV(self, result):
        # lay du lieu tu bang tim kiem de gan du lieu tu database vao table
        if result:
            self.listbox_table.setRowCount(0)
            self.listbox_table.setRowCount(len(result))

            for row, info in enumerate(result):
                info_list = [
                    info["MASV"],
                    info["HOTEN"],
                    info["LOP"],
                    info["DCHI"],
                    info["NGSINH"],
                    info["GTINH"],
                    info["SDT"],
                ]

                for column, item in enumerate(info_list):
                    cell_item = QTableWidgetItem(str(item))
                    self.listbox_table.setItem(row, column, cell_item)

    def display_data_QLSV(self):
        # Lay du lieu tu ham tim kiem
        search_result = self.DB.search_info()

        # Hien thi data
        self.show_data_QLSV(search_result)

    def get_sv_info(self):
        # Lay du lieu tu input
        get_Masv = self.Masv.text().strip()
        get_Hoten = self.Hoten.text().strip()
        get_Lop = self.Lop.text().strip()
        get_Dchi = self.Dchi.text().strip()
        get_Ngsinh = self.Ngsinh.date().toString("yyyy-MM-dd")
        get_Gtinh = self.GTinh.currentText().strip()
        get_Sdt = self.Sdt.text().strip()

        # tao dict de luu cac bien
        sv_info = {
            "MASV": get_Masv,
            "HOTEN": get_Hoten,
            "LOP": get_Lop,
            "DCHI": get_Dchi,
            "NGSINH": get_Ngsinh,
            "GTINH": get_Gtinh,
            "SDT": get_Sdt
        }

        return sv_info

    def check_masv(self, new_masv):
        result = self.DB.search_info(masvtk=new_masv)
        return result
