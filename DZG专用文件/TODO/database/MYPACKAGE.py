import os

from xlrd import open_workbook
from xlutils.copy import copy
# from os import *
from platform import *

# todo xls_book

class xls_book():
    '''我的这个的使用范围好小啊 准确将是不好用 就是因为 它读取的时候 就是 '''
    def __init__(self, _filename: str):
        self.filename = _filename
        self.book = open_workbook(self.filename)
        self.sheets = self.book.sheets()
        self.sheet = self.sheets[0]  # type:xlrd.sheet.Sheet

    def get_value_by_row_and_colum(self, _row: int, _colum: int):
        try:
            return self.sheet[_row][_colum].value
        except:
            return f"表格中的{_row}  {_colum} 存在问题 请检查"

    def rewrite_value_by_row_and_colum(self, _row: int, _colum: int, _value: str):
        '''
        我们修改xls文件 先读取 然后覆盖式保存
        :param _row:  修改的行数
        :param _colum:  修改的列数
        :param _value:  修改的内容为
        :return: 没有返回值

        '''
        self.book = open_workbook(self.filename)
        self.copy_book = copy(self.book)  # type: xlwt.Workbook.Workbook
        self.copy_sheet = self.copy_book.get_sheet(0)  # type: xlwt.Worksheet.Worksheet
        self.copy_sheet.write(_row, _colum, _value)
        self.copy_book.save(self.filename)
    def get_all_info_by_sheet(self):
        pass
        # for i in range(self.book.sheet.rows):




# todo os and sys
def insert_top_info(_filename,_info):
    """
    you could use this function to write some infomation in a cteated file

    you could see it is not effective for a big file
    because it will read all the file
    our computer is powerful so it wont cost ton much time
    """
    file = open(_filename,"r")
    info = file.readlines()
    info.insert(0,_info+"\n")
    file.close()
    file = open(_filename,"w")
    file.writelines(info)
    file.close()
def  check_platform_and_change_path(_path):
    # _path should be the Linux
    # FIXME how about apple should i write it for apple ???

    if system()=="Linux":
        return _path
    else:
        # file_list = _path.split("/")
        # return "\\".join(file_list)
        return _path.replace("/","\\")

class folder_creator:
    def __init__(self,_folder_name):
        self.Xpath = os.getcwd()
        self.folder_name = _folder_name
        # self.makefolder()
    # def makefolder(self):
        '''
        input your folder_name and creat it 
        '''
        # path = getcwd()
        Xpath = check_platform_and_change_path(self.Xpath + "/"+self.folder_name)
        if not os.path.exists(Xpath):
            os.makedirs(Xpath)
        else:
            print("文件夹已经存在")
    def makefile(self,filename):
        # print(check_platform_and_change_path(self.folder_name+"/"+filename))
        open(check_platform_and_change_path(self.folder_name+"/"+filename),"a")
# use it like this
# code = folder_creator("code")
# code.makefile("fie.txt")
# code.makefile("as.md")
# bin = folder_creator("bin")
# bin.makefile()



# todo a class for a file
class question_bank:
    '''
    qt could be a part of it
    now we should write some model for qt

    '''
    def __init__(self,_filename):
        self.filename = _filename
        self.text_pool = []


    # todo only for ulearn

    # todo  single choise

    # todo mut choise

    # todo eroor or right

    # todo anything is ok ????

# todo a key to answer



