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

    def add_info(self, masv, hoten, lop, ngsinh, gtinh, sdt):
        self.link_db()
        
        sql = f"""
            INSERT INTO SINHVIEN (MASV, HOTEN, LOP, NGSINH, GTINH, SDT)
            VALUES ({masv}, '{hoten}', '{lop}', '{ngsinh}', '{gtinh}', {sdt});
        """

        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:
            self.con.rollback()
            return E
        finally:
            self.con.close()

    def update_info(self, masv, hoten, lop, ngsinh, gtinh, sdt):
        self.link_db()
        
        # Cap nhat database
        sql = f"""
            UPDATE SINHVIEN
            SET HOTEN='{hoten}', LOP='{lop}', NGSINH='{ngsinh}', GTINH='{gtinh}', SDT={sdt}
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

    def delete_info(self, masv):
        self.link_db()
        
        sql = f"""
            DELETE FROM SINHVIEN 
            WHERE MASV={masv};
        """

        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:
            self.con.rollback()
            return E
        
        finally:
            self.con.close()

    def search_info(self, masvtk=None, hotentk=None, loptk=None, ngsinhtk=None, gtinhtk=None, sdttk=None):
        self.link_db()

        # Tim kiem du lieu trong database
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

        # Lenh truy van tim kiem thong tin
        # Neu khong co dieu kien se lay tat ca thong tin
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