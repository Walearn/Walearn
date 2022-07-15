import random
import sys
import time

from PyQt5.QtWidgets import *
from qt_material import apply_stylesheet
from PyQt5.QtGui import *
from PyQt5.QtCore import *

'''
我们应该是把代码共享 这样就不会把这些乱七八糟的东西污染环境了 



'''

'''
目前有的功能

1:菜单
2:状态栏
3:消息
4:按钮
5: todo 进度条 (这个东西的实现方法有好多
6: 第二窗口 
'''


class ProGressBar(QWidget):
    def __init__(self,text,function):
        super(ProGressBar, self).__init__()

        self.function = function

        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon("resources\image.ico"))
        self.setWindowTitle("执行中(这可能需要几分钟的时间)")

        # 居中
        self.desktop = QDesktopWidget()
        self.setGeometry(int(self.desktop.width() * 0.3), int(self.desktop.height() * 0.4),
                         int(self.desktop.width() * 0.4), int(self.desktop.height() * 0.2))


        self.bar = QProgressBar(self)
        self.pv = 0
        self.bar.setValue(self.pv)
        self.bar.setMinimum(0)
        self.bar.setMaximum(100)
        self.bar.resize(int(self.size().width()*0.6),int(self.size().height()*0.2))
        self.bar.move(int(self.size().width()*0.2),int(self.size().height()*0.3+30))
        self.timer = QBasicTimer()
        self.bar.show()
        self.timer.start(100,self)

        self.lable = QLabel(self)
        self.lable.setText(text)
        self.lable.resize(len(text) * 15, 15)
        self.lable.move(int(0.5*self.size().width()-self.lable.size().width()*0.5),int(self.size().height()*0.3))
        self.lable.show()
        self.show()

    def timerEvent(self, e):
        if self.pv==100:
            # self.timer.stop()
            self.close()
        elif self.pv<90:
            self.pv+=random.randint(0,7)
            self.bar.setValue(self.pv)
        # elif self.function():
            # time.sleep(1)
        else:
            self.pv+=1
            self.bar.setValue(self.pv)


# app = QApplication(sys.argv)
# apply_stylesheet(app, theme="dark_blue.xml")
# bar = ProGressBar("标题","neirong")
# app.exec_()


