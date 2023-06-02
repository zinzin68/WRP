import sys
import os
from PySide6 import QtUiTools, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow

class MainView(QMainWindow):    
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        global UI_set

        UI_set = QtUiTools.QUiLoader().load(resource_path("WRP_Start.ui"))
        self.setCentralWidget(UI_set)
        self.setWindowTitle("UI TEST")
        self.setWindowIcon(QtGui.QPixmap(resource_path("./images/word.png")))
        self.setGeometry(100,50,300,200)
        self.show()
 

#파일 경로
#pyinstaller로 원파일로 압축할때 경로 필요함

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainView()
    #main.show()
    sys.exit(app.exec())


import openpyxl

wb = openpyxl.load_workbook("C:/Users/dnwls/WRP/engword.xlsx")
wb_sheet = wb.active

for row in wb_sheet:
    if row[0].value == None:
        break
    print(row[0].value, row[1].value, row[2].value)

wb.close()