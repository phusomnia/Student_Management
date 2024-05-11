import mysql.connector
from PyQt6.QtWidgets import QMessageBox

class Connect_DB:
    def __init__(self) -> None:
        self.host = "127.0.0.1"
        self.port = 3306
        self.user = "root"
        self.db = "test"
        self.con = None
        self.cursor = None

    def Link_db(self):
        try:
            self.con = mysql.connector.connect(
                host=self.host,
                port=self.port,
                database=self.db,
                user=self.user,
            )
            if self.con.is_connected():
                print("Kết nối database thành công!.\n")
            else:
                print("Kết nối thất bại.")
            self.cursor = self.con.cursor(dictionary=True, buffered=True)
        except mysql.connector.Error as E:
            return E
    #############################################################################
    def search_data_acc(self):
        self.Link_db()

        sql_search_info_acc = f"""
            SELECT *
            FROM ACC;
        """

        try:
            self.cursor.execute(sql_search_info_acc)
            result = self.cursor.fetchall()
            if result:
                print("Tìm thông tin thành công!\n")
                for info in result:
                    print(info)
                return result
            else:
                print("Không tìm thông tin thành công!\n")
        except mysql.connector.Error as E:
            return E
