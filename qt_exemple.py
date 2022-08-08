#!/usr/bin/python3
from curses import window
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QWidget, 
                               QVBoxLayout, QMainWindow)
from PySide6.QtGui import QFont, QAction
from PySide6.QtCore import Qt

app = QApplication()    #set/beggin a apllication
#Funciona para multiplas janelas, dessa forma uma 
#janela só pode ter um único widgets 
window = QMainWindow()
base = QWidget()       
layout = QVBoxLayout()
font = QFont()
font.setPixelSize(20)   #set font size 

button = QPushButton('Test_Button')
button.setFont(font)
#button.show()

label = QLabel('Hello world')   #set a widgets 
label.setFont(font)
label.setAlignment(Qt.AlignCenter)
#label.show() para não mostrar mais

layout.addWidget(label)
layout.addWidget(button)

menu = window.menuBar()
file_menu = menu.addMenu('File') #create a menu
action = QAction('Test_Action')  #create a action for menu 
file_menu.addAction(action)

base.setLayout(layout)
window.setCentralWidget(base)
window.show()
#base.show()
app.exec()

##ctrl C + ctrl K comenta
##ctrl C + ctrl U descomenta