from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem, QPushButton, QWidget, QApplication
from PyQt6.QtCore import QDate
from PyQt6.QtGui import QIntValidator, QDoubleValidator
from main.Form_Menu import Menu
from Backend.Connection_Database import ConnectDB

class Window_Menu(QWidget):
    def __init__(self):
        super(Window_Menu, self).__init__()

        self.UI = Menu()
        self.UI.setupMenu(self)
        #############################################################################
        self.DB = ConnectDB()
        #############################################################################
        ## GV ##
        self.MaGV = self.UI.MaGV_Entry_QLGV
        self.Hoten_QLGV = self.UI.TenGV_Entry_QLGV
        self.Ngsinh_QLGV = self.UI.NgSinh_Entry_QLGV
        self.Gtinh_QLGV = self.UI.Gtinh_Cbox_QLGV
        self.Khoa_GLGV = self.UI.Khoa_Entry_QLGV
        ## GV BTN
        self.add_btn_QLGV = self.UI.AddBtn_QLGV
        self.update_btn_QLGV = self.UI.UpdateBtn_GLGV
        self.delete_btn_QLGV = self.UI.DelBtn_QLGV
        #############################################################################
        ## GV TABLE
        self.listbox_QLGV = self.UI.tableWidget_QLGV
        self.listbox_QLGV.setSortingEnabled(False)
        self.buttons_list_QLGV = self.UI.Frame_Listbox_QLGV.findChildren(QPushButton)
        #############################################################################
        self.display_data_QLGV()
        #############################################################################
        self.add_btn_QLGV.clicked.connect(self.add_info_QLGV)
        self.update_btn_QLGV.clicked.connect(self.update_info_QLGV)
        self.delete_btn_QLGV.clicked.connect(self.delete_info_QLGV)
        #############################################################################
        self.UI.QLGVBtn.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_QLGV))
        #############################################################################
    def toggleForm(self, Frame, Form):
            Frame.setCurrentIndex(Frame.indexOf(Form))
    #############################################################################
    def disable_buttons_QLGV(self):
        for button in self.buttons_list_QLGV:
            button.setDisabled(True)
    def enable_buttons_QLGV(self):
        for button in self.buttons_list_QLGV:
            button.setDisabled(False)
    #############################################################################
    ## GV ##
    #############################################################################
    def add_info_QLGV(self):
        self.disable_buttons_QLGV() 

        gv_info = self.get_gv_info()  

        if gv_info["MAGV"] and gv_info["HOTEN"]:
            check_result = self.check_magv(new_magv=gv_info["MAGV"])

            if check_result:
                QMessageBox.information(self, "Canh bao", "Nhap lai ma giang vien!", QMessageBox.StandardButton.Ok)
                self.enable_buttons_QLGV()
                return

            add_result = self.DB.add_info_gv(
                magv=gv_info["MAGV"],
                hoten=gv_info["HOTEN"],
                ngsinh=gv_info["NGSINH"],
                gtinh=gv_info["GTINH"],
                khoa=gv_info["KHOA"]
            )

            if add_result:
                QMessageBox.information(self, "Warning", f"Them : {add_result} that bai!.", QMessageBox.StandardButton.Ok)
            else:
                self.MaGV.clear()
                self.Hoten_QLGV.clear()
                self.Ngsinh_QLGV.clear()
                self.Gtinh_QLGV.setCurrentIndex(0)
                self.Khoa_GLGV.clear()
                self.display_data_QLGV()
        else:
            QMessageBox.information(self, "Canh bao", "Nhap ma va ho ten giang vien", QMessageBox.StandardButton.Ok)

        self.display_data_QLGV()  
        self.enable_buttons_QLGV()
    #############################################################################
    def update_info_QLGV(self):
        if self.MaGV.isEnabled():
            self.select_info_QLGV()
        else:
            new_gv_info = self.get_gv_info()

            if new_gv_info["MAGV"]:
                update_result = self.DB.update_info_gv(
                    magv=new_gv_info["MAGV"],
                    hoten=new_gv_info["HOTEN"],
                    ngsinh=new_gv_info["NGSINH"],
                    gtinh=new_gv_info["GTINH"],
                    khoa=new_gv_info["KHOA"]
                )

                if update_result:
                    QMessageBox.information(self, "Canh bao", f"Cap nhap: {update_result} that bai!", QMessageBox.StandardButton.Ok)
                else:
                    self.MaGV.setEnabled(True)
                    self.MaGV.clear()
                    self.Hoten_QLGV.clear()
                    self.Ngsinh_QLGV.clear()
                    self.Gtinh_QLGV.setCurrentIndex(0)
                    self.Khoa_GLGV.clear()
                    self.display_data_QLGV()
            else:
                QMessageBox.information(self, "Canh bao", "Chon 1 giang vien de cap nhat", QMessageBox.StandardButton.Ok)
    #############################################################################
    def delete_info_QLGV(self):
        select_row = self.listbox_QLGV.currentRow()
        if select_row != -1:
            selected_option = QMessageBox.warning(self, "Canh bao", "Ban muon xoa du lieu?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
                MaGV = self.listbox_QLGV.item(select_row, 0).text().strip()

                delete_result = self.DB.delete_info_gv(MaGV)

                if not delete_result:
                    self.listbox_QLGV.removeRow(select_row)
                else:
                    QMessageBox.information(self, "Canh bao", f"That bai xoa {delete_result}! hay thu lai.", QMessageBox.StandardButton.Ok)

        else:
            QMessageBox.information(self, "Canh bao", "Hay chon 1 giang vien de xoa", QMessageBox.StandardButton.Ok)
    #############################################################################        
    def select_info_QLGV(self):
        select_row = self.listbox_QLGV.currentRow()
        if select_row != -1:
            self.MaGV.setEnabled(False)
            s_MaGV = self.listbox_QLGV.item(select_row, 0).text().strip()
            s_Hoten = self.listbox_QLGV.item(select_row, 1).text().strip()
            s_Ngsinh = self.listbox_QLGV.item(select_row, 2).text().strip()
            s_Gtinh = self.listbox_QLGV.item(select_row, 3).text().strip()
            s_Khoa = self.listbox_QLGV.item(select_row, 4).text().strip()

            self.MaGV.setText(s_MaGV)
            self.Hoten_QLGV.setText(s_Hoten)
            self.Ngsinh_QLGV.setDate(QDate.fromString(s_Ngsinh, 'yyyy-MM-dd'))
            self.Gtinh_QLGV.setCurrentText(s_Gtinh)
            self.Khoa_GLGV.setText(s_Khoa)
        else:
            QMessageBox.information(self, "Canh bao", "Hay chon 1 giang vien", QMessageBox.StandardButton.Ok)
    #############################################################################
    def show_data_QLGV(self, result):
        if result:
            self.listbox_QLGV.setRowCount(0)
            self.listbox_QLGV.setRowCount(len(result))

            for row, info in enumerate(result):
                info_list = [
                    info["MAGV"],
                    info["HOTEN"],
                    info["NGSINH"],
                    info["GTINH"],
                    info["KHOA"]
                ]

                for column, item in enumerate(info_list):
                    cell_item = QTableWidgetItem(str(item))
                    self.listbox_QLGV.setItem(row, column, cell_item)
    ###############################################################################        
    def display_data_QLGV(self):
        # Lay du lieu tu ham tim kiem
        search_result = self.DB.search_info_gv()

        # Hien thi data
        self.show_data_QLGV(search_result)
    # #############################################################################
    def get_gv_info(self):
        get_MaGV = self.MaGV.text().strip()
        get_Hoten = self.Hoten_QLGV.text().strip()
        get_Ngsinh = self.Ngsinh_QLGV.date().toString("yyyy-MM-dd")
        get_Gtinh = self.Gtinh_QLGV.currentText().strip()
        get_Khoa = self.Khoa_GLGV.text().strip()

        gv_info = {
            "MAGV": get_MaGV,
            "HOTEN": get_Hoten,
            "NGSINH": get_Ngsinh,
            "GTINH": get_Gtinh,
            "KHOA": get_Khoa
        }
        return gv_info
    #############################################################################
    def check_magv(self, new_magv):
        result = self.DB.search_info_gv(magvtk=new_magv)
        return result
if __name__ == '__main__':
    APP  = QApplication([])
    WINDOW = Window_Menu()
    WINDOW.show()
    APP.exec()
