import datetime
import math
import os
import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


# class Example(QMainWindow):
#     def __init__(self):
#         super(Example, self).__init__()
#         # 窗口居中
#         self.setWindowTitle("QT通用模板")
#         self.desktop = QDesktopWidget()
#         self.setGeometry(int(self.desktop.width() * 0.25), int(self.desktop.height() * 0.15),
#                          int(self.desktop.width() * 0.5), int(self.desktop.height() * 0.7))
#         self.show()
#         # self.setWindowIcon(QIcon("resources\strat.ico"))
#
#         self.but = QPushButton(self)
#         self.but.show()
#         self.but.move(100, 100)
#         self.but.setText("显示进度条")
#         self.but.clicked.connect(lambda: self.creat_sttatusbar("push buttom"))
#         # self.but.linkHovered.connect(lambda: self.creat_sttatusbar("push buttom"))
#
#         self.creat_sttatusbar("hellow")
#         # 打印当前时间
#         time1 = datetime.datetime.now()
#         # print(time1)
#         # 打印按指定格式排版的时间
#         time2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         # print(time2)
#
#         # 显示窗口
#         # self.creat_menu()
#         # self.show()
#         # self.creat_questionbox()
time1 = datetime.datetime.now()
#         # print(time1)
time2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         # print(time2)
class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("标题")
        self.destop = QDesktopWidget()

        self.resize(int(0.5*self.destop.width()),int(0.7*self.destop.height()))


        self.add_Lable()
        self.add_push_button()

    def add_Lable(self):
        self.Label = QLabel(self)
        self.Label.setText("标签的内容")
        self.Label.move(100,220)

    def add_push_button(self):
        self.push_button = QPushButton(self)
        self.push_button.setText("按钮")
        self.push_button.move(220,400)
        self.push_button.clicked.connect(lambda :print(time2))
        self.push_button.show()

        self.show()




qpp = QApplication(sys.argv)
win  = Window()
app.exec()
