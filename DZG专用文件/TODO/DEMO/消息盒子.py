import sys
import time
import PyQt5.QtCore as core
from PyQt5.QtWidgets import *
from qt_material import apply_stylesheet
from PyQt5.QtGui import *
import threading


class mywindow(QWidget):
    def __init__(self):
        super(mywindow, self).__init__()

        self.setWindowTitle("窗口标题")

        self.setWindowFlag(core.Qt.WindowStaysOnTopHint) # 窗口始终保持在所有窗口的最前面
        self.show()


        self.message = QMessageBox(self)
        self.but = QPushButton(self)
        self.but.setText("显示消息")
        self.but.clicked.connect(lambda:self.mess("标题","显示的内容"))

        self.but.move(100,100)
        self.but.show()

        self.show_question()

    def mess(self,_title,_text):
        self.message.setText(_text)
        self.message.setWindowTitle(_title)
        self.message.show()

        #确实我们是要写出很优秀的GUI 不是 只是一个可以使用的就好 现在启动我们的 break
    def show_and_hide(self,object):
        print("hide")
        object.hide()
    def show_question(self):
        # todo 重写不同的指令
        """创建一个提问消息
        需要重写
        """
        reply = QMessageBox.question(self, 'title',
                                     "Are you sure to quit? info ", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            pass

        else:
            pass






app = QApplication(sys.argv)
apply_stylesheet(app, theme="dark_blue.xml")
win = mywindow()
app.exec_()



# if __name__=="__main__":
#     app = QApplication(sys.argv)
#     win = mywindow()
#     app.exec_()
