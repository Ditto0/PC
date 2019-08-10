from bs4 import BeautifulSoup
import requests
import re
import json

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

def open_url_with_proxy(url,proxy):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
    header = {"User-Agent":user_agent}
    proxies={}
    if proxy.startswith(("HTTPS","https")):
        proxies["https"] = proxy
    else:
        proxies["http"] = proxy
    try:
        r = requests.get(url,headers = header, proxies=proxies, timeout=10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return (r.text,r.status_code)
    except:
        print("网页无效"+url)
        print("无效的代理IP："+proxy)
        return False

def check_proxy(proxy):
    url = "https://www.baidu.com/"
    result = open_url_with_proxy(url,proxy)
    proxy_flag = False
    if result:
        text,status_code = result
        if status_code==200:
            r_title = re.findall("<title>.*</title>", text)
            if r_title:
                if r_title[0] =="<title>百度一下，你就知道</title>":
                    proxy_flag = True
        if proxy_flag:
            check_ip_url = "https://jsonip.com/"
            try:
                text,status_code = open_url_with_proxy(check_ip_url,proxy)
            except:
                return
            print("有效代理IP："+proxy)
            with open("valid_ip.txt","a") as f:
                f.writelines(proxy)
            try:
                source_ip = json.loads(text).get("ip")
                print(f"源IP地址为：{source_ip}")
                print("="*40)
            except:
                print("返回的非json，无法解析")
    else:
        print("无效代理IP："+proxy)



if __name__ == "__main__":
    url = "https://www.xicidaili.com/"
    proxy_ip_file="ip.txt"
    #text = openurl(url)
    #f_name = "ip.txt"
    #with open(f_name, 'w') as f:
    #    f.write(text)

    text = open(proxy_ip_file, 'r').read()
    proxy_ip_list = get_ip(text)
    proxy_ip_list.insert(0,"http://172.16.160.1:3128")
    for proxy in proxy_ip_list:
        check_proxy(proxy)
    #print(proxy_ip_list)