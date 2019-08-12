from selenium import webdriver
import  time
import lxml
import requests
import requests
from bs4 import BeautifulSoup as bs
url = "https://auth.dxy.cn/"
browser = webdriver.Chrome(executable_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
browser.get(url)




def getItem(html):
    datas = []  # 用来存放获取的用户名和评论
    for data in html.find_all("tbody"):
        try:
            userid = data.find("div", class_="auth").get_text(strip=True)
            content = data.find("td", class_="postbody").get_text(strip=True)
            datas.append((userid, content))
        except:
            pass
    for i in range(0,len(datas)):
        print(datas[i][0])
        print(datas[i][1])
        dir_file = open("DXY_re.txt","a",encoding="UTF-8")
        dir_file.write(datas[i][0]+"\n"+datas[i][1]+"\n")
        dir_file.close()
    print("抓取结束")

#打开丁香园网页
browser.get(url)
#默认是扫码登陆，切换成密码登陆
met = browser.find_element_by_link_text("返回电脑登录")
met.click()
#最大化浏览器
browser.maximize_window()
time.sleep(2)

#账号输入框
inputna=browser.find_element_by_name("username")
inputna.clear()
inputna.send_keys("18625463100")
#密码输入
inputpasswd = browser.find_element_by_name("password")
inputpasswd.clear()
inputpasswd.send_keys("hennan123")
#登陆
browser.find_element_by_xpath('//*[@class="form__button"]/button').click()
time.sleep(10)
#抓取页面
heards={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}
url = "http://www.dxy.cn/bbs/thread/626626#626626"
r = requests.get(url, headers=heards)
r.encoding="utf-8"
html = bs(r.text,"lxml")
getItem(html)
