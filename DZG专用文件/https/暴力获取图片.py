import datetime
# print(datetime.date.today())
# print(str(datetime.date.today()))
# print(str(datetime.date.today())[:-2]+"12"=="2022-07-12")

def get_yesterday():
    return (datetime.date.today() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')

    # """这个函数存在问题 如果今天是1号就gg了"""
    # date = str(datetime.date.today())
    # today = date[-2:]
    # yesterday = str(int(today)-1)
    # return date[:-2]+yesterday
