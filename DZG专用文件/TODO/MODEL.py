import os
import sys
import time
import PyQt5.QtCore as core
from PyQt5.QtWidgets import *
from qt_material import apply_stylesheet
import atexit
def del_tex():
    os.popen("del lock.txt")
atexit.register(del_tex)
def return_tiem_and_info():
    file = open("database/SCHEDULE.txt", "r", encoding="utf-8")
    time_list = []
    info_list = []
    file.readline()
    for i in file:
        if i == "\n":
            continue
        time = i.split("|")[0]
        time = time.strip()
        time = time.replace(".", ":")
        time_list.append(time)

        info = i.split("|")[1]
        info = info.strip()
        info_list.append(info)

    return (time_list, info_list)


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.time_list = return_tiem_and_info()[0]
        self.info_list = return_tiem_and_info()[1]
        self.desktop = QDesktopWidget()
        self.setWindowFlag(core.Qt.WindowStaysOnTopHint)

        # self.font = QFont()
        # self.font.setFamily("Arial")  # 括号里可以设置成自己想要的其它字体
        # self.font.setPointSize(90)
        self.lable_time = QLabel(self)
        self.lable_info = QLabel(self)
        self.message = QMessageBox(self)

    def creat_lable(self):

        self.time_text = "现在的时间是" + time.ctime()[11:16]
        self.lable_time.setText(self.time_text)
        self.x_posion = int(self.desktop.width() * 0.5)
        self.lable_time.resize(400, 30)


        self.lable_time.setStyleSheet("font-size:30px;")

        self.lable_time.move(int(self.x_posion - self.lable_time.size().width() * 0.5),
                             int(self.desktop.height() * 0.28))
        self.lable_time.show()
        self.lable_time.update()


        self.info_text = self.info_list[self.time_list.index(time.ctime()[11:16])]

        self.lable_info.resize(400, 30)

        self.lable_info.setText(self.info_text)

        self.lable_info.setStyleSheet("font-size:30px;")
        self.lable_info.move(int(self.x_posion - self.lable_info.size().width() * 0.5),
                             int(self.desktop.height() * 0.40))
        self.lable_info.show()
        self.lable_info.repaint()
        self.lable_info.update()

        # threading.Thread(target=lambda :self.close(self)).start()

    def close_all(self):
        time.sleep(3)
        self.close()
        self.lable_info.destroy()

    def check_time(self):
        try:
            if time.ctime()[11:16] in self.time_list:
                return True
        except:
            return False
    def messagebox(self,_text):
        self.message.setText(_text)
        self.message.move(int(self.desktop.width()*0.47),int(self.desktop.height()*0.4))
        self.message.setWindowTitle("温馨提示")

        # self.message.setIcon(QIcon(QPixmap("image.ico")))
        self.message.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme="dark_blue.xml")
    mywindow = Window()
    try:
        open("lock.txt", "x", encoding="utf-8")
        mywindow.messagebox("程序启动成功")
        while 1:
            time.sleep(60)
            if mywindow.check_time():
                mywindow.creat_lable()
                mywindow.showFullScreen()
                app.exec_()
    except:
        mywindow.messagebox("程序已经启动")
        sys.exit()

# todo you-get 现在用不了