import requests
from bs4 import BeautifulSoup as bs
import lxml
def getItem(html):
    datas = [] # 用来存放获取的用户名和评论
    for data in html.find_all("tbody"):
        try:
            userid = data.find("div", class_="auth").get_text(strip=True)
            print(userid)
            content = data.find("td", class_="postbody").get_text(strip=True)
            print(content)
            datas.append((userid,content))
        except:
            pass

if __name__ == '__main__':
    heards={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}
    url = "http://www.dxy.cn/bbs/thread/626626#626626"
    r = requests.get(url, headers=heards)
    r.encoding="utf-8"
    html = bs(r.text,"lxml")
    getItem(html)


