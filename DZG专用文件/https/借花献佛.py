import json
import os
import requests as q
import datetime


def get_yesterday():
    return (datetime.date.today() + datetime.timedelta(days=-10)).strftime('%Y-%m-%d')


def check_respond(_respond):
    if _respond.status_code == 200:
        return True
    else:
        return False


def download_image_by_url(_url: str):
    respond = q.get(url=_url, headers=header)
    if check_respond(respond):
        # with open(_image_name+".jpg","wb") as file:
        #     file.write(respond.content)\
        location = _url.rfind("/")
        file = open(f"{yesterday}/" + _url[location + 1:], "wb")
        file.write(respond.content)
        file.close()


def check_init():
    if os.path.exists(f"{yesterday}"):
        os._exit()
    else:
        os.popen(f"mkdir {yesterday}")
yesterday = get_yesterday()
check_init()

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}
url = f"https://api.bbmang.me/ranks?page=1&date={yesterday}&mode=day&pageSize=30"
res = q.get(url=url, headers=header)
json_data = json.loads(res.text)
task_num = len(json_data["data"])
for i in range(task_num):
    print(i, task_num)
    download_image_by_url(
        json_data["data"][i]["imageUrls"][0]["large"].replace("i.pximg.net", "proxy.pixivel.moe"))
