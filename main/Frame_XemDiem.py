from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem, QPushButton, QWidget, QApplication
from FrontEnd.Form_Menu import Menu
from Backend.Connection_Database import ConnectDB

class Window_Menu(QWidget):
    def __init__(self):
        super().__init__()

        self.UI = Menu()
        self.UI.setupMenu(self)
        
        self.user_id = "222010001"
        self.DB = ConnectDB()

        # Get references to widgets from UI
        self.Hocky_BD = self.UI.Hocky_Cbox_BD 
        self.Namhoc_BD = self.UI.NamHoc_Cbox_BD
        self.DTBHe4_BD = self.UI.DTB_He4_DB
        self.DTBHe10_BD = self.UI.DTB_He10_DB
        self.TongTinChi = self.UI.TongTinChi_BD
        self.listbox_BD = self.UI.tableWidget_BD  # Assign listbox_BD
        self.listbox_BD.setSortingEnabled(False)
        self.buttons_list_BD = self.UI.Frame_Listbox_BD.findChildren(QPushButton)

        # Connect dropdowns to display_data_BD method using lambda
        self.Hocky_BD.activated.connect(lambda: self.display_data_BD(self.user_id))
        self.Namhoc_BD.activated.connect(lambda: self.display_data_BD(self.user_id))
        
        self.UI.XemDiemBtn.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_BangDiem))

    def toggleForm(self, Frame, Form):
        Frame.setCurrentIndex(Frame.indexOf(Form))

    def display_data_BD(self, user_id):
        bangdiem_info = self.get_nhapdiem_info()
        search_result = self.DB.search_info_bangdiem(
            masvtk=user_id, 
            hockytk=bangdiem_info["HOCKY"], 
            namhoctk=bangdiem_info["NAMHOC"])

        self.show_data_BD(search_result)

    def show_data_BD(self, result):
        self.listbox_BD.clearContents()
        self.listbox_BD.setRowCount(0)

        if result:
            self.listbox_BD.setRowCount(len(result))
            for row, info in enumerate(result):
                info_list = [
                    info["MAMH"],
                    info["TENMH"],
                    info["SOTC"],
                    info["DIEMTK_HE10"],
                    info["DIEMTK_HE4"],
                    info["HOCKY"],
                    info["NAMHOC"],
                    info["TINHTRANG"]
                ]

                for column, item in enumerate(info_list):
                    cell_item = QTableWidgetItem(str(item))
                    self.listbox_BD.setItem(row, column, cell_item)

            self.DTBHe10_BD.setText(str(info["DIEMTB_HE10"]))
            self.DTBHe4_BD.setText(str(info["DIEMTB_HE4"]))
            self.TongTinChi.setText(str(info["TONGTINCHI"]))
        else:
            self.clear_listbox_and_entry_BD()

    def clear_listbox_and_entry_BD(self):
        self.listbox_BD.clearContents()
        self.listbox_BD.setRowCount(0) 
        self.DTBHe10_BD.setText("")
        self.DTBHe4_BD.setText("")
        self.TongTinChi.setText("")

    def get_nhapdiem_info(self):
        get_HocKy = self.Hocky_BD.currentText().strip()
        get_NamHoc = self.Namhoc_BD.currentText().strip()

        bangdiem_info = {
            "HOCKY": get_HocKy,
            "NAMHOC": get_NamHoc
        }

        return bangdiem_info

if __name__ == '__main__':
    app = QApplication([])
    window = Window_Menu()
    window.show()
    app.exec()
