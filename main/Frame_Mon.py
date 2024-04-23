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
        ## MON ##
        self.MaMon_QLMH = self.UI.MaMon_Entry_QLMH
        self.TenMon_QLMH = self.UI.TenMon_Entry_QLMH
        self.SoTinChi_QLMH = self.UI.SoTinChi_Entry_QLMH
        self.SoTinChi_QLMH.setValidator(QIntValidator())
        #############################################################################
        ## MONHOC BTN
        self.add_btn_QLMH = self.UI.AddBtn_QLMH
        self.update_btn_QLMH = self.UI.UpdateBtn_QLMH
        self.delete_btn_QLMH = self.UI.DelBtn_QLMH
        #############################################################################
        ## MON TABLE
        self.listbox_QLMH = self.UI.tableWidget_QLMH
        self.listbox_QLMH.setSortingEnabled(False)
        self.buttons_list_QLMH = self.UI.Frame_Listbox_QLMH.findChildren(QPushButton)
        #############################################################################
        self.display_data_QLMH()
        #############################################################################
        self.add_btn_QLMH.clicked.connect(self.add_info_QLMH)
        self.update_btn_QLMH.clicked.connect(self.update_info_QLMH)
        self.delete_btn_QLMH.clicked.connect(self.delete_info_QLMH)
        #############################################################################
        self.UI.QLMHBtn.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_QLMH))
    #############################################################################
    def toggleForm(self, Frame, Form):
        Frame.setCurrentIndex(Frame.indexOf(Form))
    #############################################################################
    def disable_buttons_QLMH(self):
        for button in self.buttons_list_QLMH:
            button.setDisabled(True)
    def enable_buttons_QLMH(self):
        for button in self.buttons_list_QLMH:
            button.setDisabled(False)
    #############################################################################
    ## MON ##
    #############################################################################
    def add_info_QLMH(self):
        self.disable_buttons_QLMH() 

        monhoc_info = self.get_monhoc_info()  

        if monhoc_info["MAMH"] and monhoc_info["TENMH"]:
            check_result = self.check_mamh(new_mamh=monhoc_info["MAMH"])

            if check_result:
                QMessageBox.information(self, "Canh bao", "Nhap lai ma mon hoc!", QMessageBox.StandardButton.Ok)
                self.enable_buttons_QLMH()
                return

            add_result = self.DB.add_info_mh(
                mamh=monhoc_info["MAMH"],
                tenmh=monhoc_info["TENMH"],
                sotc=int(monhoc_info["SOTC"])
            )

            if add_result:
                QMessageBox.information(self, "Warning", f"Them : {add_result} that bai!.", QMessageBox.StandardButton.Ok)
            else:
                    self.MaMon_QLMH.setEnabled(True)
                    self.MaMon_QLMH.clear()
                    self.TenMon_QLMH.clear()
                    self.SoTinChi_QLMH.clear()
                    self.display_data_QLMH()
        else:
            QMessageBox.information(self, "Canh bao", "Nhap ma va ten mon hoc", QMessageBox.StandardButton.Ok)

        self.display_data_QLMH()  
        self.enable_buttons_QLMH()

    #############################################################################
    def update_info_QLMH(self):
        if self.MaMon_QLMH.isEnabled():
            self.select_info_QLMH()
        else:
            new_monhoc_info = self.get_monhoc_info()  

            if new_monhoc_info["MAMH"]:
                update_result = self.DB.update_info_mh(
                    mamh=new_monhoc_info["MAMH"],
                    tenmh=new_monhoc_info["TENMH"],
                    sotc=new_monhoc_info["SOTC"]
                )

                if update_result:
                    QMessageBox.information(self, "Canh bao", f"Cap nhap: {update_result} that bai!", QMessageBox.StandardButton.Ok)
                else:
                    self.MaMon_QLMH.setEnabled(True)
                    self.MaMon_QLMH.clear()
                    self.TenMon_QLMH.clear()
                    self.SoTinChi_QLMH.clear()
                    self.display_data_QLMH()
            else:
                QMessageBox.information(self, "Canh bao", "Chon 1 mon hoc de cap nhat", QMessageBox.StandardButton.Ok)

    #############################################################################
    def select_info_QLMH(self):
        select_row = self.listbox_QLMH.currentRow()
        if select_row != -1:
            self.MaMon_QLMH.setEnabled(False)
            s_MaMonMH = self.listbox_QLMH.item(select_row, 0).text().strip()
            s_TenMonMH = self.listbox_QLMH.item(select_row, 1).text().strip()
            s_SoTinChi = self.listbox_QLMH.item(select_row, 2).text().strip()

            self.MaMon_QLMH.setText(s_MaMonMH)
            self.TenMon_QLMH.setText(s_TenMonMH)
            self.SoTinChi_QLMH.setText(s_SoTinChi)
        else:
            QMessageBox.information(self, "Canh bao", "Hay chon 1 mon hoc", QMessageBox.StandardButton.Ok)
    #############################################################################
    def delete_info_QLMH(self):
        select_row = self.listbox_QLMH.currentRow()
        if select_row != -1:
            selected_option = QMessageBox.warning(self, "Canh bao", "Ban muon xoa du lieu?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
                MaMonMH = self.listbox_QLMH.item(select_row, 0).text().strip()

                delete_result = self.DB.delete_info_mh(MaMonMH)

                if not delete_result:
                    self.listbox_QLMH.removeRow(select_row)
                else:
                    QMessageBox.information(self, "Canh bao", f"That bai xoa {delete_result}! hay thu lai.", QMessageBox.StandardButton.Ok)

        else:
            QMessageBox.information(self, "Canh bao", "Hay chon 1 mon hoc de xoa", QMessageBox.StandardButton.Ok)
    #############################################################################
    def show_data_QLMH(self, result):
        if result:
            self.listbox_QLMH.setRowCount(0)
            self.listbox_QLMH.setRowCount(len(result))

            for row, info in enumerate(result):
                monhoc_info = [
                    info["MAMH"],
                    info["TENMH"],
                    info["SOTC"]
                ]

                for column, item in enumerate(monhoc_info):
                    cell_item = QTableWidgetItem(str(item))
                    self.listbox_QLMH.setItem(row, column, cell_item)
    #############################################################################
    def display_data_QLMH(self):
        search_result = self.DB.search_info_mh()

        self.show_data_QLMH(search_result)
    #############################################################################
    def get_monhoc_info(self):
        get_MaMonMH = self.MaMon_QLMH.text().strip()
        get_TenMonMH = self.TenMon_QLMH.text().strip()
        get_SoTinChi = self.SoTinChi_QLMH.text().strip()

        monhoc_info = {
            "MAMH": get_MaMonMH,
            "TENMH": get_TenMonMH,
            "SOTC": get_SoTinChi
        }

        return monhoc_info
    #############################################################################
    def check_mamh(self, new_mamh):
        result = self.DB.search_info_mh(mamhtk=new_mamh)
        return result
    
if __name__ == '__main__':
    APP  = QApplication([])
    WINDOW = Window_Menu()
    WINDOW.show()
    APP.exec()
