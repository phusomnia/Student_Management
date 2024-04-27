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

        self.user_id = user_id

        self.DB = ConnectDB()

        self.UI = Menu()
        self.UI.setupMenu(self)
        #############################################################################
        # INIT ENTRY 
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
        ## NHAP DIEM
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
        self.NamHoc_QLD = self.UI.NamHoc_Cbox_QLD
        self.HocKy_QLD = self.UI.HocKy_CBox_QLD
        ## THONG KE
        self.Frame_BieuDo = self.UI.Frame_BieuDo
        self.MaMH_TKD = self.UI.MaMH_Entry_TKD
        self.chonBieudo = self.UI.BieuDo_CBox
        #############################################################################
        # INIT BTN
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
        ## THONG KE BTN
        self.search_btn_TKD = self.UI.SearchBtn_TKD
        #############################################################################
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
        #############################################################################
        # Init empty page
        # Init hide
        self.HideDropDown()
        self.init_signal_slot_toggle_dropdown(user_id)
        self.init_signal_slot_form()

        # Khoi tao cac chuc nang
        # self.init_signal_slot()
        #############################################################################
        # Khoi tao hien thi du lieu dang co trong database
        ## SV
        # self.display_data_QLSV()
        ## GV
        # self.display_data_QLGV()
        ## LOP
        # self.display_data_QLL()
        ## KHOA
        # self.display_data_QLK()
        ## MON
        # self.display_data_QLMH()
    #############################################################################
    def init_signal_slot(self):
        self.add_btn_QLSV.clicked.connect(self.add_info_QLSV)
        self.update_btn_QLSV.clicked.connect(self.update_info_QLSV)
        self.delete_btn_QLSV.clicked.connect(self.delete_info_QLSV)
        self.add_btn_QLGV.clicked.connect(self.add_info_QLGV)
        self.update_btn_QLGV.clicked.connect(self.update_info_QLGV)
        self.delete_btn_QLGV.clicked.connect(self.delete_info_QLGV)
        self.add_btn_QLL.clicked.connect(self.add_info_QLL)
        self.update_btn_QLL.clicked.connect(self.update_info_QLL)
        self.delete_btn_QLL.clicked.connect(self.delete_info_QLL)
        self.add_btn_QLK.clicked.connect(self.add_info_QLK)
        self.update_btn_QLK.clicked.connect(self.update_info_QLK)
        self.delete_btn_QLK.clicked.connect(self.delete_info_QLK)
        self.add_btn_QLMH.clicked.connect(self.add_info_QLMH)
        self.update_btn_QLMH.clicked.connect(self.update_info_QLMH)
        self.delete_btn_QLMH.clicked.connect(self.delete_info_QLMH)
        ## TKD 
        self.search_btn_TKD.clicked.connect(self.on_search_button_clicked)
        ## NHAPDIEM
        self.search_btn_QLD.clicked.connect(self.search_info_QLD)
        self.update_btn_QLD.clicked.connect(self.update_info_QLD)
    #############################################################################
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
        if self.DB.check_username(user_id):
            self.UI.AdminBtn.clicked.connect(lambda: self.toggleDropDown(self.UI.SubFrame_AdminBtn))
        else:
            self.UI.SVBtn.clicked.connect(lambda: self.toggleDropDown(self.UI.SubFrame_SVBtn))
            self.UI.GVBtn.clicked.connect(lambda: self.toggleDropDown(self.UI.SubFrame_GVBtn))
    #############################################################################
    # BAT TAT DROPDOWN
    def toggleDropDown(self, Subframe):
        if Subframe.isVisible():
            Subframe.hide()
        else:
            Subframe.show()
    #############################################################################
    # khoi tao chuyen form
    def init_signal_slot_form(self):
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
    #############################################################################
    def toggleForm(self, Frame, Form):
        Frame.setCurrentIndex(Frame.indexOf(Form))
    

if __name__ == '__main__':
    APP  = QApplication([])
    WINDOW = Window_Menu()
    WINDOW.show()
    APP.exec()
