from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from FrontEnd.Form_Menu import Menu
from Backend.Connection_Database import ConnectDB
from docx import Document

class Window_Menu(QWidget):
    def __init__(self):
        super(Window_Menu, self).__init__()

        self.UI = Menu()
        self.UI.setupMenu(self)
        #############################################################################
        ## INIT BAOCAO
        self.report_textbox = self.UI.BaoCaoEntry
        self.search_textbox = self.UI.TimKiemEntry_BaoCao
        self.no_matches_label = self.UI.NMF_Label
        self.no_matches_label.hide()
        #############################################################################
        ## BAO CAO BTN
        self.print_btn_BC = self.UI.InBC_Btn
        self.search_keyboard_btn_BC = self.UI.TimKiemBtn_BaoCao
        self.clear_text_btn_BC = self.UI.XoaBtn_BaoCao
        self.exit_btn_BC = self.UI.ThoatBtn_BaoCao
        #############################################################################
        self.UI.BaoCaoBtn.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_BaoCao))
        self.print_btn_BC.clicked.connect(self.save_as_word)
        self.search_keyboard_btn_BC.clicked.connect(self.search_keyword)
        self.clear_text_btn_BC.clicked.connect(self.clear_all)
        self.exit_btn_BC.clicked.connect(lambda: self.toggleForm(self.UI.Frame_Admin, self.UI.Frame_Init))
    #############################################################################
    def toggleForm(self, Frame, Form):
        Frame.setCurrentIndex(Frame.indexOf(Form))
    #############################################################################
    def save_as_word(self):
        text = self.report_textbox.toPlainText()

        if not text:
            QMessageBox.warning(self, "Cảnh báo", "Nhập thông tin vào báo cáo!")
            return

        document = Document()
        document.add_paragraph(text)

        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Word Files (*.docx)")

        if filename:
            try:
                document.save(filename)
                QMessageBox.information(self, "Thông báo", "Lưu file thành công")
            except Exception as e:
                QMessageBox.critical(self, "Cảnh báo", f"Lỗi: {str(e)}")
    #############################################################################
    def search_keyword(self):
        search_text = self.search_textbox.text()
        print(search_text)
        if search_text:
            document = self.report_textbox.document()
            cursor = QTextCursor(document)

            format_ = QTextCharFormat()
            format_.setBackground(QColor("yellow"))

            cursor.movePosition(QTextCursor.MoveOperation.Start)
            cursor.select(QTextCursor.SelectionType.Document)
            cursor.setCharFormat(QTextCharFormat())

            search_words = search_text.split("\n")

            search_results = []

            for word in search_words:
                if word:
                    cursor = document.find(word)
                    while not cursor.isNull():
                        cursor.mergeCharFormat(format_)
                        search_results.append(cursor.selection().toPlainText())
                        cursor = document.find(word, cursor.position() + len(word))
            
            if search_results:
                self.no_matches_label.hide()
            else:
                cursor.movePosition(QTextCursor.MoveOperation.Start)
                cursor.select(QTextCursor.SelectionType.Document)
                cursor.setCharFormat(QTextCharFormat())
                self.no_matches_label.setText("No matches found.")
                self.no_matches_label.show()
        else:
            cursor = QTextCursor(self.report_textbox.document())
            cursor.movePosition(QTextCursor.MoveOperation.Start)
            cursor.select(QTextCursor.SelectionType.Document)
            self.no_matches_label.setText("No matches found.")
            self.no_matches_label.show()
    #############################################################################
    def clear_all(self):
        self.report_textbox.clear()
        self.search_textbox.clear()
        self.no_matches_label.hide()
    #############################################################################
if __name__ == '__main__':
    APP  = QApplication([])
    WINDOW = Window_Menu()
    WINDOW.show()
    APP.exec()


