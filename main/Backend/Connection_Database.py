import mysql.connector
from PyQt6.QtWidgets import QMessageBox

class ConnectDB:
    def __init__(self):
        self._host = "localhost"
        self._port = 3306
        self._user = "root"
        self._database = "dulieu"
        self.con = None
        self.cursor = None
    # Ket noi den mysql

    def get_connection(self):
        return mysql.connector.connect(
            host='localhost',
            user='root',
            database='dulieu'
        )
    
    def link_db(self):
        try:
            self.con = mysql.connector.connect(
                host=self._host,
                port=self._port,
                database=self._database,
                user=self._user,
            )
            if self.con.is_connected():
                print("Connect successfully!.")
            self.cursor = self.con.cursor(dictionary=True, buffered=True)
        except mysql.connector.Error as err:
            print(f"Error connecting: {err}")
            return None
    #############################################################################
    ## LOGIN ##
    #############################################################################
    def check_username(self, username):
        try:
            self.link_db()
            # TIM TAI KHOAN 
            sql = f"""
                SELECT *
                FROM ACCOUNT
                WHERE USERNAME = '{username}'
            """
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            print(result)
            return result
        except Exception as e:
            print("Error occurred while checking username:", e)
            return None
        finally:
            if self.con:
                self.con.close()
    #############################################################################
    ## SV ##
    #############################################################################
    def add_info_sv(self, masv, hoten, ngsinh, gtinh, diachi, sdt, lop):
        self.link_db()
        ## THEM
        sql = f"""
            INSERT INTO SINHVIEN (MASV, HOTEN, NGSINH, DCHI ,GTINH, SDT, LOP)
            VALUES ('{masv}', '{hoten}', '{ngsinh}', '{gtinh}', {diachi}, {sdt}, {lop});
        """

        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:
            self.con.rollback()
            return E
        finally:
            self.con.close()
    #############################################################################
    def update_info_sv(self, masv, hoten, ngsinh, gtinh, diachi, sdt, lop):
        self.link_db()
        ## CAP NHAT 
        sql = f"""
            UPDATE SINHVIEN
            SET HOTEN='{hoten}', NGSINH='{ngsinh}', GTINH='{gtinh}', DCHI='{diachi}', SDT={sdt}, LOP='{lop}'
            WHERE MASV='{masv}'
        """

        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:
            self.con.rollback()
            return E
        finally:
            self.con.close()
    #############################################################################
    def delete_info_sv(self, masv):
        self.link_db()
        
        sql = f"""
            DELETE FROM SINHVIEN
            WHERE MASV='{masv}';
        """

        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:
            self.con.rollback()
            return E
        
        finally:
            self.con.close()
    #############################################################################
    def search_info_sv(self, masvtk=None, hotentk=None, ngsinhtk=None, gtinhtk=None, dchitk=None, sdttk=None, loptk=None):
        self.link_db()
        # TIM KIEM DU LIEU TRONG DATABASE
        condition = ""
        if masvtk:
            condition += f"MASV LIKE '%{masvtk}%'"
        else:
            if hotentk:
                if condition:
                    condition += f" AND HOTEN LIKE '%{hotentk}%'"
                else:
                    condition += f"HOTEN LIKE '%{hotentk}%'"
            if ngsinhtk:
                if condition:
                    condition += f" AND NGSINH LIKE '%{ngsinhtk}%'"
                else:
                    condition += f"NGSINH LIKE '%{ngsinhtk}%'"
            if gtinhtk:
                if condition:
                    condition += f" AND GTINH LIKE '%{gtinhtk}%'"
                else:
                    condition += f"GTINH LIKE '%{gtinhtk}%'"
            if dchitk:
                if condition:
                    condition += f" AND DCHI LIKE '%{dchitk}%'"
                else:
                    condition += f"DCHI LIKE '%{dchitk}%'"
            if sdttk:
                if condition:
                    condition += f" AND SDT LIKE '%{sdttk}%'"
                else:
                    condition += f"SDT LIKE '%{sdttk}%'"
            if loptk:
                if condition:
                    condition += f" AND LOP LIKE '%{loptk}%'"
                else:
                    condition += f"LOP LIKE '%{loptk}%'"
        if condition:
            sql = f"""
                SELECT * 
                FROM SINHVIEN WHERE {condition};
            """
        else:
            sql = f"""
                SELECT *
                FROM SINHVIEN;
            """

        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
            
        except Exception as E:
            return E
            
        finally:
            self.con.close()
    #############################################################################  
    ## LOP ##
    #############################################################################
    def add_info_lop(self, malop, tenlop, khoa, khoahoc, hedaotao):
        self.link_db()
        
        sql = f"""
            INSERT INTO LOP (MALOP, TENLOP, KHOA, KHOAHOC, HEDAOTAO)
            VALUES ('{malop}', '{tenlop}', '{khoa}', '{khoahoc}', '{hedaotao}');
        """

        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:
            self.con.rollback()
            return E
        finally:
            self.con.close()
    ##############################################################################
    def update_info_lop(self, malop, tenlop, khoa, khoahoc, hedaotao):
        self.link_db()
        
        # Cap nhat database
        sql = f"""
            UPDATE LOP
            SET MALOP={malop}, TENLOP={tenlop}, KHOA={khoa}, KHOAHOC={khoahoc}, HEDAOTAO={hedaotao}
            WHERE MASV={malop}
        """

        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:
            self.con.rollback()
            return E
        finally:
            self.con.close()
    #############################################################################      
    def delete_info_lop(self, malop):
        self.link_db()
        
        sql = f"""
            DELETE FROM LOP 
            WHERE MALOP='{malop}';
        """

        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:
            self.con.rollback()
            return E
        
        finally:
            self.con.close()
    ############################################################################# 
    def search_info_lop(self, maloptk=None, tenloptk=None, khoatk=None, khoahoctk=None, hedaotaotk=None):
        self.link_db()

        condition = ""
        if maloptk:
            condition += f"MALOP LIKE '%{maloptk}%'"
        else:
            if tenloptk:
                if condition:
                    condition += f" AND TENLOP LIKE '%{tenloptk}%'"
                else:
                    condition += f"TENLOP LIKE '%{tenloptk}%'"
            if khoatk:
                if condition:
                    condition += f" AND KHOA LIKE '%{khoatk}%'"
                else:
                    condition += f"KHOA LIKE '%{khoatk}%'"
            if khoahoctk:
                if condition:
                    condition += f" AND KHOAHOC LIKE '%{khoahoctk}%'"
                else:
                    condition += f"KHOAHOC LIKE '%{khoahoctk}%'"
            if hedaotaotk:
                if condition:
                    condition += f"AND HEDAOTAO LIKE '%{hedaotaotk}%'"
                else:
                    condition += f"HEDAOTAO LIKE '%{hedaotaotk}%'"

        if condition:
            sql = f"""
                SELECT * 
                FROM LOP WHERE {condition};
            """
        else:
            sql = f"""
                SELECT *
                FROM LOP;
            """

        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        
        except Exception as E:
            return E
        
        finally:
            self.con.close()
    #############################################################################
    ## GV ##
    #############################################################################
    def add_info_gv(self, magv, hoten, ngsinh, gtinh, khoa):
        self.link_db()
        
        sql = f"""
            INSERT INTO GIANGVIEN (MAGV, HOTEN, NGSINH, GTINH, KHOA)
            VALUES ('{magv}', '{hoten}', '{ngsinh}', '{gtinh}', '{khoa}');
        """

        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:
            self.con.rollback()
            return E
        finally:
            self.con.close()
    ##############################################################################
    def update_info_gv(self, magv, hoten, ngsinh, gtinh, khoa):
        self.link_db()
        
        # Cap nhat database
        sql = f"""
            UPDATE GIANGVIEN
            SET HOTEN='{hoten}', NGSINH='{ngsinh}', GTINH='{gtinh}', KHOA='{khoa}'
            WHERE MAGV='{magv}'
        """

        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:
            self.con.rollback()
            return E
        finally:
            self.con.close()
    #############################################################################      
    def delete_info_gv(self, magv):
        self.link_db()
        
        sql = f"""
            DELETE FROM GIANGVIEN 
            WHERE MAGV='{magv}';
        """

        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:
            self.con.rollback()
            return E
        
        finally:
            self.con.close()
    ############################################################################# 
    def search_info_gv(self, magvtk=None, hotentk=None, ngsinhtk=None, gtinhtk=None, khoatk=None):
        self.link_db()

        condition = ""
        if magvtk:
            condition += f"MAGV LIKE '%{magvtk}%'"
        else:
            if hotentk:
                if condition:
                    condition += f" AND HOTEN LIKE '%{hotentk}%'"
                else:
                    condition += f"HOTEN LIKE '%{hotentk}%'"
            if ngsinhtk:
                if condition:
                    condition += f" AND NGSINH LIKE '%{ngsinhtk}%'"
                else:
                    condition += f"NGSINH LIKE '%{ngsinhtk}%'"
            if gtinhtk:
                if condition:
                    condition += f" AND GTINH = '{gtinhtk}'"
                else:
                    condition += f"GTINH = '{gtinhtk}'"
            if khoatk:
                if condition:
                    condition += f" AND KHOA LIKE '%{khoatk}%'"
                else:
                    condition += f"KHOA LIKE '%{khoatk}%'"

        if condition:
            sql = f"""
                SELECT * 
                FROM GIANGVIEN WHERE {condition};
            """
        else:
            sql = f"""
                SELECT *
                FROM GIANGVIEN;
            """

        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
            
        except Exception as E:
            return E
            
        finally:
            self.con.close()
    #############################################################################
    ## LOP ##
    #############################################################################
    def add_info_lop(self, malop, tenlop, khoa, khoahoc, hedaotao):
        self.link_db()
        
        sql = f"""
            INSERT INTO LOP (MALOP, TENLOP, KHOA, KHOAHOC, HEDAOTAO)
            VALUES ('{malop}', '{tenlop}', '{khoa}', '{khoahoc}', '{hedaotao}');
        """

        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:
            self.con.rollback()
            return E
        finally:
            self.con.close()
    #############################################################################
    def update_info_lop(self, malop, tenlop, khoa, khoahoc, hedaotao):
        self.link_db()
        
        # Update the database
        sql = f"""
            UPDATE LOP
            SET TENLOP='{tenlop}', KHOA='{khoa}', KHOAHOC='{khoahoc}', HEDAOTAO='{hedaotao}'
            WHERE MALOP='{malop}'
        """

        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:
            self.con.rollback()
            return E
        finally:
            self.con.close()
    #############################################################################      
    def delete_info_lop(self, malop):
        self.link_db()
        
        sql = f"""
            DELETE FROM LOP 
            WHERE MALOP='{malop}';
        """

        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:
            self.con.rollback()
            return E
        
        finally:
            self.con.close()
    ##############################################################################
    def search_info_lop(self, maloptk=None, tenloptk=None, khoatk=None, khoahoctk=None, hedaotaotk=None):
        self.link_db()

        condition = ""
        if maloptk:
            condition += f"MALOP LIKE '%{maloptk}%'"
        else:
            if tenloptk:
                if condition:
                    condition += f" AND TENLOP LIKE '%{tenloptk}%'"
                else:
                    condition += f"TENLOP LIKE '%{tenloptk}%'"
            if khoatk:
                if condition:
                    condition += f" AND KHOA LIKE '%{khoatk}%'"
                else:
                    condition += f"KHOA LIKE '%{khoatk}%'"
            if khoahoctk:
                if condition:
                    condition += f" AND KHOAHOC LIKE '%{khoahoctk}%'"
                else:
                    condition += f"KHOAHOC LIKE '%{khoahoctk}%'"
            if hedaotaotk:
                if condition:
                    condition += f" AND HEDAOTAO LIKE '%{hedaotaotk}%'"
                else:
                    condition += f"HEDAOTAO LIKE '%{hedaotaotk}%'"

        if condition:
            sql = f"""
                SELECT * 
                FROM LOP WHERE {condition};
            """
        else:
            sql = f"""
                SELECT *
                FROM LOP;
            """

        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
            
        except Exception as E:
            return E
            
        finally:
            self.con.close()
    #############################################################################
    ## KHOA ##
    #############################################################################
    def add_info_khoa(self, makhoa, tenkhoa, sdt, phong, trgkhoa):
        self.link_db()
        
        sql = f"""
            INSERT INTO KHOA (MAKHOA, TENKHOA, SDT, PHONG, TRGKHOA)
            VALUES ('{makhoa}', '{tenkhoa}', '{sdt}', '{phong}', '{trgkhoa}');
        """

        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:
            self.con.rollback()
            return E
        finally:
            self.con.close()
    #############################################################################
    def update_info_khoa(self, makhoa, tenkhoa, sdt, phong, trgkhoa):
        self.link_db()
        
        # Update the database
        sql = f"""
            UPDATE KHOA
            SET TENKHOA='{tenkhoa}', SDT='{sdt}', PHONG='{phong}', TRGKHOA='{trgkhoa}'
            WHERE MAKHOA='{makhoa}'
        """

        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:
            self.con.rollback()
            return E
        finally:
            self.con.close()

    #############################################################################      
    def delete_info_khoa(self, makhoa):
        self.link_db()
        
        sql = f"""
            DELETE FROM KHOA 
            WHERE MAKHOA='{makhoa}';
        """

        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:
            self.con.rollback()
            return E
        
        finally:
            self.con.close()

    ##############################################################################
    def search_info_khoa(self, makhoatk=None, tenkhoatk=None, sdttk=None, phongtk=None, trgkhoatk=None):
        self.link_db()

        condition = ""
        if makhoatk:
            condition += f"MAKHOA LIKE '%{makhoatk}%'"
        else:
            if tenkhoatk:
                if condition:
                    condition += f" AND TENKHOA LIKE '%{tenkhoatk}%'"
                else:
                    condition += f"TENKHOA LIKE '%{tenkhoatk}%'"
            if sdttk:
                if condition:
                    condition += f" AND SDT LIKE '%{sdttk}%'"
                else:
                    condition += f"SDT LIKE '%{sdttk}%'"
            if phongtk:
                if condition:
                    condition += f" AND PHONG LIKE '%{phongtk}%'"
                else:
                    condition += f"PHONG LIKE '%{phongtk}%'"
            if trgkhoatk:
                if condition:
                    condition += f" AND TRGPHONG LIKE '%{trgkhoatk}%'"
                else:
                    condition += f"TRGPHONG LIKE '%{trgkhoatk}%'"

        if condition:
            sql = f"""
                SELECT * 
                FROM KHOA WHERE {condition};
            """
        else:
            sql = f"""
                SELECT *
                FROM KHOA;
            """

        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
            
        except Exception as E:
            return E
            
        finally:
            self.con.close()
    #############################################################################
    ## MON ##
    #############################################################################
    def add_info_mh(self, mamh, tenmh, sotc):
        self.link_db()
        
        sql = f"""
            INSERT INTO MONHOC (MAMH, TENMH, SOTC)
            VALUES ('{mamh}', '{tenmh}', '{sotc}');
        """

        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:
            self.con.rollback()
            return E
        finally:
            self.con.close()
    #############################################################################
    def update_info_mh(self, mamh, tenmh, sotc):
        self.link_db()
        
        # Update the database
        sql = f"""
            UPDATE MONHOC
            SET TENMH='{tenmh}', SOTC='{sotc}'
            WHERE MAMH='{mamh}'
        """

        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:
            self.con.rollback()
            return E
        finally:
            self.con.close()
    #############################################################################      
    def delete_info_mh(self, mamh):
        self.link_db()
        
        sql = f"""
            DELETE FROM MONHOC 
            WHERE MAMH='{mamh}';
        """

        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:
            self.con.rollback()
            return E
        
        finally:
            self.con.close()
    ##############################################################################
    def search_info_mh(self, mamhtk=None, tenmhtk=None, sotctk=None):
        self.link_db()

        condition = ""
        if mamhtk:
            condition += f"MAMH LIKE '%{mamhtk}%'"
        if tenmhtk:
            if condition:
                condition += f" AND TENMH LIKE '%{tenmhtk}%'"
            else:
                condition += f"TENMH LIKE '%{tenmhtk}%'"
        if sotctk:
            if condition:
                condition += f" AND SOTC LIKE '%{sotctk}%'"
            else:
                condition += f"SOTC LIKE '%{sotctk}%'"

        if condition:
            sql = f"""
                SELECT * 
                FROM MONHOC WHERE {condition};
            """
        else:
            sql = f"""
                SELECT *
                FROM MONHOC;
            """

        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
            
        except Exception as E:
            return E
            
        finally:
            self.con.close()
    ##############################################################################
    ## NHAP DIEM ##
    ##############################################################################
    def search_info_nhapdiem(self, mamhtk=None, manhomtk=None, masvtk=None, hockytk=None, namhoctk=None):
        self.link_db()
        # LENH TRUY VAN
        condition = ""
        if mamhtk:
            condition += f"MH.MAMH LIKE '%{mamhtk}%'"
        if manhomtk:
            if condition:
                condition += f" AND NMH.MANHOM LIKE '%{manhomtk}%'"
            else:
                condition += f"NMH.MANHOM LIKE '%{manhomtk}%'"
        if masvtk:
            if condition:
                condition += f" AND SV.MASV LIKE '%{masvtk}%'"
            else:
                condition += f"SV.MASV LIKE '%{masvtk}%'"
        if namhoctk:
            if condition:
                condition += f" AND BD.NAMHOC LIKE '%{namhoctk}%'"
            else:
                condition += f"BD.NAMHOC LIKE '%{namhoctk}%'"
        if hockytk:
            if condition:
                condition += f" AND BD.HOCKY LIKE '%{hockytk}%'"
            else:
                condition += f"BD.HOCKY LIKE '%{hockytk}%'"
        if condition:
            sql = f"""
                SELECT DISTINCT GV.MAGV, GV.HOTEN , MH.MAMH, NMH.MANHOM, SV.MASV, SV.HOTEN , CTBD.DIEM_QT, CTBD.HESO_QT, CTBD.DIEMTHI, CTBD.HESO_THI, CTBD.DIEMTB_HE10, BD.HOCKY, BD.NAMHOC
                FROM GIANGVIEN GV
                JOIN KHOA K ON GV.KHOA = K.MAKHOA
                JOIN LOP L ON L.KHOA = K.MAKHOA
                JOIN NHOMMONHOC NMH ON NMH.GV = GV.MAGV
                JOIN CHITIETBANGDIEM CTBD ON CTBD.MANHOM = NMH.MANHOM
                JOIN BANGDIEM BD ON CTBD.BD = BD.MABD
                JOIN DANGKYNHOM DKN ON DKN.NHOM = NMH.MANHOM
                JOIN SINHVIEN SV ON DKN.SV = SV.MASV AND BD.MASV = SV.MASV
                JOIN MONHOC MH ON NMH.MH = MH.MAMH
                WHERE {condition};
            """ 
        else:
            sql = f"""
                SELECT DISTINCT GV.MAGV, GV.HOTEN , MH.MAMH, NMH.MANHOM, SV.MASV, SV.HOTEN , CTBD.DIEM_QT, CTBD.HESO_QT, CTBD.DIEMTHI, CTBD.HESO_THI, CTBD.DIEMTB_HE10 ,BD.HOCKY, BD.NAMHOC
                FROM GIANGVIEN GV
                JOIN KHOA K ON GV.KHOA = K.MAKHOA
                JOIN LOP L ON L.KHOA = K.MAKHOA
                JOIN NHOMMONHOC NMH ON NMH.GV = GV.MAGV
                JOIN CHITIETBANGDIEM CTBD ON CTBD.MANHOM = NMH.MANHOM
                JOIN BANGDIEM BD ON CTBD.BD = BD.MABD
                JOIN DANGKYNHOM DKN ON DKN.NHOM = NMH.MANHOM
                JOIN SINHVIEN SV ON DKN.SV = SV.MASV AND BD.MASV = SV.MASV
                JOIN MONHOC MH ON NMH.MH = MH.MAMH
            """

        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            print(result)
            return result
            
        except Exception as E:
            return E
            
        finally:
            self.con.close()            
    ##############################################################################
    def update_info_nhapdiem(self, mamh, manhom, masv, diem_qt, heso_qt, diemthi, heso_thi):
            self.link_db()
            sql = f"""
                UPDATE CHITIETBANGDIEM CTBD
                JOIN BANGDIEM BD ON CTBD.BD = BD.MABD
                JOIN SINHVIEN SV ON SV.MASV = BD.MASV
                JOIN NHOMMONHOC NMH ON NMH.MANHOM = CTBD.MANHOM
                JOIN MONHOC MH ON NMH.MH = MH.MAMH
                JOIN GIANGVIEN GV ON GV.MAGV = NMH.GV
                JOIN KHOA K ON GV.KHOA = K.MAKHOA
                JOIN LOP L ON L.KHOA = K.MAKHOA
                JOIN DANGKYNHOM DKN ON DKN.NHOM = NMH.MANHOM
                SET 
                    CTBD.DIEM_QT = '{diem_qt}',
                    CTBD.HESO_QT = '{heso_qt}', 
                    CTBD.DIEMTHI = '{diemthi}',
                    CTBD.HESO_THI = '{heso_thi}',
                    CTBD.DIEMTB_HE10 = ('{diem_qt}' * '{heso_qt}') + ('{diemthi}' * '{heso_thi}')
                WHERE 
                    MH.MAMH = '{mamh}'
                    AND CTBD.MANHOM = '{manhom}'
                    AND SV.MASV = '{masv}';
            """
            
            try:
                self.cursor.execute(sql)
                self.con.commit()
            except Exception as E:
                self.con.rollback()
                return str(E)
            finally:
                self.con.close()
    ##############################################################################
    ## TTSV ##
    ##############################################################################
    def info_acc_sv(self, masv):
        if not self.link_db():
            return None

        sql_sv = f"""
                  SELECT sinhvien.MASV, sinhvien.HOTEN, sinhvien.NGSINH, sinhvien.GTINH, sinhvien.SDT, sinhvien.DCHI, sinhvien.LOP, khoa.TENKHOA
                  from sinhvien, lop, khoa
                  where sinhvien.LOP = lop.MALOP and lop.KHOA = khoa.MAKHOA and MASV = '{masv}' ;
              """
        try:
            # self.cursor = self.con.cursor()
            self.cursor.execute(sql_sv)
            result_sv = self.cursor.fetchall()
            if result_sv:
                print("Lấy thông tin giang vien thành công!")
                return result_sv  # Return the fetched data

            print("Không tìm thấy thông tin sinh viên.")
            return None

        except mysql.connector.Error as e:
            print("MySQL Error:", e)
            return None
        finally:
            if self.con:
                self.con.close()
    ##############################################################################
    def ketqua(self, masv):
        if not self.link_db():
            return None
        sql_diem_sv = f"""
                        SELECT CTBD.DIEMTB_HE10 
                        FROM BANGDIEM BD, CHITIETBANGDIEM CTBD 
                        where BD.MASV = '{masv}' AND BD.MABD = CTBD.BD;
                     """
        try:
            self.cursor = self.con.cursor()
            self.cursor.execute(sql_diem_sv)
            result = self.cursor.fetchall()
            if result:
                print(result)
                print("Lấy thông tin tất cả môn học thành công!")
                return result  # Return the fetched data

            print("Không tìm thấy thông tin môn học sinh .")
            return None
        except mysql.connector.Error as e:
            print("MySQL Error:", e)
            return None

        finally:
            if self.con:
               self.con.close()



