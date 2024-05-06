import sys
import pandas as pd
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem, QPushButton, QWidget, QApplication, QVBoxLayout
from PyQt6.QtCore import QDate
from PyQt6.QtGui import QIntValidator, QDoubleValidator
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import seaborn as sns
from FrontEnd.Form_Menu import Menu
from Backend.Connection_Database import ConnectDB

class Window_Menu(QWidget):
    def __init__(self, user_id):
        super(Window_Menu, self).__init__()

        self.user = user_id

        self.DB = ConnectDB()

        self.UI = Menu()
        self.UI.setupMenu(self)
        #############################################################################
        # INIT ENTRY
        ## TK ##
        self.MaTK = self.UI.MaTK_Entry_QLTK
        self.MatKhau = self.UI.MatKhau_Entry_QLTK
        ## SV ##
        self.MaSV = self.UI.MaSV_Entry_QLSV
        self.Hoten_QLSV = self.UI.TenSV_Entry_QLSV
        self.Ngsinh_QLSV = self.UI.NgSinh_Entry_QLSV
        self.GTinh_QLSV = self.UI.Gtinh_Cbox_QLSV
        self.Dchi_QLSV = self.UI.DiaChi_Entry_QLSV
        self.Sdt_QLSV = self.UI.Sdt_Entry_QLSV
        self.Lop_QLSV = self.UI.Lop_Entry_QLSV
        ## GV ##
        self.MaGV = self.UI.MaGV_Entry_QLGV
        self.Hoten_QLGV = self.UI.TenGV_Entry_QLGV
        self.Ngsinh_QLGV = self.UI.NgSinh_Entry_QLGV
        self.Gtinh_QLGV = self.UI.Gtinh_Cbox_QLGV
        self.Khoa_GLGV = self.UI.Khoa_Entry_QLGV
        ## LOP ##
        self.MaLop = self.UI.MaLop_Entry_QLL
        self.TenLop_QLL = self.UI.TenLop_Entry_QLL
        self.Khoa_QLL = self.UI.Khoa_Entry_QLL
        self.KhoaHK_QLL = self.UI.KhoaHK_Entry_QLL
        self.HDT_QLL = self.UI.HeDaoTao_Entry_QLL
        ## KHOA ##
        self.MaKhoa = self.UI.MaKhoa_Entry_QLK
        self.TenKhoa_QLK = self.UI.TenKhoa_Entry_QLK
        self.Sdt_QLK = self.UI.Sdt_Entry_QLK
        self.Phong_QLK = self.UI.Phong_Entry_QLK
        self.TrgKhoa_QLK = self.UI.TrgKhoa_Entry_QLK
        ## MON ##
        self.MaMon_QLMH = self.UI.MaMon_Entry_QLMH
        self.TenMon_QLMH = self.UI.TenMon_Entry_QLMH
        self.SoTinChi_QLMH = self.UI.SoTinChi_Entry_QLMH
        self.SoTinChi_QLMH.setValidator(QIntValidator())
        ## NHAP DIEM ## 
        self.MaMon_QLD = self.UI.MaMH_Entry_QLD
        self.MaNhom_QLD = self.UI.MaNhom_Entry_QLD
        self.MaSV_QLD = self.UI.MaSV_Entry_QLD
        self.DiemQT = self.UI.DiemQT_Entry_QLD
        self.DiemQT.setValidator(QDoubleValidator())
        self.HesoQT = self.UI.HSQT_Entry_QLD
        self.HesoQT.setValidator(QDoubleValidator())
        self.DiemThi = self.UI.DiemThi_Entry_QLD
        self.DiemThi.setValidator(QDoubleValidator())
        self.HesoThi = self.UI.HST_Entry_QLD
        self.HesoThi.setValidator(QDoubleValidator())
        ## THONG KE ## 
        self.Frame_BieuDo = self.UI.Frame_BieuDo
        self.MaMH_TKD = self.UI.MaMH_Entry_TKD
        self.chonBieudo = self.UI.BieuDo_CBox
        ## TTSV
        self.Frame_BieuDo_TTSV = self.UI.Frame_BieuDo_TTSV
        ## TTGV
        ## XEM DIEM
        self.Hocky_BD = self.UI.Hocky_Cbox_BD 
        self.Namhoc_BD = self.UI.NamHoc_Cbox_BD
        self.DTBHe4_BD = self.UI.DTB_He4_DB
        self.DTBHe10_BD = self.UI.DTB_He10_DB
        self.TongTinChi = self.UI.TongTinChi_BD
        #############################################################################
        # INIT BTN
        ## TK BTN
        self.add_btn_QLTK = self.UI.AddBtn_QLTK
        self.update_btn_QLTK = self.UI.UpdateBtn_QLTK
        self.delete_btn_QLTK = self.UI.DelBtn_QLTK
        ## SV BTN
        self.add_btn_QLSV = self.UI.AddBtn_QLSV
        self.update_btn_QLSV = self.UI.UpdateBtn_QLSV
        self.delete_btn_QLSV = self.UI.DelBtn_QLSV
        ## GV BTN
        self.add_btn_QLGV = self.UI.AddBtn_QLGV
        self.update_btn_QLGV = self.UI.UpdateBtn_GLGV
        self.delete_btn_QLGV = self.UI.DelBtn_QLGV
        ## LOP BTN
        self.add_btn_QLL = self.UI.AddBtn_QLL
        self.update_btn_QLL = self.UI.UpdateBtn_QLL
        self.delete_btn_QLL = self.UI.DelBtn_QLL
        ## KHOA BTN
        self.add_btn_QLK = self.UI.AddBtn_QLK
        self.update_btn_QLK = self.UI.UpdateBtn_QLK
        self.delete_btn_QLK = self.UI.DelBtn_QLK
        ## MONHOC BTN
        self.add_btn_QLMH = self.UI.AddBtn_QLMH
        self.update_btn_QLMH = self.UI.UpdateBtn_QLMH
        self.delete_btn_QLMH = self.UI.DelBtn_QLMH
        ## NHAP DIEM BTN
        self.search_btn_QLD = self.UI.SearchBtn_QLD
        self.update_btn_QLD = self.UI.UpdateBtn_QLD
        self.NamHoc_QLD = self.UI.NamHoc_Cbox_QLD
        self.HocKy_QLD = self.UI.HocKy_CBox_QLD
        ## THONG KE BTN
        self.search_btn_TKD = self.UI.SearchBtn_TKD
        ## XEM DIEM BTN
        self.Hocky_BD.activated.connect(lambda: self.display_data_BD(self.user))
        self.Namhoc_BD.activated.connect(lambda: self.display_data_BD(self.user))
        #############################################################################
        ## TK TABLE
        self.listbox_QLTK = self.UI.tableWidget_QLTK
        self.listbox_QLTK.setSortingEnabled(False)
        self.buttons_list_QLTK = self.UI.Frame_Listbox_QLTK.findChildren(QPushButton)
        ## SV TABLE
        self.listbox_QLSV = self.UI.tableWidget_QLSV
        self.listbox_QLSV.setSortingEnabled(False)
        self.buttons_list_QLSV = self.UI.Frame_Listbox_QLSV.findChildren(QPushButton)
        ## GV TABLE
        self.listbox_QLGV = self.UI.tableWidget_QLGV
        self.listbox_QLGV.setSortingEnabled(False)
        self.buttons_list_QLGV = self.UI.Frame_Listbox_QLGV.findChildren(QPushButton)
        ## LOP TABLE
        self.listbox_QLL = self.UI.tableWidget_QLL
        self.listbox_QLL.setSortingEnabled(False)
        self.buttons_list_QLL = self.UI.Frame_Listbox_QLL.findChildren(QPushButton)
        ## KHOA TABLE
        self.listbox_QLK = self.UI.tableWidget_QLK
        self.listbox_QLK.setSortingEnabled(False)
        self.buttons_list_QLK = self.UI.Frame_Listbox_QLK.findChildren(QPushButton)
        ## MON TABLE
        self.listbox_QLMH = self.UI.tableWidget_QLMH
        self.listbox_QLMH.setSortingEnabled(False)
        self.buttons_list_QLMH = self.UI.Frame_Listbox_QLMH.findChildren(QPushButton)
        ## NHAP DIEM TABLE
        self.listbox_QLD = self.UI.tableWidget_QLD
        self.listbox_QLD.setSortingEnabled(False)
        self.buttons_list_QLD = self.UI.Frame_Listbox_QLD.findChildren(QPushButton)
        ## XEM DIEM TABLE
        self.listbox_BD = self.UI.tableWidget_BD
        self.listbox_BD.setSortingEnabled(False)
        self.buttons_list_BD = self.UI.Frame_Listbox_BD.findChildren(QPushButton)
        #############################################################################
        # Init empty page
        # Init hide
        self.HideDropDown()
        self.init_signal_slot_toggle_dropdown(self.user)
        self.init_signal_slot_form()

        # Khoi tao cac chuc nang
        self.init_signal_slot()
        #############################################################################
        # Khoi tao hien thi du lieu dang co trong database
        # TK
        self.display_data_QLTK()
        # SV
        self.display_data_QLSV()
        # GV
        self.display_data_QLGV()
        # LOP
        self.display_data_QLL()
        # KHOA
        self.display_data_QLK()
        # MON
        self.display_data_QLMH()
    #############################################################################
    def init_signal_slot(self):
        ## TK 
        self.add_btn_QLTK.clicked.connect(self.add_info_QLTK)
        self.update_btn_QLTK.clicked.connect(self.update_info_QLTK)
        self.delete_btn_QLTK.clicked.connect(self.delete_info_QLTK)
        ## SV
        self.add_btn_QLSV.clicked.connect(self.add_info_QLSV)
        self.update_btn_QLSV.clicked.connect(self.update_info_QLSV)
        self.delete_btn_QLSV.clicked.connect(self.delete_info_QLSV)
        ## GV
        self.add_btn_QLGV.clicked.connect(self.add_info_QLGV)
        self.update_btn_QLGV.clicked.connect(self.update_info_QLGV)
        self.delete_btn_QLGV.clicked.connect(self.delete_info_QLGV)
        ## LOP
        self.add_btn_QLL.clicked.connect(self.add_info_QLL)
        self.update_btn_QLL.clicked.connect(self.update_info_QLL)
        self.delete_btn_QLL.clicked.connect(self.delete_info_QLL)
        ## KHOA
        self.add_btn_QLK.clicked.connect(self.add_info_QLK)
        self.update_btn_QLK.clicked.connect(self.update_info_QLK)
        self.delete_btn_QLK.clicked.connect(self.delete_info_QLK)
        ## MH
        self.add_btn_QLMH.clicked.connect(self.add_info_QLMH)
        self.update_btn_QLMH.clicked.connect(self.update_info_QLMH)
        self.delete_btn_QLMH.clicked.connect(self.delete_info_QLMH)
        ## TKD 
        self.search_btn_TKD.clicked.connect(self.on_search_button_clicked)
        ## NHAPDIEM
        self.search_btn_QLD.clicked.connect(self.search_info_QLD)
        # self.search_btn_QLD.clicked.connect(self.get_info_bangdiem_QLD)
        self.update_btn_QLD.clicked.connect(self.update_info_chitietbangdiem_QLD(self.user))
    #############################################################################
    ## DIS TK
    def disable_buttons_QLTK(self):
        for button in self.buttons_list_QLTK:
            button.setDisabled(True)
    def enable_buttons_QLTK(self):
        for button in self.buttons_list_QLTK:
            button.setDisabled(False)
    ## DIS SV 
    def disable_buttons_QLSV(self):
        for button in self.buttons_list_QLSV:
            button.setDisabled(True)
    def enable_buttons_QLSV(self):
        for button in self.buttons_list_QLSV:
            button.setDisabled(False)
    ## DIS GV 
    def disable_buttons_QLGV(self):
        for button in self.buttons_list_QLGV:
            button.setDisabled(True)
    def enable_buttons_QLGV(self):
        for button in self.buttons_list_QLGV:
            button.setDisabled(False)
    ## DIS LOP 
    def disable_buttons_QLL(self):
        for button in self.buttons_list_QLL:
            button.setDisabled(True)
    def enable_buttons_QLL(self):
        for button in self.buttons_list_QLL:
            button.setDisabled(False)
    ## DIS KHOA 
    def disable_buttons_QLK(self):
        for button in self.buttons_list_QLK:
            button.setDisabled(True)
    def enable_buttons_QLK(self):
        for button in self.buttons_list_QLK:
            button.setDisabled(False)
    ## DIS MON HOC
    def disable_buttons_QLMH(self):
        for button in self.buttons_list_QLMH:
            button.setDisabled(True)
    def enable_buttons_QLMH(self):
        for button in self.buttons_list_QLMH:
            button.setDisabled(False)
    #############################################################################
    # an dropdown
    def HideDropDown(self):
        self.UI.SubFrame_AdminBtn.setHidden(True)
        self.UI.SubFrame_GVBtn.setHidden(True)
        self.UI.SubFrame_SVBtn.setHidden(True)
    #############################################################################
    # khoi tao toggle drop down
    def init_signal_slot_toggle_dropdown(self, user_id):
        ## Tim acc sv trong qlsv
        info_acc_sv = self.DB.search_info_sv(masvtk=user_id)
        check_sv = ""
        if info_acc_sv != None:
            for info in info_acc_sv:
                print("Kiểm tra user_id: ", info["MASV"])
                check_sv = info["MASV"]
        info_acc_gv = self.DB.search_info_gv(magvtk=user_id)
        ## Tim acc sv trong qlgv
        check_gv = ""
        if info_acc_gv != None:
            for info in info_acc_gv:
                print("Kiểm tra user_id: ", info["MAGV"])
                check_gv = info["MAGV"]
        ## Phan quyen
        if user_id == 'ADMIN':
            self.UI.AdminBtn.clicked.connect(lambda: self.toggleDropDown(self.UI.SubFrame_AdminBtn))
        elif user_id == check_sv:
            self.UI.SVBtn.clicked.connect(lambda: self.toggleDropDown(self.UI.SubFrame_SVBtn))
            self.show_info(user_id)
            self.create_chart_sv(user_id)
        elif user_id == check_gv:
            self.UI.GVBtn.clicked.connect(lambda: self.toggleDropDown(self.UI.SubFrame_GVBtn))
            self.show_gv_info(user_id)
            self.search_info_QLD(user_id)
        else:
            QMessageBox.information(self, "Cảnh báo", "Tài khoản bị khóa hoặc không tồn tại", QMessageBox.StandardButton.Ok)
    ############################################################################
    # BAT TAT DROPDOWN
    def toggleDropDown(self, Subframe):
        if Subframe.isVisible():
            Subframe.hide()
        else:
            Subframe.show()
    #############################################################################
    # khoi tao chuyen form
    def init_signal_slot_form(self):
        ## TK TOGGLE
        self.UI.QLTKBtn.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_QLTK))
        ## SV TOGGLE
        self.UI.QLSVBtn.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_QLSV))
        ## GV TOGGLE
        self.UI.QLGVBtn.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_QLGV))
        ## LOP TOGGLE
        self.UI.QLLBtn.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_QLL))
        ## MON TOGGLE
        self.UI.QLMHBtn.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_QLMH))
        ## KHOA TOGGLE
        self.UI.QLKBtn.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_QLK))
        ## CHAMDIEM TOGGLE
        self.UI.ChamDiemBtn.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_NhapDiem))
        ## THONGKE TOGGLE
        self.UI.ThongKeBtn.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_ThongKeDiem))
        ## TTSV TOGGLE 
        self.UI.TTSVBtn.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_TTSV))
        ## TTGV TOGGLE
        self.UI.TTGVBtn.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_TTGV))
        ## XEM DIEM TOGGLE 
        self.UI.XemDiemBtn.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_BangDiem))
        ## NHAP DIEM TOGGLE
        self.UI.ChamDiemBtn.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_NhapDiem))
        ## TOGGLE THOAT
        self.UI.ExitBtn_QLSV.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_Init))
        self.UI.ExitBtn_QLL.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_Init))
        self.UI.ExitBtn_QLK.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_Init))
        self.UI.ExitBtn_QLGV.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_Init))
        self.UI.ExitBtn_QLD.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_Init))
        self.UI.ExitBtn_QLMH.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_Init))
        self.UI.ExitBtn_QLTK.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_Init))
    #############################################################################
    def toggleForm(self, Frame, Form):
        Frame.setCurrentIndex(Frame.indexOf(Form))
    #############################################################################
    #############################################################################
    ## TK ##
    #############################################################################
    def add_info_QLTK(self):
        self.disable_buttons_QLTK() 

        acc_info = self.get_acc_info()  

        if acc_info["USERNAME"] and acc_info["PASS"]:
            check_result = self.check_matk(new_matk=acc_info["USERNAME"])

            if check_result:
                QMessageBox.information(self, "Cảnh báo", "Nhập lại tài khoản!", QMessageBox.StandardButton.Ok)
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
            QMessageBox.information(self, "Cảnh báo", "Nhập tài khoản và mật khẩu", QMessageBox.StandardButton.Ok)

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
    #############################################################################
    #############################################################################
    ## SV ##
    #############################################################################
    def add_info_QLSV(self):
        self.disable_buttons_QLSV()

        sv_info = self.get_sv_info()

        if sv_info["MASV"] and sv_info["HOTENSV"]:
            check_result = self.check_masv(new_masv=sv_info["MASV"])

            if check_result:
                QMessageBox.information(self, "Cảnh báo", "Nhập lại mã sv!", QMessageBox.StandardButton.Ok)
                self.enable_buttons_QLSV()
                return

            add_result = self.DB.add_info_sv(
                masv=sv_info["MASV"],
                hoten=sv_info["HOTENSV"],
                ngsinh=sv_info["NGSINH"],
                gtinh=sv_info["GTINH"],
                diachi=sv_info["DCHI"],
                sdt=sv_info["SDT"],
                lop=sv_info["LOP"]
            )

            if add_result:
                QMessageBox.information(self, "Cảnh báo", f"Thêm : {add_result} thất bại!.", QMessageBox.StandardButton.Ok)
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
    #############################################################################
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
    #############################################################################
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
                    info["HOTENGV"],
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
    #############################################################################
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
    ##############################################################################
    ############################################################################# 
    ## THONG KE ## 
    ############################################################################# 
    def on_search_button_clicked(self):
        print("Test button") 
        self.create_chart_mh()
    ############################################################################# 
    def create_chart_mh(self):
        mamh = self.MaMH_TKD.text()

        if not self.check_mamh_exists(mamh):
            QMessageBox.warning(self, "Lỗi", "Mã môn học không tồn tại.")
            return

        mydb = self.DB.get_connection()
        mycursor = mydb.cursor()
        query = f"""
        SELECT chitietbangdiem.DIEMTB_HE10
        FROM sinhvien, chitietbangdiem, bangdiem, nhommonhoc
        WHERE sinhvien.MASV = bangdiem.SV
            AND bangdiem.MABD = chitietbangdiem.BD
            AND chitietbangdiem.NHOM = nhommonhoc.MANHOM
            AND nhommonhoc.MH = '{mamh}';
        """
        mycursor.execute(query)
        result = mycursor.fetchall()
        mycursor.close()
        mydb.close()
    #############################################################################
        if not result:
            QMessageBox.information(self, "Thông báo", "Môn học chưa được nhập điểm.")
            return

        df = pd.DataFrame(result, columns=['DIEMTB_HE10'])

        bieudo_option = self.chonBieudo.currentText()
        if bieudo_option == "Tròn":
            chart = self.create_pie_chart(df)
        else:
            chart = self.create_histogram(df)

        self.add_chart_to_frame(chart)
    #############################################################################
    def check_mamh_exists(self, mamh):
        mydb = self.DB.get_connection()
        mycursor = mydb.cursor()
        query = f"SELECT COUNT(*) FROM nhommonhoc WHERE MH = '{mamh}';"
        mycursor.execute(query)
        result = mycursor.fetchone()
        mycursor.close()
        mydb.close()
        return result[0] > 0
    #############################################################################
    def create_histogram(self, df):
        plt.figure(figsize=(8, 4.8))
        ax = plt.subplot()
        sns.histplot(df['DIEMTB_HE10'], ax=ax, color='skyblue', edgecolor='black', kde=True)
        ax.set_title('Biểu đồ Histogram và KDE của Điểm trung bình hệ 10')
        ax.set_xlabel('Điểm trung bình hệ 10')
        ax.set_ylabel('Số lượng sinh viên')
        plt.tight_layout()

        canvas = FigureCanvas(plt.gcf())
        plt.close()
        return canvas
    #############################################################################
    def create_pie_chart(self, df):
        count_gt_4 = (df['DIEMTB_HE10'] > 4).sum()
        count_lt_4 = (df['DIEMTB_HE10'] < 4).sum()

        labels = ['>4', '<4']
        sizes = [count_gt_4, count_lt_4]

        plt.figure(figsize=(6, 6))
        ax = plt.subplot()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        ax.axis('equal')
        ax.set_title('Phân phối điểm trên và dưới 4')
        plt.tight_layout()

        canvas = FigureCanvas(plt.gcf())
        plt.close()
        return canvas
    #############################################################################
    def add_chart_to_frame(self, chart):
        if self.Frame_BieuDo.layout() is not None:
            self.remove_current_chart()       
        layout = self.Frame_BieuDo.layout()
        if self.Frame_BieuDo.layout() is None:
            layout = QVBoxLayout()
            self.Frame_BieuDo.setLayout(layout)
        
        layout.addWidget(chart)
        self.current_chart = chart
    #############################################################################
    def remove_current_chart(self):
        if self.current_chart:
            self.Frame_BieuDo.layout().removeWidget(self.current_chart)
            self.current_chart.deleteLater()
            self.current_chart = None
    #############################################################################
    ## TTSV ## 
    #############################################################################
    def show_info(self, masv_search):
        search_result = self.DB.info_acc_sv(masv_search)
        if search_result:
            print("Search result:", search_result)
            for sv_info in search_result:
                masv = sv_info['MASV']
                tensv = sv_info['HOTENSV']
                ngaysinh = sv_info['NGSINH']
                gioitinh = sv_info['GTINH']
                sdt = sv_info['SDT']
                diachi = sv_info['DCHI']
                lop = sv_info['LOP']
                khoa = sv_info['TENKHOA']
                khoahoc = sv_info['KHOAHOC']
                hedaotao = sv_info['HEDAOTAO']

                self.display_info_sv(str(masv), tensv, ngaysinh.strftime('%d-%m-%Y'), gioitinh, diachi, sdt, lop, khoa, khoahoc, hedaotao)
        else:
            print("No data found for the provided search criteria.")
    #############################################################################
    def display_info_sv(self, id, name, date, gtinh, diachi ,sdt, lop, khoa, khoahoc, hedaotao):
        self.UI.MaSV_Entry_TTSV.setText(id)
        self.UI.Hoten_Entry_TTSV.setText(name)
        self.UI.NgSinh_Entry_TTSV.setText(date)
        self.UI.Gtinh_Entry_TTSV.setText(gtinh)
        self.UI.DiaChi_Entry_TTSV.setText(diachi)
        self.UI.Sdt_Entry_TTSV.setText(sdt)
        self.UI.Lop_Entry_TTSV.setText(lop)
        self.UI.Khoa_Entry_TTSV.setText(khoa)
        self.UI.KhoaHK_Entry_TTSV.setText(khoahoc)
        self.UI.HDT_Entry_TTSV.setText(hedaotao)
        print("Labels text set successfully.")
    #############################################################################
    def create_chart_sv(self, masv_search):
        result = self.DB.ketqua(masv_search)
        if result:
            df = pd.DataFrame(result, columns=['TENMH', 'DIEMTB_HE10'])
            fig, ax = plt.subplots(figsize=(10, 6))
            monhoc = df['TENMH']
            diem = df['DIEMTB_HE10']

            ax.bar( monhoc, diem, color='skyblue')

            ax.set_ylabel('Điểm')
            ax.set_xlabel('Môn học')
            ax.set_title('Biểu đồ điểm của sinh viên')

            canvas = FigureCanvas(fig)
            self.Frame_BieuDo_TTSV.addWidget(canvas)
        else:
            print("Không có dữ liệu nào được trả về từ cơ sở dữ liệu.")
    #############################################################################
    #############################################################################
    ## TTGV ## 
    #############################################################################
    def show_gv_info(self, magv_search):
        search_result = self.DB.search_acc_gv(magv_search)

        if search_result:
            print(search_result)
            for gv_info in search_result:
                magv = gv_info['MAGV']
                tengv = gv_info['HOTENGV']
                ngaysinh = gv_info['NGSINH']
                gioitinh = gv_info['GTINH']
                # khoa = gv_info['KHOA']
                tenkhoa = gv_info['TENKHOA']

            self.display_info_gv(magv, tengv, ngaysinh.strftime('%d-%m-%Y'), gioitinh, tenkhoa)
        else:
            print("Không thể hiện thị dữ liệu...")
    #############################################################################
    def display_info_gv(self, magv, tengv, ngaysinh, gioitinh, tenkhoa):
        self.UI.MaGV_Entry_TTGV.setText(magv)
        self.UI.Hoten_Entry_TTGV.setText(tengv)
        self.UI.Ngsinh_Entry_TTGV.setText(ngaysinh)
        self.UI.Gtinh_Entry_TTGV.setText(gioitinh)
        # ma_ten_khoa = f"{khoa} - {tenkhoa}"
        # self.UI.Khoa_Entry_TTGV.setText(ma_ten_khoa)
        self.UI.Khoa_Entry_TTGV.setText(tenkhoa)

        if self.DB.check_truongkhoa(magv):
            chucvu = "Trưởng Khoa"
            self.UI.Chuc_Vu_TTGV.setText(chucvu)
        else:
            chucvu = "Giảng viên"
            self.UI.Chuc_Vu_TTGV.setText(chucvu)
    #############################################################################
    #############################################################################
    ## XEM DIEM ## 
    #############################################################################
    def show_data_BD(self, result):
        if result:
            self.listbox_BD.clearContents()
            self.listbox_BD.setRowCount(0)
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
    #############################################################################
    def display_data_BD(self, user_id):
        # Lay du lieu tu entry
        bangdiem_info = self.get_xemdiem_info()
        # tim du lieu bang dict, masv can cu theo id_user
        search_result = self.DB.search_info_bangdiem(
            masvtk=user_id, 
            hockytk=bangdiem_info["HOCKY"], 
            namhoctk=bangdiem_info["NAMHOC"])

        self.show_data_BD(search_result)
    #############################################################################
    def clear_listbox_and_entry_BD(self):
        self.listbox_BD.clearContents()
        self.listbox_BD.setRowCount(0) 
        self.DTBHe10_BD.setText("")
        self.DTBHe4_BD.setText("")
        self.TongTinChi.setText("")
    #############################################################################
    def get_xemdiem_info(self):
        get_HocKy = self.Hocky_BD.currentText().strip()
        print(get_HocKy)
        get_NamHoc = self.Namhoc_BD.currentText().strip()
        print(get_NamHoc)

        bangdiem_info = {
            "HOCKY": get_HocKy,
            "NAMHOC": get_NamHoc
        }

        return bangdiem_info
    #############################################################################
    #############################################################################
    ## NHAP DIEM ##
    #############################################################################
    def update_info_chitietbangdiem_QLD(self, user_id):
        if self.MaMon_QLD.isEnabled():
            self.select_info_QLD()
        else:
            new_info_ctbd = self.get_nhapdiem_info()
            if new_info_ctbd["MAMH"]:
                # Mo rong phuong thuc de tinh diemtb he4, diem chu, xep loai
                diem_qt = float(new_info_ctbd["DIEM_QT"])
                diem_thi = float(new_info_ctbd["DIEMTHI"])
                heso_qt = float(new_info_ctbd["HESO_QT"])
                heso_thi = float(new_info_ctbd["HESO_THI"])
                diemtb_he10 = ((diem_qt*heso_qt) + (diem_thi*heso_thi))
                # Convert diemtb_10 sang diemtb_he4
                if diemtb_he10 >= 8.5 and diemtb_he10 <= 10: 
                    diemtb_he4 = 4.0
                    xeploai = 'A'
                    tinhtrang = 'Đạt'
                elif diemtb_he10 >= 7.0 and diemtb_he10 <= 8.4:
                    diemtb_he4 = 3.0
                    xeploai = 'B'
                    tinhtrang = 'Đạt'
                elif diemtb_he10 >= 5.5 and diemtb_he10 <= 6.9:
                    diemtb_he4 = 2.0
                    xeploai = 'C'
                    tinhtrang = 'Đạt'
                elif diemtb_he10 >= 4.0 and diemtb_he10 <= 5.4:
                    diemtb_he4 = 1.0
                    xeploai = 'D'
                    tinhtrang = 'Đạt'
                    danhgia = ''
                else:
                    diemtb_he4 = 0.0
                    xeploai = 'F'
                    tinhtrang = 'Trượt'
                    danhgia = 'NULL'
                print(diem_qt, diem_thi, heso_qt, heso_thi, diemtb_he10, xeploai, tinhtrang)
                
                result_bangdiem = self.get_info_bangdiem_QLD()
                
                # Tim tong tinh chi mot hoc ky, tong dtb_he4, tong dtb_he10
                for new_info_bd in result_bangdiem:
                    tong_tc_hk = int(new_info_bd["SUM(MH.SOTC)"])
                    tk_he10 = round(float(new_info_bd["SUM(CTBD.DIEMTB_HE10*MH.SOTC)"]) / tong_tc_hk, 2)
                    tk_he4 = round(float(new_info_bd["SUM(CTBD.DIEMTB_HE4*MH.SOTC)"])/tong_tc_hk, 2)
                if tk_he4 >= 2.0 and tk_he4 <= 2.49:
                    danhgia = 'Trung bình'
                elif tk_he4 >= 2.5 and tk_he4 <= 3.19:
                    danhgia = 'Khá'
                elif tk_he4 >= 3.2 and tk_he4 <= 3.59:
                    danhgia = 'Giỏi'
                elif tk_he4 >= 3.2 and tk_he4 <= 3.59:
                    danhgia = 'Xuất xắc'
                else:
                    danhgia = 'NULL'
                print(tong_tc_hk, tk_he10, tk_he4, danhgia)

                # Tinh tong tinh chi tat ca nam hoc, diem trung binh tich luy ca nam hoc
                # tongtc = 0
                # tong_tbtl_he4 = 0
                # for sem in range(1):
                #     for year in range(2023):
                #         infos = self.DB.search_info_bd_nhapdiem(
                #             masvtk=new_info_ctbd["MASV"], 
                #             hockytk=sem, 
                #             namhoctk=year
                #         )
                #     for info in infos:
                #         tongtc_hk = info["SUM(MH.SOTC)"]
                #         tongdiem_he4 = info["SUM(CTBD.DIEMTB_HE4*MH.SOTC)"]
                #         tong_tbtl_he4 += tongdiem_he4
                #         tongtc += tongtc_hk

                # print("Thong tin: {} {} {} {}\n". format(tongtc,tong_tbtl_he4,diemtb_tl,danhgia))

                if 0 <= diem_qt <= 10 and 0 <= diem_thi <= 10 and 0 <= heso_qt <= 1.0 and 0 <= heso_thi <= 1.0 and (heso_qt + heso_thi) == 1.0:
                    update_result_ctbd = self.DB.update_info_nhapdiem(
                        new_info_ctbd["MAMH"],
                        new_info_ctbd["MANHOM"],
                        new_info_ctbd["MASV"],
                        diem_qt,
                        heso_qt,
                        diem_thi,
                        heso_thi,
                        diemtb_he10,
                        diemtb_he4,
                        xeploai,
                        tinhtrang
                    )

                    update_result_bd = self.DB.update_info_bd_nhapdiem(
                        new_info_ctbd["MASV"],
                        new_info_ctbd["HOCKY"],
                        new_info_ctbd["NAMHOC"],
                        tk_he10,
                        tk_he4,
                        tk_he4,
                        tong_tc_hk,
                        danhgia
                    )

                    if update_result_ctbd:
                        QMessageBox.information(self, "Cảnh báo", f"Cập nhật: {update_result_ctbd} thất bại!", QMessageBox.StandardButton.Ok)
                    elif update_result_bd:
                        QMessageBox.information(self, "Cảnh báo", f"Cập nhật: {update_result_bd} thất bại!", QMessageBox.StandardButton.Ok)
                    else:
                        self.MaMon_QLD.setEnabled(True)
                        self.MaNhom_QLD.setEnabled(True)
                        self.MaSV_QLD.setEnabled(True)
                        self.search_info_QLD(user_id)
                        self.MaMon_QLD.clear()
                        self.MaNhom_QLD.clear()
                        self.MaSV_QLD.clear()
                        self.DiemQT.clear()
                        self.HesoQT.clear()
                        self.DiemThi.clear()
                        self.HesoThi.clear()
                else:
                    QMessageBox.information(self, "Cảnh báo", "Điểm thi và điểm quá trình từ 1-10. Hệ số quá trình vả hệ số thi tổng bằng 1.0", QMessageBox.StandardButton.Ok)
            else:
                QMessageBox.information(self, "Cảnh báo", "Chọn 1 sinh viên để cập nhật điểm", QMessageBox.StandardButton.Ok)
    #############################################################################
    def get_info_bangdiem_QLD(self):
        new_info_ctbd = self.get_nhapdiem_info() 
        result_bangdiem = self.DB.search_info_bd_nhapdiem(
            masvtk=new_info_ctbd["MASV"],
            hockytk=new_info_ctbd["HOCKY"],
            namhoctk=new_info_ctbd["NAMHOC"]
        )
        return result_bangdiem
    #############################################################################
    def select_info_QLD(self):
        select_row = self.listbox_QLD.currentRow()
        if select_row != -1:
            self.MaMon_QLD.setEnabled(False)
            self.MaNhom_QLD.setEnabled(False)
            self.MaSV_QLD.setEnabled(False)
            s_MaMon_QLD = self.listbox_QLD.item(select_row, 1).text().strip()
            s_MaNhom_QLD = self.listbox_QLD.item(select_row, 3).text().strip()
            s_MaSV_QLD = self.listbox_QLD.item(select_row, 4).text().strip()
            s_DiemQT_QLD = self.listbox_QLD.item(select_row, 6).text().strip()
            s_HSQT_QLD = self.listbox_QLD.item(select_row, 7).text().strip()
            s_DiemThi_QLD = self.listbox_QLD.item(select_row, 8).text().strip()
            s_HST_QLD = self.listbox_QLD.item(select_row, 9).text().strip()
            s_Hocky_QLD = self.listbox_QLD.item(select_row, 18).text().strip()
            s_NamHoc_QLD = self.listbox_QLD.item(select_row, 19).text().strip()

            self.MaMon_QLD.setText(s_MaMon_QLD)
            self.MaNhom_QLD.setText(s_MaNhom_QLD)
            self.MaSV_QLD.setText(s_MaSV_QLD)
            self.DiemQT.setText(s_DiemQT_QLD)
            self.HesoQT.setText(s_HSQT_QLD)
            self.DiemThi.setText(s_DiemThi_QLD)
            self.HesoThi.setText(s_HST_QLD)
            self.HocKy_QLD.setCurrentText(s_Hocky_QLD)
            self.NamHoc_QLD.setCurrentText(s_NamHoc_QLD)
        else:
            QMessageBox.information(self, "Cảnh báo", "Hãy chọn 1 môn", QMessageBox.StandardButton.Ok)
    ##############################################################################
    def search_info_QLD(self, user_id):
        nhapdiem_info = self.get_nhapdiem_info()

        search_result = self.DB.search_info_ctdb_nhapdiem(
            magvtk=user_id, #user_id
            mamhtk= nhapdiem_info["MAMH"],
            manhomtk= nhapdiem_info["MANHOM"],
            masvtk= nhapdiem_info["MASV"],
            hockytk= nhapdiem_info["HOCKY"],
            namhoctk= nhapdiem_info["NAMHOC"]
        )

        if search_result:
            self.show_data_QLD(search_result)
        else:
            self.clear_listbox_QLD()
    ############################################################################s
    def clear_listbox_QLD(self):
        self.listbox_QLD.clearContents()
        self.listbox_QLD.setRowCount(0) 
    ############################################################################
    ##  HIEN THI NHAP DIEM
    def show_data_QLD(self, result):
        if result:
            self.listbox_QLD.setRowCount(0)
            self.listbox_QLD.setRowCount(len(result))

            for row, info in enumerate(result):
                nhapdiem_info = [
                    info["MAGV"],
                    info["MAMH"],
                    info["SOTC"],
                    info["NHOM"],
                    info["MASV"],
                    info["HOTENSV"],
                    info["DIEM_QT"],
                    info["HESO_QT"],
                    info["DIEMTHI"],
                    info["HESO_THI"],
                    info["DIEMTB_HE10"],
                    info["DIEMTB_HE4"],
                    info["XEPLOAI"],
                    info["TINHTRANG"],
                    info["DIEMTK_HE10"],
                    info["DIEMTK_HE4"],
                    info["DIEMTB_TL"],
                    info["XEPLOAIHK"],
                    info["HOCKY"],
                    info["NAMHOC"]
                ]
                for column, item in enumerate(nhapdiem_info):
                    cell_item = QTableWidgetItem(str(item))
                    self.listbox_QLD.setItem(row, column, cell_item)
    #############################################################################
    # def display_data_QLD(self):
    #     ## LAY DU LIEU DE HIEN THI
    #     search_result = self.DB.search_info_ctdb_nhapdiem(
    #         magvtk="GV01001"
    #     )
    #     ## HIEN THI
    #     self.show_data_QLD(search_result)
    #############################################################################  
    def get_nhapdiem_info(self):
        get_MaMH = self.MaMon_QLD.text().strip()
        get_MaNhom = self.MaNhom_QLD.text().strip()
        get_MaSV = self.MaSV_QLD.text().strip()
        get_DiemQT = self.DiemQT.text().strip()
        get_HSQT = self.HesoQT.text().strip()
        get_DiemThi = self.DiemThi.text().strip()
        get_HST = self.HesoThi.text().strip()
        get_HocKy = self.HocKy_QLD.currentText().strip()
        get_NamHoc = self.NamHoc_QLD.currentText().strip()
        print(get_MaMH, get_MaNhom, get_DiemQT, get_HSQT, get_DiemThi, get_HST, get_MaSV, get_HocKy, get_NamHoc)

        diem_info = {
            "MAMH": get_MaMH,
            "MANHOM": get_MaNhom,
            "MASV": get_MaSV,
            "DIEM_QT": get_DiemQT,
            "HESO_QT":  get_HSQT,
            "DIEMTHI": get_DiemThi,
            "HESO_THI": get_HST,
            "HOCKY": get_HocKy,
            "NAMHOC": get_NamHoc
        }

        return diem_info
    #############################################################################
if __name__ == '__main__':
    APP  = QApplication([])
    WINDOW = Window_Menu()
    WINDOW.show()
    APP.exec()
