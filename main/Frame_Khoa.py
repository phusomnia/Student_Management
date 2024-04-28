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
        ## KHOA ##
        self.MaKhoa = self.UI.MaKhoa_Entry_QLK
        self.TenKhoa_QLK = self.UI.TenKhoa_Entry_QLK
        self.Sdt_QLK = self.UI.Sdt_Entry_QLK
        self.Phong_QLK = self.UI.Phong_Entry_QLK
        self.TrgKhoa_QLK = self.UI.TrgKhoa_Entry_QLK
        #############################################################################
        ## KHOA BTN
        self.add_btn_QLK = self.UI.AddBtn_QLK
        self.update_btn_QLK = self.UI.UpdateBtn_QLK
        self.delete_btn_QLK = self.UI.DelBtn_QLK
        #############################################################################
        ## KHOA TABLE
        self.listbox_QLK = self.UI.tableWidget_QLK
        self.listbox_QLK.setSortingEnabled(False)
        self.buttons_list_QLK = self.UI.Frame_Listbox_QLK.findChildren(QPushButton)
        #############################################################################
        ## KHOA
        self.display_data_QLK()
        #############################################################################
        self.add_btn_QLK.clicked.connect(self.add_info_QLK)
        self.update_btn_QLK.clicked.connect(self.update_info_QLK)
        self.delete_btn_QLK.clicked.connect(self.delete_info_QLK)
        #############################################################################
        self.UI.QLKBtn.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_QLK))
    #############################################################################
    def toggleForm(self, Frame, Form):
        Frame.setCurrentIndex(Frame.indexOf(Form))
    #############################################################################
    ## DIS KHOA 
    def disable_buttons_QLK(self):
        for button in self.buttons_list_QLK:
            button.setDisabled(True)
    def enable_buttons_QLK(self):
        for button in self.buttons_list_QLK:
            button.setDisabled(False)
    #############################################################################
    #############################################################################
    ## KHOA ##
    #############################################################################
    def add_info_QLK(self):
        self.disable_buttons_QLK() 

        khoa_info = self.get_khoa_info()  

        if khoa_info["MAKHOA"] and khoa_info["TENKHOA"]:
            check_result = self.check_makhoa(new_makhoa=khoa_info["MAKHOA"])

            if check_result:
                QMessageBox.information(self, "Canh bao", "Nhap lai ma khoa!", QMessageBox.StandardButton.Ok)
                self.enable_buttons_QLK()
                return

            add_result = self.DB.add_info_khoa(
                makhoa=khoa_info["MAKHOA"],
                tenkhoa=khoa_info["TENKHOA"],
                sdt=khoa_info["SDT"],
                phong=khoa_info["PHONG"],
                trgkhoa=khoa_info["TRGKHOA"]
            )

            if add_result:
                QMessageBox.information(self, "Canh bao", f"Them : {add_result} that bai!.", QMessageBox.StandardButton.Ok)
            else:
                self.MaKhoa.clear()
                self.TenKhoa_QLK.clear()
                self.Sdt_QLK.clear()
                self.Phong_QLK.clear()
                self.TrgKhoa_QLK.clear()
                self.display_data_QLK()
        else:
            QMessageBox.information(self, "Canh bao", "Nhap ma va ten khoa", QMessageBox.StandardButton.Ok)

        self.display_data_QLK()  
        self.enable_buttons_QLK()
    #############################################################################
    def update_info_QLK(self):
        if self.MaKhoa.isEnabled():
            self.select_info_QLK()
        else:
            new_khoa_info = self.get_khoa_info()  

            if new_khoa_info["MAKHOA"]:
                update_result = self.DB.update_info_khoa(
                    makhoa=new_khoa_info["MAKHOA"],
                    tenkhoa=new_khoa_info["TENKHOA"],
                    sdt=new_khoa_info["SDT"],
                    phong=new_khoa_info["PHONG"],
                    trgkhoa=new_khoa_info["TRGKHOA"]
                )

                if update_result:
                    QMessageBox.information(self, "Canh bao", f"Cap nhap: {update_result} that bai!", QMessageBox.StandardButton.Ok)
                else:
                    self.MaKhoa.setEnabled(True)
                    self.MaKhoa.clear()
                    self.TenKhoa_QLK.clear()
                    self.Sdt_QLK.clear()
                    self.Phong_QLK.clear()
                    self.TrgKhoa_QLK.clear()
                    self.display_data_QLK()
            else:
                QMessageBox.information(self, "Canh bao", "Chon 1 khoa de cap nhat", QMessageBox.StandardButton.Ok)
    #############################################################################
    def select_info_QLK(self):
        select_row = self.listbox_QLK.currentRow()
        if select_row != -1:
            self.MaKhoa.setEnabled(False)
            self.TrgKhoa_QLK.setEnabled(False)
            s_MaKhoa = self.listbox_QLK.item(select_row, 0).text().strip()
            s_TenKhoa = self.listbox_QLK.item(select_row, 1).text().strip()
            s_SdtKhoa = self.listbox_QLK.item(select_row, 2).text().strip()
            s_PhongKhoa = self.listbox_QLK.item(select_row, 3).text().strip()
            s_TrgKhoa = self.listbox_QLK.item(select_row, 4).text().strip()

            self.MaKhoa.setText(s_MaKhoa)
            self.TenKhoa_QLK.setText(s_TenKhoa)
            self.Sdt_QLK.setText(s_SdtKhoa)
            self.Phong_QLK.setText(s_PhongKhoa)
            self.TrgKhoa_QLK.setText(s_TrgKhoa)
        else:
            QMessageBox.information(self, "Canh bao", "Hay chon 1 khoa de xem thong tin", QMessageBox.StandardButton.Ok)
    #############################################################################
    def delete_info_QLK(self):
        select_row = self.listbox_QLK.currentRow()
        if select_row != -1:
            selected_option = QMessageBox.warning(self, "Canh bao", "Ban muon xoa du lieu?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
                MaKhoa = self.listbox_QLK.item(select_row, 0).text().strip()

                delete_result = self.DB.delete_info_khoa(MaKhoa)

                if not delete_result:
                    self.listbox_QLK.removeRow(select_row)
                else:
                    QMessageBox.information(self, "Canh bao", f"That bai xoa {delete_result}! hay thu lai.", QMessageBox.StandardButton.Ok)

        else:
            QMessageBox.information(self, "Canh bao", "Hay chon 1 khoa de xoa", QMessageBox.StandardButton.Ok)
    #############################################################################
    def show_data_QLK(self, result):
        if result:
            self.listbox_QLK.setRowCount(0)
            self.listbox_QLK.setRowCount(len(result))

            for row, info in enumerate(result):
                khoa_info = [
                    info["MAKHOA"],
                    info["TENKHOA"],
                    info["SDT"],
                    info["PHONG"],
                    info["TRGKHOA"]
                ]

                for column, item in enumerate(khoa_info):
                    cell_item = QTableWidgetItem(str(item))
                    self.listbox_QLK.setItem(row, column, cell_item)
    #############################################################################        
    def display_data_QLK(self):
        search_result = self.DB.search_info_khoa()

        self.show_data_QLK(search_result)
    #############################################################################
    def get_khoa_info(self):
        get_MaKhoa = self.MaKhoa.text().strip()
        get_TenKhoa = self.TenKhoa_QLK.text().strip()
        get_Sdt = self.Sdt_QLK.text().strip()
        get_Phong = self.Phong_QLK.text().strip()
        get_TrgKhoa = self.TrgKhoa_QLK.text().strip()

        khoa_info = {
            "MAKHOA": get_MaKhoa,
            "TENKHOA": get_TenKhoa,
            "SDT": get_Sdt,
            "PHONG": get_Phong,
            "TRGKHOA": get_TrgKhoa
        }

        return khoa_info
    #############################################################################
    def check_makhoa(self, new_makhoa):
        result = self.DB.search_info_khoa(makhoatk=new_makhoa)
        return result
    #############################################################################
    ## KHOA ##
    #############################################################################
    def add_info_QLK(self):
        self.disable_buttons_QLK() 

        khoa_info = self.get_khoa_info()  

        if khoa_info["MAKHOA"] and khoa_info["TENKHOA"]:
            check_result = self.check_makhoa(new_makhoa=khoa_info["MAKHOA"])

            if check_result:
                QMessageBox.information(self, "Canh bao", "Nhap lai ma khoa!", QMessageBox.StandardButton.Ok)
                self.enable_buttons_QLK()
                return

            add_result = self.DB.add_info_khoa(
                makhoa=khoa_info["MAKHOA"],
                tenkhoa=khoa_info["TENKHOA"],
                sdt=khoa_info["SDT"],
                phong=khoa_info["PHONG"],
                trgkhoa=khoa_info["TRGKHOA"]
            )

            if add_result:
                QMessageBox.information(self, "Canh bao", f"Them : {add_result} that bai!.", QMessageBox.StandardButton.Ok)
            else:
                self.MaKhoa.clear()
                self.TenKhoa_QLK.clear()
                self.Sdt_QLK.clear()
                self.Phong_QLK.clear()
                self.TrgKhoa_QLK.clear()
                self.display_data_QLK()
        else:
            QMessageBox.information(self, "Canh bao", "Nhap ma va ten khoa", QMessageBox.StandardButton.Ok)

        self.display_data_QLK()  
        self.enable_buttons_QLK()
    #############################################################################
    def update_info_QLK(self):
        if self.MaKhoa.isEnabled():
            self.select_info_QLK()
        else:
            new_khoa_info = self.get_khoa_info()  

            if new_khoa_info["MAKHOA"]:
                update_result = self.DB.update_info_khoa(
                    makhoa=new_khoa_info["MAKHOA"],
                    tenkhoa=new_khoa_info["TENKHOA"],
                    sdt=new_khoa_info["SDT"],
                    phong=new_khoa_info["PHONG"],
                    trgkhoa=new_khoa_info["TRGKHOA"]
                )

                if update_result:
                    QMessageBox.information(self, "Canh bao", f"Cap nhap: {update_result} that bai!", QMessageBox.StandardButton.Ok)
                else:
                    self.MaKhoa.setEnabled(True)
                    self.MaKhoa.clear()
                    self.TenKhoa_QLK.clear()
                    self.Sdt_QLK.clear()
                    self.Phong_QLK.clear()
                    self.TrgKhoa_QLK.clear()
                    self.display_data_QLK()
            else:
                QMessageBox.information(self, "Canh bao", "Chon 1 khoa de cap nhat", QMessageBox.StandardButton.Ok)
    #############################################################################
    def select_info_QLK(self):
        select_row = self.listbox_QLK.currentRow()
        if select_row != -1:
            self.MaKhoa.setEnabled(False)
            self.TrgKhoa_QLK.setEnabled(False)
            s_MaKhoa = self.listbox_QLK.item(select_row, 0).text().strip()
            s_TenKhoa = self.listbox_QLK.item(select_row, 1).text().strip()
            s_SdtKhoa = self.listbox_QLK.item(select_row, 2).text().strip()
            s_PhongKhoa = self.listbox_QLK.item(select_row, 3).text().strip()
            s_TrgKhoa = self.listbox_QLK.item(select_row, 4).text().strip()

            self.MaKhoa.setText(s_MaKhoa)
            self.TenKhoa_QLK.setText(s_TenKhoa)
            self.Sdt_QLK.setText(s_SdtKhoa)
            self.Phong_QLK.setText(s_PhongKhoa)
            self.TrgKhoa_QLK.setText(s_TrgKhoa)
        else:
            QMessageBox.information(self, "Canh bao", "Hay chon 1 khoa de xem thong tin", QMessageBox.StandardButton.Ok)
    #############################################################################
    def delete_info_QLK(self):
        select_row = self.listbox_QLK.currentRow()
        if select_row != -1:
            selected_option = QMessageBox.warning(self, "Canh bao", "Ban muon xoa du lieu?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
                MaKhoa = self.listbox_QLK.item(select_row, 0).text().strip()

                delete_result = self.DB.delete_info_khoa(MaKhoa)

                if not delete_result:
                    self.listbox_QLK.removeRow(select_row)
                else:
                    QMessageBox.information(self, "Canh bao", f"That bai xoa {delete_result}! hay thu lai.", QMessageBox.StandardButton.Ok)

        else:
            QMessageBox.information(self, "Canh bao", "Hay chon 1 khoa de xoa", QMessageBox.StandardButton.Ok)
    #############################################################################
    def show_data_QLK(self, result):
        if result:
            self.listbox_QLK.setRowCount(0)
            self.listbox_QLK.setRowCount(len(result))

            for row, info in enumerate(result):
                khoa_info = [
                    info["MAKHOA"],
                    info["TENKHOA"],
                    info["SDT"],
                    info["PHONG"],
                    info["TRGKHOA"]
                ]

                for column, item in enumerate(khoa_info):
                    cell_item = QTableWidgetItem(str(item))
                    self.listbox_QLK.setItem(row, column, cell_item)
    #############################################################################        
    def display_data_QLK(self):
        search_result = self.DB.search_info_khoa()

        self.show_data_QLK(search_result)
    #############################################################################
    def get_khoa_info(self):
        get_MaKhoa = self.MaKhoa.text().strip()
        get_TenKhoa = self.TenKhoa_QLK.text().strip()
        get_Sdt = self.Sdt_QLK.text().strip()
        get_Phong = self.Phong_QLK.text().strip()
        get_TrgKhoa = self.TrgKhoa_QLK.text().strip()

        khoa_info = {
            "MAKHOA": get_MaKhoa,
            "TENKHOA": get_TenKhoa,
            "SDT": get_Sdt,
            "PHONG": get_Phong,
            "TRGKHOA": get_TrgKhoa
        }

        return khoa_info
    #############################################################################
    def check_makhoa(self, new_makhoa):
        result = self.DB.search_info_khoa(makhoatk=new_makhoa)
        return result
    
    
if __name__ == '__main__':
    APP  = QApplication([])
    WINDOW = Window_Menu()
    WINDOW.show()
    APP.exec()
