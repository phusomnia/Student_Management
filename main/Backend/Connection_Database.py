import mysql.connector

class ConnectDB:
    def __init__(self):
        self._host = "localhost"
        self._port = 3306
        self._user = "root"
        self._password = "1337"
        self._database = "dulieu"
        self.con = None
        self.cursor = None
    
    # Ket noi den mysql
    def link_db(self):
        try:
            self.con = mysql.connector.connect(
                host=self._host,
                port=self._port,
                database=self._database,
                user=self._user,
            )
            self.cursor = self.con.cursor(dictionary=True)
        except mysql.connector.Error as err:
            print("Error:", err)
    #############################################################################
    ## SV ##
    #############################################################################
    def add_info_sv(self, masv, hoten, lop, diachi, ngsinh, gtinh, sdt):
        self.link_db()
        ## THEM
        sql = f"""
            INSERT INTO SINHVIEN (MASV, HOTEN, LOP, DCHI ,NGSINH, GTINH, SDT)
            VALUES ('{masv}', '{hoten}', '{lop}', {diachi}, '{ngsinh}', '{gtinh}', {sdt});
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
    def update_info_sv(self, masv, hoten, lop, diachi, ngsinh, gtinh, sdt):
        self.link_db()
        ## CAP NHAT 
        sql = f"""
            UPDATE SINHVIEN
            SET HOTEN='{hoten}', LOP='{lop}', NGSINH='{ngsinh}', DCHI='{diachi}', GTINH='{gtinh}', SDT={sdt}
            WHERE MASV={masv}
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
        ## XOA
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
    def search_info_sv(self, masvtk=None, hotentk=None, loptk=None, dchitk=None ,ngsinhtk=None, gtinhtk=None, sdttk=None):
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
            if loptk:
                if condition:
                    condition += f" AND LOP LIKE '%{loptk}%'"
                else:
                    condition += f"LOP LIKE '%{loptk}%'"
            if dchitk:
                if condition:
                    condition += f" AND LOP LIKE '%{dchitk}%'"
                else:
                    condition += f"LOP LIKE '%{dchitk}%'"
            if ngsinhtk:
                if condition:
                    condition += f"AND NGSINH LIKE '%{ngsinhtk}%'"
                else:
                    condition += f"NGSINH LIKE '%{ngsinhtk}%'"
            if gtinhtk:
                if condition:
                    condition += f"AND GTINH LIKE '%{gtinhtk}%'"
                else:
                    condition += f"GTINH LIKE '%{gtinhtk}%'"
            if sdttk:
                if condition:
                    condition += f" AND SDT LIKE '%{sdttk}%'"
                else:
                    condition += f"SDT LIKE '%{sdttk}%'"         
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
            WHERE MAGV={magv}
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
    def add_info_khoa(self, makhoa, tenkhoa, sdt, phong, trgphong):
        self.link_db()
        
        sql = f"""
            INSERT INTO KHOA (MAKHOA, TENKHOA, SDT, PHONG, TRGPHONG)
            VALUES ('{makhoa}', '{tenkhoa}', '{sdt}', '{phong}', '{trgphong}');
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
    def search_info_khoa(self, makhoa=None, tenkhoa=None, sdt=None, phong=None, trgkhoa=None):
        self.link_db()

        condition = ""
        if makhoa:
            condition += f"MAKHOA LIKE '%{makhoa}%'"
        else:
            if tenkhoa:
                if condition:
                    condition += f" AND TENKHOA LIKE '%{tenkhoa}%'"
                else:
                    condition += f"TENKHOA LIKE '%{tenkhoa}%'"
            if sdt:
                if condition:
                    condition += f" AND SDT LIKE '%{sdt}%'"
                else:
                    condition += f"SDT LIKE '%{sdt}%'"
            if phong:
                if condition:
                    condition += f" AND PHONG LIKE '%{phong}%'"
                else:
                    condition += f"PHONG LIKE '%{phong}%'"
            if trgkhoa:
                if condition:
                    condition += f" AND TRGPHONG LIKE '%{trgkhoa}%'"
                else:
                    condition += f"TRGPHONG LIKE '%{trgkhoa}%'"

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
    def search_info_nhapdiem(self):
        self.link_db()
        sql = f"""
                SELECT DISTINCT GV.MAGV, GV.HOTEN AS TEN_GIANGVIEN, SV.MASV, SV.HOTEN AS TEN_SINHVIEN, 
                    MH.MAMH, MH.TENMH, BD.HOCKY, BD.NAMHOC, CTBD.DIEM_QUATRINH, CTBD.HESO_QT, CTBD.DIEMTHI, CTBD.HESO_THI
                FROM SINHVIEN SV
                INNER JOIN BANGDIEM BD ON SV.MASV = BD.MASV
                INNER JOIN DANGKYNHOM DKNH ON SV.MASV = DKNH.MASV
                INNER JOIN CHITIETBANGDIEM CTBD ON BD.MABD = CTBD.MABD
                INNER JOIN NHOMMONHOC NH ON CTBD.MANHOM = NH.MANHOM
                INNER JOIN MONHOC MH ON NH.MH = MH.MAMH
                INNER JOIN GIANGVIEN GV ON NH.GV = GV.MAGV
            """
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
            
        except Exception as E:
            return E
            
        finally:
            self.con.close()

