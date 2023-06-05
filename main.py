import openpyxl
import sys
import os
from PySide6 import QtUiTools, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import *
from PySide6.QtCore import *

class MainView(QMainWindow):    
    def __init__(self):
        super().__init__()
        self.setupUI()

    

    def setupUI(self):
        global UI_set

        UI_set = QtUiTools.QUiLoader().load(resource_path("wrp_start.ui"))
        self.setCentralWidget(UI_set)
        self.setWindowTitle("UI TEST")
        self.setWindowIcon(QtGui.QPixmap(resource_path("./images/word.png")))
        self.resize(270,500)
        self.show()

        UI_set.start.clicked.connect(self.Main)

    def Main (self):
        global Main

        Main = QtUiTools.QUiLoader().load(resource_path("wrp_main.ui"))
        self.setCentralWidget(Main)
        self.setWindowTitle("List")
        self.setWindowIcon(QtGui.QPixmap(resource_path("./images/word.png")))
        self.resize(270,500)

        list = openpyxl.load_workbook('wordfile.xlsx')
        name = list.get_sheet_names()
        for i in name:
            Main.wordList.addItem(i)
        Main.wordList.itemClicked.connect(self.wordplace)
        self.show()

    def wordplace (self):
        chapter = Main.wordList.currentItem().text()
        list = openpyxl.load_workbook('wordfile.xlsx')
        sheet = list.get_sheet_by_name(chapter)
        print(sheet['A2'].value)


    def Word (self):
        Word = QtUiTools.QUiLoader().load(resource_path("wrp_word.ui"))
        self.setCentralWidget(Word)
        self.setWindowTitle("Word")
        self.setWindowIcon(QtGui.QPixmap(resource_path("./images/word.png")))
        self.resize(270,500)
        self.show()

    def check (self):
        Check = QtUiTools.QUiLoader().load(resource_path("wrp_check.ui"))
        self.setCentralWidget(Check)
        self.setWindowTitle("Check")
        self.setWindowIcon(QtGui.QPixmap(resource_path("./images/word.png")))
        self.resize(270,500)
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
    main.show()
    sys.exit(app.exec())
