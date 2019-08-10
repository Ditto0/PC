import requests
import re

#状态码
#200 - 请求成功
#301 - 资源（网页等）被永久转移到其它URL
#404 - 请求的资源（网页等）不存在
#500 - 内部服务器错误*/

def openurl(url):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
    headers={"User-Agent":user_agent}
    try:
        r = requests.get(url,headers=headers,timeout=20)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("无法访问网页"+url)

if __name__=="__main__":
    douban_250=[]

    for i in range(10):
        url = "https://movie.douban.com/top250?start="
        url += str(i*25)
        text =openurl(url)
        #print(text)
        ranks = re.findall('<em class="">(.*)</em>',text)
        move_name = re.findall('<img width="100" alt="(.*)" src="https:',text)
        counties = re.findall('&nbsp;/&nbsp;(.*)&nbsp;/&nbsp;',text)
        directors = re.findall('导演: (.*)&nbsp;&nbsp;&nbsp;',text)

        z = zip(ranks,move_name,counties,directors)
        for i in z:
            douban_250.append(i)

    with open('douban250.txt','w',encoding='utf-8') as f:
        for i in douban_250:
            f.writelines(str(i)+'\n')