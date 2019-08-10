from bs4 import BeautifulSoup
import requests
import time

def openurl(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
    header = {"User-Agent":user_agent}
    try:
        r = requests.get(url,headers=header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("网页出错"+url)

def get_ip(respon):
    ip_list=[]
    soup =BeautifulSoup(respon,"html.parser")
    ips = soup.find(id = "ip_list").find_all("tr")
    for i in ips:
        if len(i.select('td')) >= 8:
            ip = i.select("td")[1].text
            port = i.select("td")[2].text
            protocol = i.select("td")[5].text
            if protocol in ("HTTP","HTTPS","http","https"):
                ip_list.append(f'{protocol}://{ip}:{port}')
    return ip_list

if __name__ == "__main__":
    url = "https://www.xicidaili.com/"
    text = openurl(url)
    f_name = "ip.txt"
    #print(text)
    with open(f_name, 'w') as f:
        f.write(text)
    text = open(f_name, 'r').read()
    proxy_ip_list = get_ip(text)
    print(proxy_ip_list)