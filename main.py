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
        self.show()

        list = openpyxl.load_workbook('wordfile.xlsx')
        name = list.get_sheet_names()
        for i in name:
            Main.wordList.addItem(i)
        
        Main.wordList.itemDoubleClicked.connect(self.Word)
        Main.deleteButton.clicked.connect(self.delete)

    def delete (self):
        list = openpyxl.load_workbook('wordfile.xlsx')
        name = list.sheetnames()
        chap = Main.wordList.currentRow()
        print(name[chap])
        #list.remove_sheet(list[name[chap]])
        self.Main

    #def wordplace (self,name):
        #chap = Main.wordList.currentRow()
        #self.Word(chap)
    a=0
    def Word (self):
        global Word

        Word = QtUiTools.QUiLoader().load(resource_path("wrp_word.ui"))
        self.setCentralWidget(Word)
        self.setWindowTitle("Word")
        self.setWindowIcon(QtGui.QPixmap(resource_path("./images/word.png")))
        self.resize(270,500)
        self.show()

        list = openpyxl.load_workbook('wordfile.xlsx')
        name = list.get_sheet_names()
        chap = Main.wordList.currentRow()

        if chap>=0:
              
            Word.chaptername.setText(name[chap])
            sheet = list.get_sheet_by_name(name[chap])            

            count =0
            for row in sheet:
                    count +=1
            print(count)
            
            i=1     
            while i<count :
                Word.word.setText(sheet.cell(row=i,column=1).value)
                Word.means.setText(sheet.cell(row=i,column=2).value)
                Word.nextButton.clicked.connect(add)
                if (a==1):
                    i+=1
                    a=0
                else:
                    break

        def add (self):
            global a
            a=1        

        Word.endButton.clicked.connect(self.Main)
    
    def add (self):
        self.a=1
    
    '''def update (self,sheet):
        self.i +=1
        Word.word.setText(sheet.cell(row=self.i,column=1).value)
        Word.means.setText(sheet.cell(row=self.i,column=2).value)'''
        

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
