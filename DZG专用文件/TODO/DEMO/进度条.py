# # import random
# # import sys
# # from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar,QMainWindow
# # from PyQt5.QtCore import QBasicTimer
# #
# #
# # class MyClass(QMainWindow):
# #     def __init__(self):
# #         super().__init__()
# #         self.initUI()
# #
# #     def initUI(self):
# #         self.resize(400, 200)
# #         # 载入进度条控件
# #         self.pgb = QProgressBar(self)
# #         self.pgb.move(50, 50)
# #         self.pgb.resize(300, 30)
# #
# #         # 配置一个值表示进度条的当前进度
# #         self.pv = 0
# #
# #         # 申明一个时钟控件
# #         self.timer1 = QBasicTimer()
# #
# #         # 设置进度条的范围
# #         self.pgb.setMinimum(0)
# #         self.pgb.setMaximum(100)
# #         self.pgb.setValue(self.pv)
# #         # 载入按钮
# #         self.btn = QPushButton("开始", self)
# #         self.btn.move(50, 100)
# #         self.btn.clicked.connect(self.myTimerState)
# #         self.show()
# #
# #     def myTimerState(self):
# #         if self.timer1.isActive():
# #             self.timer1.stop()
# #             self.btn.setText("开始")
# #         else:
# #             self.timer1.start(100, self)
# #             self.btn.setText("停止")
# #
# #     # def timerEvent(self, e):
# #     #     # 这个估计是 内置方法的重写
# #     #
# #     #     if self.pv == 100:
# #     #         self.timer1.stop()
# #     #         self.btn.setText("完成")
# #     #     else:
# #     #         self.pv += 1
# #     #         self.pgb.setValue(self.pv)
# #
# #     def timerEvent(self, e):
# #         # 这个估计是 内置方法的重写
# #         # 我们这里是一个曲线的形式 方法的重写
# #
# #         if self.pv == 100:
# #             self.timer1.stop()
# #             self.btn.setText("完成")
# #         elif self.pv<90:
# #             self.pv += random.randint(0,10)
# #             self.pgb.setValue(self.pv)
# #         else:
# #             self.pv += 1
# #             self.pgb.setValue(self.pv)
# #
# #
# #
# # if __name__ == "__main__":
# #     app = QApplication(sys.argv)
# #     mc = MyClass()
# #     app.exec_()
# from random import randint
# import sys
# from PyQt5.QtCore import QTimer
# from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QProgressBar
#
# StyleSheet = '''
# /*设置红色进度条*/
# #RedProgressBar {
#     text-align: center; /*进度值居中*/
# }
# #RedProgressBar::chunk {
#     background-color: #F44336;
# }
# #GreenProgressBar {
#     min-height: 12px;
#     max-height: 12px;
#     border-radius: 6px;
# }
# #GreenProgressBar::chunk {
#     border-radius: 6px;
#     background-color: #009688;
# }
# #BlueProgressBar {
#     border: 2px solid #2196F3;/*边框以及边框颜色*/
#     border-radius: 5px;
#     background-color: #E0E0E0;
# }
# #BlueProgressBar::chunk {
#     background-color: #2196F3;
#     width: 10px; /*区块宽度*/
#     margin: 0.5px;
# }
# '''
#
#
# class ProgressBar(QProgressBar):
#
#     def __init__(self, *args, **kwargs):
#         super(ProgressBar, self).__init__(*args, **kwargs)
#         self.setValue(0)
#         if self.minimum() != self.maximum():
#             self.timer = QTimer(self, timeout=self.onTimeout)
#             self.timer.start(randint(1, 3) * 1000)
#
#     def onTimeout(self):
#         if self.value() >= 100:
#             self.timer.stop()
#             self.timer.deleteLater()
#             del self.timer
#             return
#         self.setValue(self.value() + 1)
#
#
# class Window(QWidget):
#
#     def __init__(self, *args, **kwargs):
#         super(Window, self).__init__(*args, **kwargs)
#         self.resize(800, 600)
#         layout = QVBoxLayout(self)
#         layout.addWidget(  # 常规方形加载状态
#             ProgressBar(self, minimum=0, maximum=100, objectName="RedProgressBar"))
#
#         layout.addWidget(  # 常规方形繁忙状态
#             ProgressBar(self, minimum=0, maximum=0, objectName="RedProgressBar"))
#
#         layout.addWidget(  # 常规圆形加载状态
#             ProgressBar(self, minimum=0, maximum=100, textVisible=False,
#                         objectName="GreenProgressBar"))
#         layout.addWidget(  # 常规圆形繁忙状态
#             ProgressBar(self, minimum=0, maximum=0, textVisible=False,
#                         objectName="GreenProgressBar"))
#
#         layout.addWidget(  # 方形格子加载状态
#             ProgressBar(self, minimum=0, maximum=100, textVisible=False,
#                         objectName="BlueProgressBar"))
#         layout.addWidget(  # 方形格子繁忙状态
#             ProgressBar(self, minimum=0, maximum=0, textVisible=False,
#                         objectName="BlueProgressBar"))
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     app.setStyleSheet(StyleSheet)
#     w = Window()
#     w.show()
#     sys.exit(app.exec_())
#

import math
import time

sin = 0
sum  = 0
while 1:
    time.sleep(0.2)
    sin+=0.1
    sum+= int(100*math.sin(0.01* sin))
    print(sum)
