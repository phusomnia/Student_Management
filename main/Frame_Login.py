from PyQt6.QtWidgets import QMessageBox, QWidget, QApplication
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QMouseEvent, QIcon, QPixmap
from FrontEnd.Form_Login import Login
from Backend.Connection_Database import ConnectDB
from Frame_Menu import Window_Menu

class LoginWindow(QWidget):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.UI = Login()
        self.UI.setupLogin(self)

        self.DB = ConnectDB()

        self.UI.LoginBtn.clicked.connect(self.on_loginBtn_clicked)
        self.UI.ExitBtn.clicked.connect(self.on_exitBtn_clicked)
    #############################################################################
    def on_loginBtn_clicked(self):
        print("Onclick đăng nhập")
        username = self.UI.TaiKhoan_Entry_Login.text().strip()
        password = self.UI.MatKhau_Entry_Login.text().strip()

        if username and password:
            result = self.DB.check_username(username)
            if result and len(result) == 1:
                if result[0]["PASS"] == password:
                    user_id = result[0]["USERNAME"]
                    # pass the user_id to main window and show it.
                    main_window = Window_Menu(user_id)
                    main_window.show()
                    self.close()
                else:
                    QMessageBox.information(self, "Cảnh báo", "Mật khẩu sai, vui lòng nhập lại!", QMessageBox.StandardButton.Ok)
                    self.UI.MatKhau_Entry_Login.clear()
            else:
                QMessageBox.information(self, "Cảnh báo", "Tài khoản sai, vui lòng nhập lại.", QMessageBox.StandardButton.Ok)
                self.UI.TaiKhoan_Entry_Login.clear()
                self.UI.MatKhau_Entry_Login.clear()
        else:
            QMessageBox.information(self, "Cảnh báo", "Vui lòng nhập tài khoản và mật khẩu", QMessageBox.StandardButton.Ok)
    #############################################################################
    def on_exitBtn_clicked(self):
        reply = QMessageBox.question(self, "Exit", "Are you sure to exit?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.close()

if __name__ == "__main__":
    APP  = QApplication([])
    WINDOW = LoginWindow()
    WINDOW.show()
    APP.exec()
