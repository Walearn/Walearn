import math
import os
import sys
import random
from PyQt5.QtWidgets import *
from qt_material import apply_stylesheet
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        # 窗口居中
        self.setWindowTitle("QT通用模板")
        self.desktop = QDesktopWidget()
        self.setGeometry(int(self.desktop.width() * 0.25), int(self.desktop.height() * 0.15),
                         int(self.desktop.width() * 0.5), int(self.desktop.height() * 0.7))
        self.setWindowIcon(QIcon("resources\strat.ico"))

        # 创建基本信息
        self.message = QMessageBox(self)

        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)
        # todo 添加其他的信息

        # 按钮方便我们测试进度条和状态栏
        self.but = QPushButton(self)
        self.but.show()
        self.but.move(100, 100)
        self.but.setText("显示进度条")
        self.but.clicked.connect(self.creat_progressbar)

        self.but = QPushButton(self)
        self.but.show()
        self.but.move(100, 200)
        self.but.setText("显示进度条")

        self.but.clicked.connect(lambda: self.creat_sttatusbar("push buttom"))
        # self.but.linkHovered.connect(lambda: self.creat_sttatusbar("push buttom"))

        self.creat_sttatusbar("hellow")

        # 显示窗口
        self.creat_menu()
        self.show()
        self.creat_questionbox()



    # 我们新添加的方法放到这里 默认方法 放到后面

    def creat_messagebox(self, _title, _text):
        '''创建一个提示消息'''
        self.message.setText(_text)
        self.message.setWindowTitle(_title)
        self.message.show()

    def creat_questionbox(self):
        # todo 重写不同的指令
        """创建一个提问消息
        需要重写
        """
        reply = QMessageBox.question(self, 'title',
                                     "Are you sure to quit? info ", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            print("选择了yes")
            pass
        else:
            print("选择了NO")
            pass

    def creat_progressbar(self):
        class ProGressBar(QDialog):
            """
            内置类 实现我们的进度条 这里需要我们自己去修改显示的内容
            """

            # todo 修改标题 和标签
            def __init__(self, text="内容是什么呢?", function=None):
                super(ProGressBar, self).__init__()

                self.function = function

                self.setWindowFlag(Qt.WindowStaysOnTopHint)
                self.setWindowIcon(QIcon("resources\image.ico"))
                self.setWindowTitle("执行中(这可能需要几分钟的时间)")

                # 居中
                self.desktop = QDesktopWidget()
                self.setGeometry(int(self.desktop.width() * 0.3), int(self.desktop.height() * 0.4),
                                 int(self.desktop.width() * 0.4), int(self.desktop.height() * 0.2))

                # 进度条
                self.bar = QProgressBar(self)
                self.pv = 0
                self.bar.setValue(self.pv)
                self.bar.setMinimum(0)
                self.bar.setMaximum(100)
                self.bar.resize(int(self.size().width() * 0.6), int(self.size().height() * 0.2))
                self.bar.move(int(self.size().width() * 0.2), int(self.size().height() * 0.3 + 30))
                self.timer = QBasicTimer()
                self.bar.show()
                self.timer.start(100, self)

                # 标签
                self.lable = QLabel(self)
                self.lable.setText(text)
                self.lable.resize(len(text) * 15, 15)
                self.lable.move(int(0.5 * self.size().width() - self.lable.size().width() * 0.5),
                                int(self.size().height() * 0.3))
                self.lable.show()
                self.show()
                self.sin = 0

            def timerEvent(self, e):
                # 这是普通的进度条

                if self.pv == 100:
                    # self.timer.stop()
                    self.close()
                elif self.pv < 90:
                    self.pv += random.randint(0, 7)
                    self.bar.setValue(self.pv)

                # elif self.function():
                #     time.sleep(1)

                else:
                    self.pv += 1
                    self.bar.setValue(self.pv)

                # 现在我们来实现一个丝滑的进度条
                # 利用我们的积分求和

                # if self.pv >=100:
                #     self.close()
                # elif  self.pv<98 :
                #     self.sin += 0.1
                #     if int(100*math.sin(0.01*self.sin))==0:
                #         self.pv += 1
                #
                #     self.pv += int(100*math.sin(0.01*self.sin))
                #
                #     self.bar.setValue(self.pv)
                # else:
                #     self.pv += 1
                #     self.bar.setValue(self.pv)
                # 但是真的问题难道不是 希望进度的最后时间结果与我们事件是否完成 同步吗
                # todo 时间完成的检查函数

        self.progressbar = ProGressBar()

    def creat_sttatusbar(self, _message):
        # todo 状态栏过于简单 我们是否可以直接 就 书写函数使用
        self.statusbar.showMessage(_message)

    def creat_menu(self):
        # todo 重写不同的菜单
        self.menubar = self.menuBar()

        self.me = self.menubar.addMenu("菜单")

        self.action_1 = QAction()
        self.action_1.setText("功能1")
        self.action_1.setIcon(QIcon("resources\image.ico"))
        self.action_1.setShortcut(Qt.CTRL + Qt.Key_Q)
        self.action_1.triggered.connect(lambda: print("执行功能一"))
        self.me.addAction(self.action_1)

        self.action_2 = QAction()
        self.action_2.setText("功能2")
        self.action_2.setIcon(QIcon("resources\image.ico"))
        self.action_2.setShortcut(Qt.CTRL + Qt.Key_W)
        self.action_2.triggered.connect(lambda:      self.creat_messagebox("警告","内存不足"))
        self.me.addAction(self.action_2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme="dark_blue.xml")
    model = Example()
    # model = ProGressBar()
    app.exec_()
