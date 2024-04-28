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
        ## TK ##
        self.MaTK = self.UI.MaTK_Entry_QLTK
        self.MatKhau = self.UI.MatKhau_Entry_QLTK
        #############################################################################
        ## TK BTN
        self.add_btn_QLTK = self.UI.AddBtn_QLTK
        self.update_btn_QLTK = self.UI.UpdateBtn_QLTK
        self.delete_btn_QLTK = self.UI.DelBtn_QLTK
        #############################################################################
        ## TK TABLE
        self.listbox_QLTK = self.UI.tableWidget_QLTK
        self.listbox_QLTK.setSortingEnabled(False)
        self.buttons_list_QLTK = self.UI.Frame_Listbox_QLTK.findChildren(QPushButton)
        #############################################################################
        self.display_data_QLTK()
        #############################################################################
        self.add_btn_QLTK.clicked.connect(self.add_info_QLTK)
        self.update_btn_QLTK.clicked.connect(self.update_info_QLTK)
        self.delete_btn_QLTK.clicked.connect(self.delete_info_QLTK)
        #############################################################################
        self.UI.QLTKBtn.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_QLTK))
    #############################################################################
    def toggleForm(self, Frame, Form):
        Frame.setCurrentIndex(Frame.indexOf(Form))
    #############################################################################
    def disable_buttons_QLTK(self):
        for button in self.buttons_list_QLTK:
            button.setDisabled(True)
    def enable_buttons_QLTK(self):
        for button in self.buttons_list_QLTK:
            button.setDisabled(False)
    #############################################################################
    ## TK ##
    #############################################################################
    def add_info_QLTK(self):
        self.disable_buttons_QLTK() 

        acc_info = self.get_acc_info()  

        if acc_info["USERNAME"] and acc_info["PASS"]:
            check_result = self.check_matk(new_matk=acc_info["USERNAME"])

            if check_result:
                QMessageBox.information(self, "Canh bao", "Nhap lai ma mon hoc!", QMessageBox.StandardButton.Ok)
                self.enable_buttons_QLMH()
                return

            add_result = self.DB.add_info_acc(
                matk=acc_info["USERNAME"],
                matkhau=acc_info["PASS"]
            )

            if add_result:
                QMessageBox.information(self, "Cảnh báo", f"Thêm : {add_result} thất bại!.", QMessageBox.StandardButton.Ok)
            else:
                    self.MaTK.setEnabled(True)
                    self.MatKhau.clear()
                    self.display_data_QLTK()
        else:
            QMessageBox.information(self, "Cảnh báo", "Nhập mã và tên môn học", QMessageBox.StandardButton.Ok)

        self.display_data_QLTK()  
        self.enable_buttons_QLTK()
    #############################################################################
    def update_info_QLTK(self):
        if self.MaTK.isEnabled():
            # Kiem tra xem da chon dong nao chua
            self.select_info_QLTK()
        else:
            new_acc_info = self.get_acc_info()

            if new_acc_info["USERNAME"]:
                update_result = self.DB.update_info_acc(
                    matk=new_acc_info["USERNAME"],
                    matkhau=new_acc_info["PASS"]
                )

                if update_result:
                    QMessageBox.information(self, "Cảnh báo", f"Cập nhật: {update_result} thất bại!", QMessageBox.StandardButton.Ok)
                else:
                    self.MaTK.setEnabled(True)
                    self.MaTK.clear()
                    self.MatKhau.clear()
                    self.display_data_QLTK()
            else:
                QMessageBox.information(self, "Cảnh báo", f"Chọn 1 tài khoản để cập nhật", QMessageBox.StandardButton.Ok)
    #############################################################################
    def select_info_QLTK(self):
        # CHON DU LIEU DE CHINH SUA
        select_row = self.listbox_QLTK.currentRow()
        if select_row != -1:
            self.MaTK.setEnabled(False)
            s_MaTK = self.listbox_QLTK.item(select_row, 0).text().strip()
            s_MatKhau = self.listbox_QLTK.item(select_row, 1).text().strip()
            # Set du lieu moi
            self.MaTK.setText(s_MaTK)
            self.MatKhau.setText(s_MatKhau)
        else:
            QMessageBox.information(self, "Cảnh báo", "Hãy chọn 1 tài khoản", QMessageBox.StandardButton.Ok)
    #############################################################################
    def delete_info_QLTK(self):
        # CHON DONG HIEN TAI
        select_row = self.listbox_QLTK.currentRow()
        if select_row != -1:
            selected_option = QMessageBox.warning(self, "Cảnh báo", "Bạn muốn xóa dữ liệu?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
                MaTK = self.listbox_QLTK.item(select_row, 0).text().strip()
                delete_result = self.DB.delete_info_acc(MaTK)

                if not delete_result:
                    self.listbox_QLTK.removeRow(select_row)
                else:
                    QMessageBox.information(self, "Cảnh báo", f"Thất bại xóa {delete_result}! hãy thử lại.", QMessageBox.StandardButton.Ok)

        else:
            QMessageBox.information(self, "Cảnh báo", "Hãy chọn 1 tài khoản để xóa", QMessageBox.StandardButton.Ok)
    #############################################################################
    def show_data_QLTK(self, result):
        if result:
            self.listbox_QLTK.setRowCount(0)
            self.listbox_QLTK.setRowCount(len(result))

            for row, info in enumerate(result):
                info_list = [
                    info["USERNAME"],
                    info["PASS"]
                ]

                for column, item in enumerate(info_list):
                    cell_item = QTableWidgetItem(str(item))
                    self.listbox_QLTK.setItem(row, column, cell_item)
    #############################################################################
    def display_data_QLTK(self):
        search_result = self.DB.search_info_acc()

        self.show_data_QLTK(search_result)
    #############################################################################
    def get_acc_info(self):
        get_MaTK = self.MaTK.text().strip()
        get_MatKhau = self.MatKhau.text().strip()

        acc_info = {
            "USERNAME": get_MaTK,
            "PASS": get_MatKhau
        }

        return acc_info
    #############################################################################
    def check_matk(self, new_matk):
        result = self.DB.search_info_acc(usernametk=new_matk)
        return result
if __name__ == '__main__':
    APP  = QApplication([])
    WINDOW = Window_Menu()
    WINDOW.show()
    APP.exec()
