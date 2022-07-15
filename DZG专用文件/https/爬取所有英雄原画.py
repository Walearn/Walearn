import requests as q
import json 

def check_respond(_respond):
    if _respond.status_code ==200:
        return True
    else:
        print("url is wrong")
        return False
def download_image_by_url(_url:str):
    respond = q.get(url = _url,headers=header)
    if check_respond(respond):
            # with open(_image_name+".jpg","wb") as file:
            #     file.write(respond.content)\
        location = _url.rfind("/")
        
        file = open("lol/"+_url[location+1:],"wb")
        file.write(respond.content)
        file.close()

header = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}
url = "https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js"

res = q.get(url=url,headers=header)
json_data = json.loads(res.text)
seed = "https://game.gtimg.cn/images/lol/act/img/skin/big1001.jpg"
# for i in range(len(json_data["hero"])):

for i in range(10):
    download_image_by_url(seed.replace("1001",f'{json_data["hero"][i]["heroId"]}001'))

