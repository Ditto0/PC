from bs4 import BeautifulSoup
import requests
import time

def open_proxy_url(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
    headers = {'User-Agent': user_agent}
    try:
        r = requests.get(url, headers = headers, timeout = 20)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('无法访问网页' + url)


def get_proxy_ip(response):
    proxy_ip_list = []
    soup = BeautifulSoup(response, 'html.parser')
    proxy_ips  = soup.select('.odd')
    for proxy_ip in proxy_ips:
        ip = proxy_ip.select('td')[1].text
        port = proxy_ip.select('td')[2].text
        protocol = proxy_ip.select('td')[5].text
        if protocol in ('HTTP','HTTPS'):
            proxy_ip_list.append(f'{protocol}://{ip}:{port}')
    return proxy_ip_list

if __name__ == '__main__':
    proxy_url = 'https://www.xicidaili.com/'
    text = open_proxy_url(proxy_url)
    file_name = 'ip.txt'
    with open(file_name, 'w') as f:
        f.write(text)
    text = open(file_name, 'r').read()
    proxy_ip_list = get_proxy_ip(text)
    print(proxy_ip_list)