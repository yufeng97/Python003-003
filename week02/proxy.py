import requests
import tqdm
from lxml import etree


def fetch(url, proxies=None):
    """
    Fetch given url page by using requests and return response html text if success
    """
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    headers = {'user-agent': user_agent,}
    try:
        if proxies:
            proxies = {'http': 'http://52.179.231.206:80'}
            res = requests.get(url, headers=headers, proxies=proxies)
        else:
            res = requests.get(url, headers=headers, )
        if res.status_code == 200:
            return res
        print("status code:", res.status_code)
    except requests.RequestException as e:
        raise e


def main():
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, '
                             'like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'}
    url = 'https://www.kuaidaili.com/free/inha/'
    res = fetch(url)
    selector = etree.HTML(res.text)
    ip = selector.xpath('//td[1]/text()')
    port = selector.xpath('//td[2]/text()')
    http_type = selector.xpath('//td[4]/text()')
    proxies = ["{}://{}:{}".format(http_type[i].lower(), ip[i], port[i]) for i in range(len(ip))]
    with open("./proxies.txt", "w") as f:
        for i in range(len(ip)):
            f.write("{}\t{}\t{}\n".format(ip[i], port[i], http_type[i].lower()))
    print(proxies)


def test_proxy():
    target_url = "https://baidu.com"
    target_url = "https://httpbin.org/ip"
    proxies = []
    with open("./proxies.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            ip, port, http_type = line.strip('\n').split('\t')
            proxy = {http_type: "{}://{}:{}".format(http_type, ip, port)}
            proxies.append(proxy)
    with open("./ip_available.txt", "w") as f:
        for proxy in proxies:
            res = fetch(target_url, proxy)
            if res:
                print(proxy)
                print(res.json())
                f.write("{}\n".format(list(proxy.values())[0]))


if __name__ == "__main__":
    # main()
    test_proxy()
