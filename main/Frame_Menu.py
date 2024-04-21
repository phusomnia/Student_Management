from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem, QPushButton, QWidget, QApplication
from PyQt6.QtCore import QDate
from PyQt6.QtGui import QIntValidator
from FrontEnd.Form_Menu import Menu
from Backend.Connection_Database import ConnectDB

class Window_Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.UI = Menu()
        self.UI.setupMenu(self)
        #############################################################################
        # Ket noi den database
        self.DB = ConnectDB()
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
        ## NHAP MON
        self.MaMon_QLD = self.UI.MaMH_Entry_QLD
        self.MaNhom_QLD = self.UI.MaNhom_Entry_QLD
        self.NamHoc_QLD = self.UI.NamHoc_Cbox_QLD
        self.HocKy_QLD = self.UI.HocKy_CBox_QLD
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
        ## 
        self.search_btn_QLD = self.UI.SearchBtn_QLD
        self.update_btn_QLD = self.UI.UpdateBtn_QLD
        #############################################################################
        # INIT TABLE 
        ## SV
        self.listbox_QLSV = self.UI.tableWidget_QLSV
        self.listbox_QLSV.setSortingEnabled(False)
        self.buttons_list_QLSV = self.UI.Frame_Listbox_QLSV.findChildren(QPushButton)
        ## GV
        self.listbox_QLGV = self.UI.tableWidget_QLGV
        self.listbox_QLGV.setSortingEnabled(False)
        self.buttons_list_QLGV = self.UI.Frame_Listbox_QLGV.findChildren(QPushButton)
        ## LOP
        self.listbox_QLL = self.UI.tableWidget_QLL
        self.listbox_QLL.setSortingEnabled(False)
        self.buttons_list_QLL = self.UI.Frame_Listbox_QLL.findChildren(QPushButton)
        ## KHOA
        self.listbox_QLK = self.UI.tableWidget_QLK
        self.listbox_QLK.setSortingEnabled(False)
        self.buttons_list_QLK = self.UI.Frame_Listbox_QLK.findChildren(QPushButton)
        ## MON
        self.listbox_QLMH = self.UI.tableWidget_QLMH
        self.listbox_QLMH.setSortingEnabled(False)
        self.buttons_list_QLMH = self.UI.Frame_Listbox_QLMH.findChildren(QPushButton)
        ## NHAP DIEM
        self.listbox_QLD = self.UI.tableWidget_QLD
        self.listbox_QLD.setSortingEnabled(False)
        self.buttons_list_QLD = self.UI.Frame_Listbox_QLD.findChildren(QPushButton)
        #############################################################################
        # Init hide
        self.HideDropDown()
        self.init_signal_slot_toggle_dropdown()
        self.init_signal_slot_form()

        # Khoi tao cac chuc nang
        self.init_signal_slot()
        #############################################################################
        # Khoi tao hien thi du lieu dang co trong database
        self.display_data_QLSV()
        self.display_data_QLGV()
        self.display_data_QLL()
        self.display_data_QLK()
        self.display_data_QLMH()
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
        self.search_btn_QLD.clicked.connect(self.search_info_QLD)
    #############################################################################
    ## SV ## 
    def disable_buttons_QLSV(self):
        for button in self.buttons_list_QLSV:
            button.setDisabled(True)
    def enable_buttons_QLSV(self):
        for button in self.buttons_list_QLSV:
            button.setDisabled(False)
    ## GV ##
    def disable_buttons_QLGV(self):
        for button in self.buttons_list_QLGV:
            button.setDisabled(True)
    def enable_buttons_QLGV(self):
        for button in self.buttons_list_QLGV:
            button.setDisabled(False)
    ## LOP ##
    def disable_buttons_QLL(self):
        for button in self.buttons_list_QLL:
            button.setDisabled(True)
    def enable_buttons_QLL(self):
        for button in self.buttons_list_QLL:
            button.setDisabled(False)
    ## KHOA ##
    def disable_buttons_QLK(self):
        for button in self.buttons_list_QLK:
            button.setDisabled(True)
    def enable_buttons_QLK(self):
        for button in self.buttons_list_QLK:
            button.setDisabled(False)
    ## MON HOC ##
    def disable_buttons_QLMH(self):
        for button in self.buttons_list_QLMH:
            button.setDisabled(True)
    def enable_buttons_QLMH(self):
        for button in self.buttons_list_QLMH:
            button.setDisabled(False)
    #############################################################################
    ## SV ##
    #############################################################################
    def add_info_QLSV(self):
        self.disable_buttons_QLSV()

        sv_info = self.get_sv_info()

        if sv_info["MASV"] and sv_info["HOTEN"]:
            check_result = self.check_masv(new_masv=sv_info["MASV"])

            if check_result:
                QMessageBox.information(self, "Canh bao", "Nhap lai MaSV!", QMessageBox.StandardButton.Ok)
                self.enable_buttons_QLSV()
                return

            add_result = self.DB.add_info_sv(
                masv=sv_info["MASV"],
                hoten=sv_info["HOTEN"],
                lop=sv_info["LOP"],
                diachi=sv_info["DCHI"],
                ngsinh=sv_info["NGSINH"],
                gtinh=sv_info["GTINH"],
                sdt=sv_info["SDT"]
            )

            if add_result:
                QMessageBox.information(self, "Canh bao", f"Them : {add_result} that bai!.", QMessageBox.StandardButton.Ok)
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
                    hoten=new_sv_info["HOTEN"],
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
                    self.MaSV.clear()
                    self.Hoten_QLSV.clear()
                    self.Lop_QLSV.clear()
                    self.Dchi_QLSV.clear()
                    self.Ngsinh_QLSV.clear()
                    self.GTinh_QLSV.setCurrentIndex(0)
                    self.Sdt_QLSV.clear()
                    self.display_data_QLSV()
            else:
                QMessageBox.information(self, "Canh bao", f"Chon 1 sinh vien de cap nhat", QMessageBox.StandardButton.Ok)
    #############################################################################
    def select_info_QLSV(self):
        # CHON DU LIEU DE CHINH SUA
        select_row = self.listbox_QLSV.currentRow()
        if select_row != -1:
            self.MaSV.setEnabled(False)
            s_MaSV = self.listbox_QLSV.item(select_row, 0).text().strip()
            s_Hoten = self.listbox_QLSV.item(select_row, 1).text().strip()
            s_Lop =  self.listbox_QLSV.item(select_row, 2).text().strip()
            s_Dchi = self.listbox_QLSV.item(select_row, 3).text().strip()
            s_Ngsinh =  self.listbox_QLSV.item(select_row, 4).text().strip()
            s_Gtinh =  self.listbox_QLSV.item(select_row, 5).text().strip()
            s_Sdt =  self.listbox_QLSV.item(select_row, 6).text().strip()

            # Set du lieu moi
            self.MaSV.setText(s_MaSV)
            self.Hoten_QLSV.setText(s_Hoten)
            self.Lop_QLSV.setText(s_Lop)
            self.Dchi_QLSV.setText(s_Dchi)
            self.Ngsinh_QLSV.setDate(QDate.fromString(s_Ngsinh, 'yyyy-MM-dd'))
            self.GTinh_QLSV.setCurrentText(s_Gtinh)
            self.Sdt_QLSV.setText(s_Sdt)
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
    # def search_info_QLSV(self):
    #     sv_info = self.get_sv_info()

    #     search_result = self.DB.search_info(
    #         MaSVtk=sv_info["MaSV"],
    #         HotenSVtk=sv_info["HotenSV"],
    #         loptk=sv_info["LOP"],
    #         dchitk=sv_info["DCHI"],
    #         ngsinhtk=sv_info["NGSINH"],
    #         gtinhtk=sv_info["GTINH"],
    #         sdttk=sv_info["SDT"]
    #     )

    #     self.show_data_QLSV(search_result)
    #############################################################################
    def show_data_QLSV(self, result):
        # LAY DU LIEU TRONG DICT GAN VAO TABLE
        if result:
            self.listbox_QLSV.setRowCount(0)
            self.listbox_QLSV.setRowCount(len(result))

            for row, info in enumerate(result):
                info_list = [
                    info["MASV"],
                    info["HOTEN"],
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
            "HOTEN": get_Hoten, 
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
                magv=int(gv_info["MAGV"]),
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
    # #############################################################################            
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
    # #############################################################################
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
    # #############################################################################
    def check_malop(self, new_malop):
        result = self.DB.search_info_lop(maloptk=new_malop)
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
                gv=khoa_info["TRGKHOA"]
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
    ## NHAP DIEM ##
    #############################################################################
    def search_info_QLD(self):
        nhapdiem_info = self.get_nhapdiem_info()

        search_result = self.DB.search_info_nhapdiem(
                mamhtk= nhapdiem_info["MAMH"],
                manhomtk= nhapdiem_info["MANHOM"],
                hockytk= nhapdiem_info["HOCKY"],
                namhoctk= nhapdiem_info["NAMHOC"]
        )

        if search_result:
            self.show_data_QLD(search_result)
        else:
            self.clear_listbox_QLD()
    ############################################################################
    ## 
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
                    info["MANHOM"],
                    info["MASV"],
                    info["HOTEN"],
                    info["DIEM_QT"],
                    info["HESO_QT"],
                    info["DIEMTHI"],
                    info["HESO_THI"],
                    info["HOCKY"],
                    info["NAMHOC"]
                ]
                for column, item in enumerate(nhapdiem_info):
                    cell_item = QTableWidgetItem(str(item))
                    self.listbox_QLD.setItem(row, column, cell_item)
    #############################################################################
    # def display_data_QLD(self):
    #     ## LAY DU LIEU DE HIEN THI
    #     search_result = self.DB.search_info_nhapdiem()

    #     ## HIEN THI
    #     self.show_data_QLD(search_result)
    #############################################################################  
    def get_nhapdiem_info(self):
        get_MaMH = self.MaMon_QLD.text().strip()
        get_MaNhom = self.MaNhom_QLD.text().strip()
        get_HocKy = self.HocKy_QLD.currentText().strip()
        get_NamHoc = self.NamHoc_QLD.currentText().strip()

        diem_info = {
            "MAMH": get_MaMH,
            "MANHOM": get_MaNhom,
            "HOCKY": get_HocKy,
            "NAMHOC": get_NamHoc
        }

        return diem_info
    #############################################################################
    # an dropdown
    def HideDropDown(self):
        self.UI.SubFrame_AdminBtn.setHidden(True)
        self.UI.SubFrame_GVBtn.setHidden(True)
        self.UI.SubFrame_SVBtn.setHidden(True)
    #############################################################################
    # khoi tao toggle drop down
    def init_signal_slot_toggle_dropdown(self):
        self.UI.AdminBtn.clicked.connect(lambda: self.toggleDropDown(self.UI.SubFrame_AdminBtn))
        self.UI.SVBtn.clicked.connect(lambda: self.toggleDropDown(self.UI.SubFrame_SVBtn))
        self.UI.GVBtn.clicked.connect(lambda: self.toggleDropDown(self.UI.SubFrame_GVBtn))
    #############################################################################
    def toggleDropDown(self, Subframe):
        if Subframe.isVisible():
            Subframe.hide()
        else:
            Subframe.show()
    #############################################################################
    def init_signal_slot_form(self):
        self.UI.QLSVBtn.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_QLSV))
        self.UI.QLGVBtn.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_QLGV))
        self.UI.QLLBtn.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_QLL))
        self.UI.QLMHBtn.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_QLMH))
        self.UI.QLKBtn.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_QLK))
        self.UI.ChamDiemBtn.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_NhapDiem))
    #############################################################################
    def toggleForm(self, Frame, Form):
        Frame.setCurrentIndex(Frame.indexOf(Form))
    #############################################################################
if __name__ == '__main__':
    APP  = QApplication([])
    WINDOW = Window_Menu()
    WINDOW.show()
    APP.exec()
