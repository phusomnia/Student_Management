from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem, QPushButton, QWidget, QApplication, QFileDialog
from FrontEnd.Data_Form import Data_Form
from BackEnd.ConnectDB import Connect_DB
import pandas as pd
import os

class Data_Menu(QWidget):
    def __init__(self):
        super(Data_Menu, self).__init__()

        self.DB = Connect_DB()

        self.DF = Data_Form()
        self.DF.setupData(self)

        self.listbox_acc = self.DF.tableWidget
        self.listbox_acc.setSortingEnabled(False)

        # Connect button click signal to export_to_excel method
        self.DF.InBtn.clicked.connect(self.export_to_excel)

        self.display_data()

    def display_data(self):
        result = self.DB.search_data_acc()

        if result:
            self.listbox_acc.setRowCount(0)
            self.listbox_acc.setRowCount(len(result))

            for row, info in enumerate(result):
                info_list = [
                    info['USERNAME'],
                    info['PASS']
                ]

                for column, item in enumerate(info_list):
                    cell_item = QTableWidgetItem(str(item))
                    self.listbox_acc.setItem(row, column, cell_item)

    def export_to_excel(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Excel Files (*.xlsx)")
        if filename:
            headers = ["Username", "Password"]
            data = []

            for row in range(self.listbox_acc.rowCount()):
                row_data = []
                for column in range(self.listbox_acc.columnCount()):
                    item = self.listbox_acc.item(row, column)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append("")  # Handle empty cells
                data.append(row_data)

            df = pd.DataFrame(data, columns=headers)

            # Export DataFrame to Excel
            excel_file_path = os.path.join(os.getcwd(), filename)
            df.to_excel(excel_file_path, index=False)
            QMessageBox.information(self, "Export Complete", f"Data exported to {excel_file_path}")
    
if __name__ == '__main__':
    import sys
    App = QApplication(sys.argv)
    Window_App = Data_Menu()
    Window_App.show()
    sys.exit(App.exec())
