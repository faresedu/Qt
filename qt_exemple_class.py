#!/usr/bin/python3
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QWidget, 
                               QVBoxLayout, QMainWindow)
from PySide6.QtGui import QFont, QAction
from PySide6.QtCore import Qt


def callback():
    print('Click button test')

def callback2():
    print('Second click button test')

class Window(QMainWindow):
    def __init__(self):
        self.click = 0
        super().__init__()
        base = QWidget()       
        layout = QVBoxLayout()
        font = QFont()
        font.setPixelSize(20)   #set font size 

        button = QPushButton('Test_Button')
        button.clicked.connect(callback) #apply the callback
        button.setFont(font)
        button.clicked.connect(self.change_label)
        #button.show()

        self.label = QLabel('Hello world')   #set a widgets 
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        #label.show() para não mostrar mais

        layout.addWidget(self.label)
        layout.addWidget(button)

        menu = self.menuBar()
        file_menu = menu.addMenu('File') #create a menu
        action = QAction('Test_Action')  #create a action for menu
        #action.triggered.connect(callback2) 
        file_menu.addAction(action)

        base.setLayout(layout)
        self.setCentralWidget(base)

    def change_label(self): 
        if(self.click == 0):
            self.label.setText('Clicked!!!!')
            self.click = 1
        else:
            self.label.setText('Hello world')
            self.click = 0 

#base.show()


app = QApplication()    #set/beggin a apllication
                        #Funciona para multiplas janelas, dessa forma uma 
                        #janela só pode ter um único widgets
window = Window()
window.show()
app.exec()

'''
callbacks são funções que se comunicam com os widgets

'''