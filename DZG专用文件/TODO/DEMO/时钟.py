import random
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MyClass(QMainWindow):
    def __init__(self):
        super(MyClass, self).__init__()
        self.time = QTimer()
        self.time.setInterval(1000)
        self.time.start()
        self.time.timeout.connect(lambda:print("刷新"))
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mc = MyClass()
    app.exec_()

