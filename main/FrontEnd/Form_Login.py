# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Login(object):
    def setupLogin(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 720)
        Form.setStyleSheet("#Title_Login {\n"
"    background-color: cyan;\n"
"}\n"
"\n"
"#Main_Login {\n"
"    background-color: grey;\n"
"}\n"
"")
        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1261, 701))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.Title_Login = QtWidgets.QFrame(parent=self.frame)
        self.Title_Login.setGeometry(QtCore.QRect(10, 10, 291, 681))
        self.Title_Login.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Title_Login.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Title_Login.setObjectName("Title_Login")
        self.Main_Login = QtWidgets.QFrame(parent=self.frame)
        self.Main_Login.setGeometry(QtCore.QRect(300, 10, 951, 681))
        self.Main_Login.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Main_Login.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Main_Login.setObjectName("Main_Login")
        self.Frame_Login = QtWidgets.QFrame(parent=self.Main_Login)
        self.Frame_Login.setGeometry(QtCore.QRect(10, 10, 921, 651))
        self.Frame_Login.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Frame_Login.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Frame_Login.setObjectName("Frame_Login")
        self.ExitBtn = QtWidgets.QPushButton(parent=self.Frame_Login)
        self.ExitBtn.setGeometry(QtCore.QRect(510, 440, 75, 23))
        self.ExitBtn.setObjectName("ExitBtn")
        self.widget = QtWidgets.QWidget(parent=self.Frame_Login)
        self.widget.setGeometry(QtCore.QRect(360, 230, 135, 41))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.TaiKhoan_Entry_Login = QtWidgets.QLineEdit(parent=self.widget)
        self.TaiKhoan_Entry_Login.setObjectName("TaiKhoan_Entry_Login")
        self.gridLayout.addWidget(self.TaiKhoan_Entry_Login, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.widget1 = QtWidgets.QWidget(parent=self.Frame_Login)
        self.widget1.setGeometry(QtCore.QRect(360, 330, 135, 41))
        self.widget1.setObjectName("widget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.widget1)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.MatKhau_Entry_Login = QtWidgets.QLineEdit(parent=self.widget1)
        self.MatKhau_Entry_Login.setObjectName("MatKhau_Entry_Login")
        self.gridLayout_2.addWidget(self.MatKhau_Entry_Login, 1, 0, 1, 1)
        self.LoginBtn = QtWidgets.QPushButton(parent=self.Frame_Login)
        self.LoginBtn.setGeometry(QtCore.QRect(270, 440, 75, 23))
        self.LoginBtn.setObjectName("LoginBtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ExitBtn.setText(_translate("Form", "Thoat"))
        self.label.setText(_translate("Form", "Tai Khoan"))
        self.label_2.setText(_translate("Form", "Mat Khau"))
        self.LoginBtn.setText(_translate("Form", "Dang Nhap"))
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
