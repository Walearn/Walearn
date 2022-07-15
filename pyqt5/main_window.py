import os
import sys
from PyQt5.QtWidgets import *
from qt_material import apply_stylesheet

from PyQt5.QtGui import *
from PyQt5.QtCore import *

from PROGRESSBAR import *
import get_config

'''
我们应该是把代码共享 这样就不会把这些乱七八糟的东西污染环境了 



'''

'''
可以选择的主题有 就是这样 哈哈 
['dark_amber.xml',
 'dark_blue.xml',
 'dark_cyan.xml',
 'dark_lightgreen.xml',
 'dark_pink.xml',
 'dark_purple.xml',
 'dark_red.xml',
 'dark_teal.xml',
 'dark_yellow.xml',
 'light_amber.xml',
 'light_blue.xml',
 'light_cyan.xml',
 'light_cyan_500.xml',
 'light_lightgreen.xml',
 'light_pink.xml',
 'light_purple.xml',
 'light_red.xml',
 'light_teal.xml',
 'light_yellow.xml']
'''


class mywindow(QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        #
        # 窗口基本信息
        self.setWindowTitle("工具箱")
        self.desktop = QDesktopWidget()
        self.setGeometry(int(self.desktop.width() * 0.25), int(self.desktop.height() * 0.15),
                         int(self.desktop.width() * 0.5), int(self.desktop.height() * 0.7))
        self.setWindowIcon(QIcon("resources\image.ico"))
        # self.setWindowFlag(Qt.WindowStaysOnTopHint)  # 窗口始终保持在所有窗口的最前面

        # 基本信息
        self.message = QMessageBox(self)
        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)

        self.cur_path = os.getcwd()
        self.lib_path = self.cur_path + "\\lib\\"
        self.get_installed_tool()
        # 方法初始化
        self.creat_menu()
        self.font = QFont('times', 18, QFont.Black)
        self.main_menu()
        self.statusbar.showMessage("hello")

        # 显示窗口
        self.show()
    def creat_n_lable(self):
        # 1 获取可用的空间大小
        print(self.size())
        print(self.button_1.size())
        print(self.button_1.geometry())
        """
        PyQt5.QtCore.QSize(960, 756)
        PyQt5.QtCore.QSize(186, 75)
        PyQt5.QtCore.QRect(19, 75, 186, 75)"""
        self.width_ = 960-19-186
        print(self.width_,756)
        # print()
        # 2 决定一行有多少个标签
        print(self.width_//100)
        for i in range(7):
            self.lable = QLabel(self)
            self.lable.resize(100,50)
            self.lable.setText(f"{i}")
            self.lable.move(186+19+i*100+50,100)
            self.lable.show()

            self.lable = QLabel(self)
            self.lable.resize(100, 50)
            self.lable.setText(f"{i}")
            self.lable.move(186 + 19 + i * 100 + 50, 200)
            self.lable.show()

    def main_menu(self):
        self.button_1 = QPushButton(self)

        self.button_1.setText("电脑基础功能")

        # self.font = QFont()
        # self.font.setFamily("times")
        # self.font.setPixelSize(30)
        # self.button_1.setFont(self.font)

        # self.sheet = self.setStyleSheet()
        # self.button_style = QStyle("font-size: 30px;color:#40e0f0")

        # self.setStyleSheet("QTableWidget{background-color: black;border:20px solid #014F84}"
        #                    "QTableWidget::item{border:1px solid #014F84}")

        self.button_1.setIcon(QIcon("resources\image.ico"))
        self.button_1.move(int(self.size().width() * 0.02), int(self.size().height() * 0.1))
        self.button_1.resize(int(self.size().width() * 0.1 + 15 * len(self.button_1.text())),
                             int(self.size().height() * 0.1))
        self.button_1.setStyleSheet("QPushButton{font-size: 20px};")
        self.button_1.clicked.connect(lambda :self.creat_n_lable())
        self.button_1.show()

        self.button_2 = QPushButton(self)
        self.button_2.setText("生活相关")
        self.button_2.setIcon(QIcon("resources\image.ico"))
        self.button_2.move(int(self.size().width() * 0.02), int(self.size().height() * 0.25))
        self.button_2.resize(int(self.size().width() * 0.1 + 15 * len(self.button_1.text())),
                             int(self.size().height() * 0.1))
        self.button_2.setStyleSheet("QPushButton{font-size: 20px};")
        self.button_2.show()

        self.button_3 = QPushButton(self)
        self.button_3.setText("其他")
        self.button_3.setIcon(QIcon("resources\image.ico"))
        self.button_3.move(int(self.size().width() * 0.02), int(self.size().height() * 0.4))
        self.button_3.resize(int(self.size().width() * 0.1 + 15 * len(self.button_1.text())),
                             int(self.size().height() * 0.1))
        self.button_3.setStyleSheet("QPushButton{font-size: 20px};")
        self.button_3.show()

        self.icon_list = []
        self.name_list = []

    # todo 去lib下寻找全部的ico 文件 和项目的名字 但是 我还是不知道
    def creat_tool(self, _icon, _name, _file_path):
        print(_name)
        print(_icon)
        """
        用于创建工具的图标 这里使用一个按钮+标签的组合 
        主要的问题在于 图标的排序问题 
        """
        icon = QPushButton(self)
        # icon.setIcon("lib/"+_file_path+"/resource/"+_icon)
        icon.move()
        icon.clicked.connect(lambda: os.popen("python "))
        icon.show()

    def get_installed_tool(self):
        """获取lib下的下载文件"""
        project_list = os.listdir(self.cur_path + "/lib")
        # for i,j in enumerate(project_list):
        #     print(i,j)
        for i in project_list:
            data = get_config.get_json_date(self.lib_path + i, )
            # self.creat_tool(data["icon"], data["name"],data["filename"])

    # 默认的功能
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

    def creat_creat_progressbar(self):
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

                font = QFont(family="楷体")
                self.setFont(font)

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
        self.menubar.setStyleSheet("font-size: 20px")
        self.menu_1 = QMenu(self)
        self.menu_1.setTitle("主菜单")
        self.base = self.menubar.addMenu(self.menu_1)
        self.base = self.menubar.addMenu("菜单")

        self.action_2 = QAction()
        self.action_2.setFont(QFont("times", 12))
        self.action_2.setText("检测文件完整性")
        self.action_2.setIcon(QIcon("resources\image.ico"))
        self.action_2.setShortcut(Qt.CTRL + Qt.Key_I)

        self.action_2.triggered.connect(lambda: self.button_1.setFont(self.font))
        self.base.addAction(self.action_2)

        self.action_3 = QAction()
        self.action_3.setFont(QFont("times", 12))
        self.action_3.setText("下载新的工具")
        self.action_3.setIcon(QIcon("resources\image.ico"))
        self.action_3.setShortcut(Qt.CTRL + Qt.Key_D)
        self.action_3.triggered.connect(lambda: print("下载新的工具"))
        self.base.addAction(self.action_3)

        self.action_4 = QAction()
        self.action_4.setFont(QFont("times", 12))
        self.action_4.setText("联系作者")
        self.action_4.setIcon(QIcon("resources\image.ico"))
        self.action_4.setShortcut(Qt.CTRL + Qt.Key_E)
        self.action_4.triggered.connect(lambda: print("联系作者"))
        self.base.addAction(self.action_4)

        self.interface = self.menubar.addMenu("切换主题")

        self.interface_action_1 = QAction()
        self.interface_action_1.setFont(QFont("times", 12))
        self.interface_action_1.setText("默认")
        # self.interface_action_1.setIcon(QIcon("resources\image.ico"))
        self.interface_action_1.setShortcut(Qt.CTRL + Qt.Key_Q)
        self.interface_action_1.triggered.connect(lambda: apply_stylesheet(self, theme="dark_blue.xml"))
        self.interface.addAction(self.interface_action_1)

        self.interface_action_2 = QAction()
        self.interface_action_2.setFont(QFont("times", 12))
        self.interface_action_2.setText("红酒")
        # self.interface_action_2.setIcon(QIcon("resources\image.ico"))
        self.interface_action_2.setShortcut(Qt.CTRL + Qt.Key_Q)
        self.interface_action_2.triggered.connect(lambda: apply_stylesheet(self, theme="dark_red.xml"))
        self.interface.addAction(self.interface_action_2)

        self.interface_action_5 = QAction()
        self.interface_action_5.setFont(QFont("times", 12))
        self.interface_action_5.setText("芥末")
        # self.interface_action_5.setIcon(QIcon("resources\image.ico"))

        self.interface_action_5.setShortcut(Qt.CTRL + Qt.Key_Q)
        self.interface_action_5.triggered.connect(lambda: apply_stylesheet(self, theme="dark_lightgreen.xml"))
        self.interface.addAction(self.interface_action_5)

        self.interface_action_3 = QAction()
        self.interface_action_3.setFont(QFont("times", 12))
        self.interface_action_3.setText("海洋")
        # self.interface_action_3.setIcon(QIcon("resources\image.ico"))
        self.interface_action_3.setShortcut(Qt.CTRL + Qt.Key_Q)
        self.interface_action_3.triggered.connect(lambda: apply_stylesheet(self, theme="light_blue.xml"))
        self.interface.addAction(self.interface_action_3)

        self.interface_action_4 = QAction()
        self.interface_action_4.setFont(QFont("times", 12))
        self.interface_action_4.setText("樱桃")
        # self.interface_action_4.setIcon(QIcon("resources\image.ico"))
        self.interface_action_4.setShortcut(Qt.CTRL + Qt.Key_Q)
        self.interface_action_4.triggered.connect(lambda: apply_stylesheet(self, theme="light_pink.xml"))
        self.interface.addAction(self.interface_action_4)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme="dark_blue.xml")
    win = mywindow()
    app.exec_()
