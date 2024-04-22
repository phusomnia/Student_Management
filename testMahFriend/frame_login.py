import mysql.connector
import sys
from PyQt6.QtWidgets import QMessageBox, QWidget, QApplication
from PyQt6.QtCore import QDate
from PyQt6.QtGui import QValidator
from form_login import login
from connect_DB import ConnectDB

class LOGIN(QWidget):
    def __init__(self):
        super().__init__()

        self.UI = login()
        self.UI.setuplogin(self)

        self.DB = ConnectDB()

        self.username = self.UI.userentry

        self.password = self.UI.passentry

        self.dn = self.UI.log_in
        self.cancel = self.UI.exit

        self.init_signal_slot()

    def init_signal_slot(self):
        self.dn.clicked.connect(self.check_info)

    def disable_buttons(self):
        self.dn.setDisabled(True)

    def enable_buttons(self):
        self.dn.setDisabled(False)

    def check_info(self):
        get_username = self.username.text().strip()
        get_password = self.password.text().strip()

        if not get_username or not get_password:
            QMessageBox.information(self, "Cảnh báo", "Nhập tên đăng nhập và mật khẩu",
                                    QMessageBox.StandardButton.Ok)
            return

        search_result = self.DB.search_acc(get_username, get_password)
        if isinstance(search_result, Exception):
            QMessageBox.information(self, "thông báo", "thông tin không hợp lệ! ",
                                    QMessageBox.StandardButton.Ok)
        else:
            QMessageBox.information(self, "thông báo", "Đăng nhập thành công! ",
                                    QMessageBox.StandardButton.Ok)
            pass

if __name__ == '__main__':
    APP = QApplication(sys.argv)
    WINDOW = LOGIN()
    WINDOW.show()
    sys.exit(APP.exec())
