from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem, QPushButton, QWidget, QApplication
from PyQt6.QtCore import QDate
from PyQt6.QtGui import QIntValidator, QDoubleValidator
from FrontEnd.Form_Menu import Menu
from Backend.Connection_Database import ConnectDB

class Window_Menu(QWidget):
    def __init__(self):
        super(Window_Menu, self).__init__()

        self.UI = Menu()
        self.UI.setupMenu(self)
        #############################################################################
        self.DB = ConnectDB()
        ## SV ##
        self.MaSV = self.UI.MaSV_Entry_QLSV
        self.Hoten_QLSV = self.UI.TenSV_Entry_QLSV
        self.Ngsinh_QLSV = self.UI.NgSinh_Entry_QLSV
        self.GTinh_QLSV = self.UI.Gtinh_Cbox_QLSV
        self.Dchi_QLSV = self.UI.DiaChi_Entry_QLSV
        self.Sdt_QLSV = self.UI.Sdt_Entry_QLSV
        self.Lop_QLSV = self.UI.Lop_Entry_QLSV
        #############################################################################
        ## SV BTN
        self.add_btn_QLSV = self.UI.AddBtn_QLSV
        self.update_btn_QLSV = self.UI.UpdateBtn_QLSV
        self.delete_btn_QLSV = self.UI.DelBtn_QLSV
        #############################################################################
        ## SV TABLE
        self.listbox_QLSV = self.UI.tableWidget_QLSV
        self.listbox_QLSV.setSortingEnabled(False)
        self.buttons_list_QLSV = self.UI.Frame_Listbox_QLSV.findChildren(QPushButton)
        #############################################################################
        self.display_data_QLSV()
        #############################################################################
        self.add_btn_QLSV.clicked.connect(self.add_info_QLSV)
        self.update_btn_QLSV.clicked.connect(self.update_info_QLSV)
        self.delete_btn_QLSV.clicked.connect(self.delete_info_QLSV)
        #############################################################################
        self.UI.QLSVBtn.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_QLSV))
    #############################################################################
    def toggleForm(self, Frame, Form):
        Frame.setCurrentIndex(Frame.indexOf(Form))
    #############################################################################
    def disable_buttons_QLSV(self):
        for button in self.buttons_list_QLSV:
            button.setDisabled(True)
    def enable_buttons_QLSV(self):
        for button in self.buttons_list_QLSV:
            button.setDisabled(False)
    #############################################################################
    ## SV ##
    #############################################################################
    def add_info_QLSV(self):
        self.disable_buttons_QLSV()

        sv_info = self.get_sv_info()

        if sv_info["MASV"] and sv_info["HOTENSV"]:
            check_result = self.check_masv(new_masv=sv_info["MASV"])

            if check_result:
                QMessageBox.information(self, "Canh bao", "Nhap lai MaSV!", QMessageBox.StandardButton.Ok)
                self.enable_buttons_QLSV()
                return

            add_result = self.DB.add_info_sv(
                masv=sv_info["MASV"],
                hoten=sv_info["HOTENSV"],
                diachi=sv_info["DCHI"],
                ngsinh=sv_info["NGSINH"],
                gtinh=sv_info["GTINH"],
                sdt=sv_info["SDT"],
                lop=sv_info["LOP"]
            )

            if add_result:
                QMessageBox.information(self, "Canh bao", f"Them : {add_result} that bai!.", QMessageBox.StandardButton.Ok)
            else:
                self.MaSV.clear()
                self.Hoten_QLSV.clear()
                self.Lop_QLSV.clear()
                self.Dchi_QLSV.clear()
                self.Ngsinh_QLSV.clear()
                self.GTinh_QLSV.setCurrentIndex(0)
                self.Sdt_QLSV.clear()
        else:
            QMessageBox.information(self, "Canh bao", "Nhap ma va ho ten sinh vien", QMessageBox.StandardButton.Ok)

        self.display_data_QLSV()
        self.enable_buttons_QLSV()
    #############################################################################
    def update_info_QLSV(self):
        if self.MaSV.isEnabled():
            # Kiem tra xem da chon dong nao chua
            self.select_info_QLSV()
        else:
            new_sv_info = self.get_sv_info()

            if new_sv_info["MASV"]:
                update_result = self.DB.update_info_sv(
                    masv=new_sv_info["MASV"],
                    hoten=new_sv_info["HOTENSV"],
                    ngsinh=new_sv_info["NGSINH"],
                    gtinh=new_sv_info["GTINH"],
                    diachi=new_sv_info["DCHI"],
                    sdt=new_sv_info["SDT"],
                    lop=new_sv_info["LOP"]
                )

                if update_result:
                    QMessageBox.information(self, "Canh bao", f"Cap nhap: {update_result} that bai!", QMessageBox.StandardButton.Ok)
                else:
                    self.MaSV.setEnabled(True)
                    self.Lop_QLSV.setEnabled(True)
                    self.MaSV.clear()
                    self.Hoten_QLSV.clear()
                    self.Ngsinh_QLSV.clear()
                    self.GTinh_QLSV.setCurrentIndex(0)
                    self.Dchi_QLSV.clear()
                    self.Sdt_QLSV.clear()
                    self.Lop_QLSV.clear()
                    self.display_data_QLSV()
            else:
                QMessageBox.information(self, "Canh bao", f"Chon 1 sinh vien de cap nhat", QMessageBox.StandardButton.Ok)
    #############################################################################
    def select_info_QLSV(self):
        # CHON DU LIEU DE CHINH SUA
        select_row = self.listbox_QLSV.currentRow()
        if select_row != -1:
            self.MaSV.setEnabled(False)
            self.Lop_QLSV.setEnabled(False)
            s_MaSV = self.listbox_QLSV.item(select_row, 0).text().strip()
            s_Hoten = self.listbox_QLSV.item(select_row, 1).text().strip()
            s_Ngsinh =  self.listbox_QLSV.item(select_row, 2).text().strip()
            s_Gtinh =  self.listbox_QLSV.item(select_row, 3).text().strip()
            s_Dchi = self.listbox_QLSV.item(select_row, 4).text().strip()
            s_Sdt =  self.listbox_QLSV.item(select_row, 5).text().strip()
            s_Lop =  self.listbox_QLSV.item(select_row, 6).text().strip()
            # Set du lieu moi
            self.MaSV.setText(s_MaSV)
            self.Hoten_QLSV.setText(s_Hoten)
            self.Lop_QLSV.setText(s_Lop)
            self.Dchi_QLSV.setText(s_Dchi)
            self.Ngsinh_QLSV.setDate(QDate.fromString(s_Ngsinh, 'yyyy-MM-dd'))
            self.GTinh_QLSV.setCurrentText(s_Gtinh)
            self.Sdt_QLSV.setText(s_Sdt)
            self.Lop_QLSV.setText(s_Lop)
        else:
            QMessageBox.information(self, "Canh bao", "Hay chon 1 sinh vien", QMessageBox.StandardButton.Ok)
    #############################################################################
    def delete_info_QLSV(self):
        # CHON DONG HIEN TAI
        select_row = self.listbox_QLSV.currentRow()
        if select_row != -1:
            selected_option = QMessageBox.warning(self, "Canh bao", "Ban muon xoa du lieu?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
                # LAY DONG DAU TIEN (THUONG LA KHOA CHINH)
                MaSV = self.listbox_QLSV.item(select_row, 0).text().strip()
                # THUC HIEN LENH XOA TRONG DB
                delete_result = self.DB.delete_info_sv(MaSV)

                if not delete_result:
                    self.listbox_QLSV.removeRow(select_row)
                else:
                    QMessageBox.information(self, "Canh bao", f"That bai xoa {delete_result}! hay thu lai.", QMessageBox.StandardButton.Ok)

        else:
            QMessageBox.information(self, "Canh bao", "Hay chon 1 sinh vien de xoa", QMessageBox.StandardButton.Ok)
    #############################################################################
    def show_data_QLSV(self, result):
        # LAY DU LIEU TRONG DICT GAN VAO TABLE
        if result:
            self.listbox_QLSV.setRowCount(0)
            self.listbox_QLSV.setRowCount(len(result))

            for row, info in enumerate(result):
                info_list = [
                    info["MASV"],
                    info["HOTENSV"],
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
    def display_data_QLSV(self):
        # LAY DU LIEU TU TRONG DB BANG HAM TRUY VAN
        search_result = self.DB.search_info_sv()

        # HIEN THI NOI DUNG
        self.show_data_QLSV(search_result)
    #############################################################################
    def get_sv_info(self):
        # LAY DU LIEU TU LINEEDIT
        get_Masv = self.MaSV.text().strip()
        get_Hoten = self.Hoten_QLSV.text().strip()
        get_Ngsinh = self.Ngsinh_QLSV.date().toString("yyyy-MM-dd")
        get_Gtinh = self.GTinh_QLSV.currentText().strip()
        get_Dchi = self.Dchi_QLSV.text().strip()
        get_Sdt = self.Sdt_QLSV.text().strip()
        get_Lop = self.Lop_QLSV.text().strip()

        # TAO DICT DE LUU CAC BIEN
        sv_info = {
            "MASV": get_Masv,
            "HOTENSV": get_Hoten, 
            "NGSINH": get_Ngsinh, 
            "GTINH": get_Gtinh, 
            "DCHI": get_Dchi,
            "SDT": get_Sdt,
            "LOP": get_Lop
        }

        return sv_info
    #############################################################################
    def check_masv(self, new_masv):
        # TIM MASV TRONG DATABASE DE KIEM TRA
        result = self.DB.search_info_sv(masvtk=new_masv)
        return result
    
if __name__ == '__main__':
    APP  = QApplication([])
    WINDOW = Window_Menu()
    WINDOW.show()
    APP.exec()
