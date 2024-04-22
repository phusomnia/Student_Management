import mysql.connector


class ConnectDB:
    def __init__(self):
        self._host = "localhost"
        self._port = 3306
        self._user = "root1"
        self._database = "222010001"
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
            if self.con.is_connected():
                print("Kết nối đến cơ sở dữ liệu MySQL thành công.")
                return True
        except mysql.connector.Error as e:
            print(f"Lỗi khi kết nối đến cơ sở dữ liệu MySQL: {e}")
            return False

    def search_acc(self, username, password):
        if not self.link_db():
            return None

        sql_sv = """
            SELECT * FROM account_sv WHERE USERNAME= %s and PASS= %s;
        """
        sql_gv = """
            SELECT * FROM account_gv WHERE USERNAME= %s and PASS= %s;
        """
        try:
            self.cursor = self.con.cursor()
            self.cursor.execute(sql_sv, (username, password))
            result_sv = self.cursor.fetchall()
            if result_sv:
                print("Tài khoản là sinh viên.")
                return result_sv

            self.cursor.execute(sql_gv, (username, password))
            result_gv = self.cursor.fetchall()
            if result_gv:
                print("Tài khoản là giáo viên.")
                return result_gv

            print("Tài khoản không tồn tại hoặc sai mật khẩu.")
            return None

        except mysql.connector.Error as e:
            print("MySQL Error:", e)
            return None
        finally:
            if self.con:
                self.con.close()


if __name__ == '__main__':
    con = ConnectDB()
    result = con.search_acc("GV01001", "123456")
    print(result)
