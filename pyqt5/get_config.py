import json
def get_config():
    file = open("config/SETTINGS.txt", "r", encoding="utf-8")
    bin_path = file.readline().split()
    time = file.readline().split()
    file.close()
    task = []
    for i in range(len(bin_path)):
        location = bin_path[i].rfind("/")
        task.append(bin_path[i][location + 1:])
    return [task, time, bin_path]


def edit_config(_bin_path, _time):
    file = open("config/SETTINGS.txt", "w", encoding="utf-8")
    file.write(" ".join(_bin_path))
    file.write("\n")
    file.write(" ".join(_time))

def get_json_date(_path):
    """
    _path 是tool 下的文件路径
    """
    file = open(_path+"\\config\\info.json","r",encoding = "utf-8")
    return json.load(file)
