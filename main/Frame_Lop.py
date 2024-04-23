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
        ## LOP ##
        self.MaLop = self.UI.MaLop_Entry_QLL
        self.TenLop_QLL = self.UI.TenLop_Entry_QLL
        self.Khoa_QLL = self.UI.Khoa_Entry_QLL
        self.KhoaHK_QLL = self.UI.KhoaHK_Entry_QLL
        self.HDT_QLL = self.UI.HeDaoTao_Entry_QLL
        #############################################################################
        ## LOP BTN
        self.add_btn_QLL = self.UI.AddBtn_QLL
        self.update_btn_QLL = self.UI.UpdateBtn_QLL
        self.delete_btn_QLL = self.UI.DelBtn_QLL
        #############################################################################
        ## LOP TABLE
        self.listbox_QLL = self.UI.tableWidget_QLL
        self.listbox_QLL.setSortingEnabled(False)
        self.buttons_list_QLL = self.UI.Frame_Listbox_QLL.findChildren(QPushButton)
        #############################################################################
        self.display_data_QLL()
        #############################################################################
        self.add_btn_QLL.clicked.connect(self.add_info_QLL)
        self.update_btn_QLL.clicked.connect(self.update_info_QLL)
        self.delete_btn_QLL.clicked.connect(self.delete_info_QLL)
        #############################################################################
        self.UI.QLLBtn.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_QLL))
    #############################################################################
    def toggleForm(self, Frame, Form):
        Frame.setCurrentIndex(Frame.indexOf(Form))
    #############################################################################
    ## DIS LOP 
    def disable_buttons_QLL(self):
        for button in self.buttons_list_QLL:
            button.setDisabled(True)
    def enable_buttons_QLL(self):
        for button in self.buttons_list_QLL:
            button.setDisabled(False)
    #############################################################################
    ## LOP ##
    #############################################################################
    def add_info_QLL(self):
        self.disable_buttons_QLL() 

        lop_info = self.get_lop_info()  

        if lop_info["MALOP"] and lop_info["TENLOP"]:
            check_result = self.check_malop(new_malop=lop_info["MALOP"])

            if check_result:
                QMessageBox.information(self, "Canh bao", "Nhap lai ma lop!", QMessageBox.StandardButton.Ok)
                self.enable_buttons_QLL()
                return

            add_result = self.DB.add_info_lop(
                malop=lop_info["MALOP"],
                tenlop=lop_info["TENLOP"],
                khoa=lop_info["KHOA"],
                khoahoc=lop_info["KHOAHK"],
                hedaotao=lop_info["HDT"]
            )

            if add_result:
                QMessageBox.information(self, "Warning", f"Them : {add_result} that bai!.", QMessageBox.StandardButton.Ok)
            else:
                self.MaLop.clear()
                self.TenLop_QLL.clear()
                self.Khoa_QLL.clear()
                self.KhoaHK_QLL.clear()
                self.HDT_QLL.clear()
                self.display_data_QLL()
        else:
            QMessageBox.information(self, "Canh bao", "Nhap ma va ten lop", QMessageBox.StandardButton.Ok)

        self.display_data_QLL()  
        self.enable_buttons_QLL()
    #############################################################################
    def update_info_QLL(self):
        if self.MaLop.isEnabled():
            self.select_info_QLL()
        else:
            new_lop_info = self.get_lop_info()  

            if new_lop_info["MALOP"]:
                update_result = self.DB.update_info_lop(
                    malop=new_lop_info["MALOP"],
                    tenlop=new_lop_info["TENLOP"],
                    khoa=new_lop_info["KHOA"],
                    khoahoc=new_lop_info["KHOAHK"],
                    hedaotao=new_lop_info["HDT"]
                )

                if update_result:
                    QMessageBox.information(self, "Canh bao", f"Cap nhap: {update_result} that bai!", QMessageBox.StandardButton.Ok)
                else:
                    self.MaLop.setEnabled(True)
                    self.MaLop.clear()
                    self.TenLop_QLL.clear()
                    self.Khoa_QLL.clear()
                    self.KhoaHK_QLL.clear()
                    self.HDT_QLL.clear()
                    self.display_data_QLL()
            else:
                QMessageBox.information(self, "Canh bao", "Chon 1 lop de cap nhat", QMessageBox.StandardButton.Ok)
    #############################################################################
    def select_info_QLL(self):
        select_row = self.listbox_QLL.currentRow()
        if select_row != -1:
            self.MaLop.setEnabled(False)
            self.Khoa_QLL.setEnabled(False)
            s_MaLop = self.listbox_QLL.item(select_row, 0).text().strip()
            s_TenLop = self.listbox_QLL.item(select_row, 1).text().strip()
            s_Khoa = self.listbox_QLL.item(select_row, 2).text().strip()
            s_KhoaHK = self.listbox_QLL.item(select_row, 3).text().strip()
            s_HDT = self.listbox_QLL.item(select_row, 4).text().strip()

            self.MaLop.setText(s_MaLop)
            self.TenLop_QLL.setText(s_TenLop)
            self.Khoa_QLL.setText(s_Khoa)
            self.KhoaHK_QLL.setText(s_KhoaHK)
            self.HDT_QLL.setText(s_HDT)
        else:
            QMessageBox.information(self, "Canh bao", "Hay chon 1 lop", QMessageBox.StandardButton.Ok)
    #############################################################################
    def delete_info_QLL(self):
        select_row = self.listbox_QLL.currentRow()
        if select_row != -1:
            selected_option = QMessageBox.warning(self, "Canh bao", "Ban muon xoa du lieu?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
                MaLop = self.listbox_QLL.item(select_row, 0).text().strip()

                delete_result = self.DB.delete_info_lop(MaLop)

                if not delete_result:
                    self.listbox_QLL.removeRow(select_row)
                else:
                    QMessageBox.information(self, "Canh bao", f"That bai xoa {delete_result}! hay thu lai.", QMessageBox.StandardButton.Ok)

        else:
            QMessageBox.information(self, "Canh bao", "Hay chon 1 lop de xoa", QMessageBox.StandardButton.Ok)
    #############################################################################
    def show_data_QLL(self, result):
        if result:
            self.listbox_QLL.setRowCount(0)
            self.listbox_QLL.setRowCount(len(result))

            for row, info in enumerate(result):
                lop_list = [
                    info["MALOP"],
                    info["TENLOP"],
                    info["KHOA"],
                    info["KHOAHOC"],
                    info["HEDAOTAO"]
                ]

                for column, item in enumerate(lop_list):
                    cell_item = QTableWidgetItem(str(item))
                    self.listbox_QLL.setItem(row, column, cell_item)
    # #############################################################################        
    def display_data_QLL(self):
        search_result = self.DB.search_info_lop()

        self.show_data_QLL(search_result)
    ###############################################################################
    def get_lop_info(self):
        get_Malop = self.MaLop.text().strip()
        get_TenLop = self.TenLop_QLL.text().strip()
        get_Khoa = self.Khoa_QLL.text().strip()
        get_KhoaHK = self.KhoaHK_QLL.text().strip()
        get_HDT = self.HDT_QLL.text().strip()

        lop_info = {
            "MALOP": get_Malop,
            "TENLOP": get_TenLop,
            "KHOA": get_Khoa,
            "KHOAHK": get_KhoaHK,
            "HDT": get_HDT
        }

        return lop_info
    ##############################################################################
    def check_malop(self, new_malop):
        result = self.DB.search_info_lop(maloptk=new_malop)
        return result
    
    
if __name__ == '__main__':
    APP  = QApplication([])
    WINDOW = Window_Menu()
    WINDOW.show()
    APP.exec()
