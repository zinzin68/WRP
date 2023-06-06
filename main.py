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
        
        Main.wordList.itemDoubleClicked.connect(self.wordplace)
        

        #Main.addButton.clicked.connect(self.addsheet)


        self.show()

    '''def addsheet(self):
        text,ok = QInputDialog.getText(self, '단어장 추가','단어장 이름:')
        list = openpyxl.load_workbook('wordfile.xlsx')
        list.create_sheet(index=0,title=text)'''

    def wordplace (self,name):
        chap = Main.wordList.currentRow()
        print(chap)
        self.Word(chap)

    def next (self):
           a=1
           return a

    def Word (self, chapter):
        Word = QtUiTools.QUiLoader().load(resource_path("wrp_word.ui"))
        self.setCentralWidget(Word)
        self.setWindowTitle("Word")
        self.setWindowIcon(QtGui.QPixmap(resource_path("./images/word.png")))
        self.resize(270,500)
        self.show()

        if chapter>=0:
    
            Word.nextButton.clicked.connect(self.next)
            
            list = openpyxl.load_workbook('wordfile.xlsx')
            name = list.get_sheet_names()
            Word.chaptername.setText(name[chapter])
            sheet = list.get_sheet_by_name(name[chapter])
            count =0
            for row in sheet:
                    count +=1 #전체 단어 개수
            i=1
            while i<=count:
                    Word.word.setText(sheet.cell(row=i,column=1).value)
                    Word.means.setText(sheet.cell(row=i,column=2).value)
                    if (int(input())==1):
                            i+=1
                    else:
                            break
        
            
        

        #Word.nextButton.clicked.connect(self.wordshow)

    #def wordshow (self):
        #global sig = not sig
        

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
