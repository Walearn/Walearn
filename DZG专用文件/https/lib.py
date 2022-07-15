import requests

header = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}

def check_respond(_respond):
    if _respond.status_code ==200:
        return True
    else:
        print("url is wrong")
        return False
def download_image_by_url(_url:str):
    respond = requests.get(url = _url,headers=header)
    if check_respond(respond):
            # with open(_image_name+".jpg","wb") as file:
            #     file.write(respond.content)\
        location = _url.rfind("/")
        
        file = open(_url[location+1:],"wb")
        file.write(respond.content)
        file.close()

u = "https://game.gtimg.cn/images/lol/act/img/skin/big1000.jpg"
A = "https://game.gtimg.cn/images/lol/act/img/skin/big1001.jpg"

M = "https://game.gtimg.cn/images/lol/act/img/skin/big2000.jpg"
                                    #                id + 000 .jpg
download_image_by_url(u)